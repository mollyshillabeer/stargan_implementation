## StarGAN - Molly Shillabeer

This repository provides a modified PyTorch implementation of the model proposed in the following paper:
> **StarGAN: Unified Generative Adversarial Networks for Multi-Domain Image-to-Image Translation**<br>
> https://arxiv.org/abs/1711.09020 <br>
>
> **Abstract:** *Recent studies have shown remarkable success in image-to-image translation for two domains. However, existing approaches have limited scalability and robustness in handling more than two domains, since different models should be built independently for every pair of image domains. To address this limitation, we propose StarGAN, a novel and scalable approach that can perform image-to-image translations for multiple domains using only a single model. Such a unified model architecture of StarGAN allows simultaneous training of multiple datasets with different domains within a single network. This leads to StarGAN's superior quality of translated images compared to existing models as well as the novel capability of flexibly translating an input image to any desired target domain. We empirically demonstrate the effectiveness of our approach on a facial attribute transfer and a facial expression synthesis tasks.*

## Dependencies
* [Python 3.5+](https://www.continuum.io/downloads)
* [PyTorch 0.4.0+](http://pytorch.org/)


## Downloading the dataset
Download the CelebA dataset from: https://www.dropbox.com/s/d1kjpkqklf0uw77/celeba.zip?dl=0
Unzip and place the contents of the images folder into the stargan\data\celeba\images folder.
Place the list_attr_celeba.txt file into the stargan\data\celeba folder.

## Training networks
To train and test StarGAN on CelebA, run the the following commands in your terminal. 

```bash
# Train StarGAN using the CelebA dataset
python main.py --mode train

# Test StarGAN using the CelebA dataset **the model must be trained before testing
python main.py --mode test
```
The results of my training can be accessed under stargan\stargan_celeba\results.