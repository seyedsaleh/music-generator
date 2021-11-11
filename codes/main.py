from MIDI import MIDI
from MODEL import MODEL

if __name__ == '__main__':
    midi = MIDI(seq_length=100)
    model = MODEL(midi_obj=midi)
    model.train(5, dataFolder='data', batch_size=128, sample_interval=1)    
    model.save()
    model.generate()
    model.plot_loss()