# Defense against Adversarial Attacks by Low level Image Transformations

This code is the implementation of the adversarial defense method introduced in the paper "Defense against Adversarial Attacks by Low-level Image Transformations".

[Paper Link](https://onlinelibrary.wiley.com/doi/abs/10.1002/int.22258)

## Abstract

Deep neural networks (DNNs) are vulnerable to adversarial examples, which can fool classifiers by maliciously adding imperceptible perturbations to the original input. Currently, a large number of research on defending adversarial examples pay little attention to the real‐world applications, either with high computational complexity or poor defensive effects. Motivated by this observation, we develop an efficient preprocessing module to defend adversarial attacks. Specifically, before an adversarial example is fed into the model, we perform two low‐level image transformations, WebP compression and flip operation, on the picture. Then we can get a de‐perturbed sample that can be correctly classified by DNNs. WebP compression is utilized to remove the small adversarial noises. Due to the introduction of loop filtering, there will be no square effect like JPEG compression, so the visual quality of the denoised image is higher. And flip operation, which flips the image once along one side of the image, destroys the specific structure of adversarial perturbations. By taking class activation mapping to localize the discriminative image regions, we show that flipping image may mitigate adversarial effects. Extensive experiments demonstrate that the proposed scheme outperforms the state‐of‐the‐art defense methods. It can effectively defend adversarial attacks while ensuring only slight accuracy drops on normal images.

## How to use the code

There are three parts:

1. Generate adversarial examples:
   python all_attack.py

2. Flip adversarial examples:
   python FlipImages.py /Mycode_path/Adversarial_image/

3. Two ways of WebP compression:

   - Single image compression

     `cwebp -q quality_factor input.png -o output.webp`

     e.g. `cwebp -q 60 airliner.jpg  -o airliner.webp`

   - Batch compress images
     `python __init__.py --c --ignore-transparency-image -q=quality_factor `

     e.g. `eg: python __init__.py --c --ignore-transparency-image -q=60`

## How to cite our paper

    @article{yin2020defense,
     title={Defense against adversarial attacks by low-level image transformations}, 
     author={Yin, Zhaoxia and Wang, Hua and Wang, Jie and Tang, Jin and Wang, Wenzhong}, 
     journal={International Journal of Intelligent Systems}, 
     volume={35}, 
     number={10},
     pages={1453--1466}, 
     year={2020}, 
     publisher={Wiley Online Library}
    }

   

   

