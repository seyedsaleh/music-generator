from MIDI import MIDI

class MODEL():
  def __init__(self, midi_obj):
    self.midi = midi_obj
    self.seq_length = self.midi.seq_length
    self.seq_shape = (self.seq_length, 1)
    self.latent_dim = 1000
    self.disc_loss = []
    self.gen_loss = []

    optimizer = Adam(0.0002, 0.5)

    # Build and compile the discriminator
    self.discriminator = self.build_discriminator()
    self.discriminator.compile(loss='binary_crossentropy', optimizer=optimizer, metrics=['accuracy'])

    # Build the generator
    self.generator = self.build_generator()

    # The generator takes noise as input and generates note sequences
    z = Input(shape=(self.latent_dim, 1))
    generated_seq = self.generator(z)

    # For the combined model we will only train the generator
    self.discriminator.trainable = False

    # The discriminator takes generated images as input and determines validity
    validity = self.discriminator(generated_seq)

    # The combined model  (stacked generator and discriminator)
    # Trains the generator to fool the discriminator
    self.combined = Model(z, validity)
    self.combined.compile(loss='binary_crossentropy', optimizer=optimizer)

  def build_discriminator(self):
    model = Sequential()
    model.add(LSTM(512, input_shape=self.seq_shape, return_sequences=True))
    model.add(Bidirectional(LSTM(512)))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(Dense(1, activation='sigmoid'))
    # model.summary()

    seq = Input(shape=self.seq_shape)
    validity = model(seq)

    return Model(seq, validity)

  def build_generator(self):
    model = Sequential()
    model.add(LSTM(512, input_shape=(self.latent_dim, 1), return_sequences=True))
    model.add(Bidirectional(LSTM(512)))
    model.add(Dense(256))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(512))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(1024))
    model.add(LeakyReLU(alpha=0.2))
    model.add(BatchNormalization(momentum=0.8))
    model.add(Dense(np.prod(self.seq_shape), activation='tanh'))
    model.add(Reshape(self.seq_shape))
    # model.summary()

    noise = Input(shape=(self.latent_dim, 1))
    seq = model(noise)

    return Model(noise, seq)

  def train(self, epochs, dataFolder, batch_size=128, sample_interval=50):
    # Load and the data
    notes = self.midi.parser(dataFolder)
    sequences = self.midi.prepare_sequences()

    print(f"\nNumber of sequences for train: {sequences.shape[0]}\n")

    # Adversarial ground truths
    real = np.ones((batch_size, 1))
    fake = np.zeros((batch_size, 1))

    # Training the model
    for epoch in range(epochs):
      # Training the discriminator
      # Select a random batch of note sequences
      index_seqs = np.random.randint(0, sequences.shape[0], batch_size)
      real_seqs = sequences[index_seqs]

      # Random noise for generator input
      noise = np.random.normal(0, 1, (batch_size, self.latent_dim))

      # Generate a batch of new note sequences
      gen_seqs = self.generator.predict(noise)

      # Train the discriminator
      d_loss_real = self.discriminator.train_on_batch(real_seqs, real)
      d_loss_fake = self.discriminator.train_on_batch(gen_seqs, fake)
      d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)

      #  Training the Generator
      noise = np.random.normal(0, 1, (batch_size, self.latent_dim))

      # Train the generator (to have the discriminator label samples as real)
      g_loss = self.combined.train_on_batch(noise, real)

      # Print the progress and save into loss lists
      if epoch % sample_interval == 0:
          print("%d / %d [D loss: %f, acc.: %.2f%%] [G loss: %f]" % (
          epoch + 1, epochs, d_loss[0], 100 * d_loss[1], g_loss))
          self.disc_loss.append(d_loss[0])
          self.gen_loss.append(g_loss)

    print(f"The C-RNN-GAN model have been trained with {dataFolder} midi music,\n" +
          "and you can save your model using save method.")
    

  def save(self):
    # create Model directory if there isn't exist
    if not os.path.exists('Model/'):
      os.makedirs('Model/')

    # save discriminator and generator trained model
    self.discriminator.save('Model/discriminator.h5')
    self.generator.save('Model/generator.h5')
    print("The trained C-RNN-GAN model (generator and discriminator) have been saved in the Model folder.")


  def generate(self):
    """ Use random noise to generate music"""
    
    # random noise for network input
    noise = np.random.normal(0, 1, (1, self.latent_dim))
    predictions = self.generator.predict(noise)

    # transfer sequence numbers to notes
    boundary = int(len(self.midi.transfer_dic) / 2)
    pred_nums = [x * boundary + boundary for x in predictions[0]]
    notes = [key for key in self.midi.transfer_dic]
    pred_notes = [notes[int(x)] for x in pred_nums]
    
    # create Result directory if there isn't exist
    if not os.path.exists('Result/'):
      os.makedirs('Result/')
        
    # generate music with .midi format
    self.midi.create_midi(pred_notes, 'Result/gan_final')


  def plot_loss(self):
    """ Plot and save discriminator and generator loss functions per epoch diagram"""
    plt.plot(self.disc_loss, c='red')
    plt.plot(self.gen_loss, c='blue')
    plt.title("GAN Loss per Epoch")
    plt.legend(['Discriminator', 'Generator'])
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.show()
    plt.savefig('Result/GAN_Loss_per_Epoch_final.png', transparent=True)
    plt.close()