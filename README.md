<div id="top"></div>


<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">music-generator</h3>

  <p align="center">
    Multi-Instrument music generation using C-RNN-GAN with MIDI format input
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/seyedsaleh/music-generator">View Demo</a>
    ·
    <a href="https://github.com/seyedsaleh/music-generator/issues">Report Bug</a>
    ·
    <a href="https://github.com/seyedsaleh/music-generator/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#results">Results</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#dataset">Dataset</a></li>
    <li><a href="#refereces">Refereces</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

![Product Name Screen Shot][product-screenshot]


Here's why:
* Your time should be focused on creating something amazing. A project that solves a problem and helps others
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

Major frameworks/libraries used to this project:

* [Python 3.8](https://www.python.org/)
* [Tensorflow , Keras](https://www.tensorflow.org/)
* [Midi2audio](https://github.com/bzamecnik/midi2audio)
* [Music21](https://web.mit.edu/music21/)
* [Numpy](https://numpy.org/)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- PARTS -->
## Project Parts
**CUDA** is a parallel computing platform interface that allows software developers to use GPUs for ML computing.

The project has been done with aid of GPU Computing and the use of NVIDIA cuDNN and NVIDIA CUDA Toolkit. It helped us to use Tensorflow with GPU support for computing and learning with more compatibility.
The model has been trained on an **NVIDIA GeForce GTX 1080Ti GPU**.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [x] Add Changelog
- [x] Add back to top links
- [ ] Add Additional Templates w/ Examples
- [ ] Add "components" document to easily copy & paste sections of the readme
- [ ] Multi-language Support
    - [ ] Chinese
    - [ ] Spanish

See the [open issues](https://github.com/othneildrew/Best-README-Template/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- RESULTS -->
## Results

![GAN_Loss_per_Epoch_final C](https://user-images.githubusercontent.com/47852354/141289514-87b11009-2835-407f-8cf3-dc99ed860811.png)

https://user-images.githubusercontent.com/47852354/141285440-be56d13f-abb4-4956-9ae3-c6845ed1fd12.mov

https://user-images.githubusercontent.com/47852354/141285431-a525b350-857f-470a-9465-7935a80a06d6.mov


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- DATASET -->
## Dataset

GiantMIDI-Piano is a classical piano MIDI dataset contains 10,854 MIDI files of 2,786 composers. The curated subset by constraining composer surnames contains 7,236 MIDI files of 1,787 composers. GiantMIDI-Piano are transcribed from live recordings with a high-resolution piano transcription system.
[find out more on Github](https://github.com/bytedance/GiantMIDI-Piano)
* *Qiuqiang Kong, Bochen Li, Jitong Chen, and Yuxuan Wang. "GiantMIDI-Piano: A large-scale MIDI dataset for classical piano music." arXiv preprint arXiv:2010.07061 (2020). https://arxiv.org/pdf/2010.07061* 

This model has been trained on a NVIDIA GeForce GTX 1080Ti GPU. 
To download the trained model (.h5 keras compatible format) contact us.

<p align="right">(<a href="#top">back to top</a>)</p>




<!-- REFERENCES -->
## Refereces

[1] *Mogren, Olof. (2016). C-RNN-GAN: Continuous recurrent neural networks with adversarial training. [arXiv:1611.09904](https://arxiv.org/abs/1611.09904).* 

[2] *“Generating Music with GANs—An Overview and Case Studies” at ISMIR 2019 (November 4th at Delft, The Netherlands). [salu133445.github.io/ismir2019tutorial](https://salu133445.github.io/ismir2019tutorial/).* 

[3] *Goodfellow, Ian & Pouget-Abadie, Jean & Mirza, Mehdi & Xu, Bing & Warde-Farley, David & Ozair, Sherjil & Courville, Aaron & Bengio, Y.. (2014). Generative Adversarial Nets.  [ArXiv](https://arxiv.org/abs/1406.2661).* 

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Seyedmohammadsaleh Mirzatabatabaei - [@seyedsaleh](https://github.com/seyedsaleh) - seyedsaleh.edu@gmail.com

Salman Amimotlagh - [@SMotlaq](https://github.com/SMotlaq) - pilot.motlaq@gmail.com


Project Link: [https://github.com/seyedsaleh/music-generator](https://github.com/seyedsaleh/music-generator)

<p align="right">(<a href="#top">back to top</a>)</p>


---
<div align="center">
<p>
 <img src="https://user-images.githubusercontent.com/47852354/138564509-b5dffb4e-f48b-4db5-b8a4-1385ef2b22c8.png" width="110">
 <img src="https://user-images.githubusercontent.com/47852354/138607395-e18bfc7a-204c-495a-914f-bd5cf8436ca4.jpg" width="70">
</p>
</div>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/seyedsaleh/music-generator.svg?style=for-the-badge
[contributors-url]: https://github.com/seyedsaleh/music-generator/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/seyedsaleh/music-generator.svg?style=for-the-badge
[forks-url]: https://github.com/seyedsaleh/music-generator/network/members
[stars-shield]: https://img.shields.io/github/stars/seyedsaleh/music-generator.svg?style=for-the-badge
[stars-url]: https://github.com/seyedsaleh/music-generator/stargazers
[issues-shield]: https://img.shields.io/github/issues/seyedsaleh/music-generator.svg?style=for-the-badge
[issues-url]: https://github.com/seyedsaleh/music-generator/issues
[license-shield]: https://img.shields.io/github/license/seyedsaleh/music-generator.svg?style=for-the-badge
[license-url]: https://github.com/seyedsaleh/music-generator/blob/master/LICENSE.txt
[product-screenshot]: https://user-images.githubusercontent.com/47852354/141186269-d31ec094-8061-4edc-b862-8e1deb3da46f.png
