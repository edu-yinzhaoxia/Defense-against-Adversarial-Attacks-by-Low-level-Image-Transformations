#### Generate adversarial examples
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import numpy as np
import matplotlib.pyplot as plt
import torch
import torch.optim as optim
import torch.utils.data as data_utils
from torch.autograd import Variable
import math
import torchvision.models as models
from PIL import Image
from deepfool import deepfool
import scipy
from scipy.misc import imsave
import os
os.environ['CUDA_VISIBLE_DEVICES']='5' # Point to a specific GPU

net = models.inception_v3(pretrained=True)

# Switch to evaluation mode
net.eval()

folder = '/home/yidaqiang/HH/DDD/WebP+Flip_code/1_Attack/Original_image/' # The path of the folder where the original images are located
filenames   = os.listdir(folder)
for line, filename in enumerate(filenames):
    
    im_orig = Image.open(folder + filename)
    
    mean = [ 0.485, 0.456, 0.406 ]
    std = [ 0.229, 0.224, 0.225 ]
    
    
    # Remove the mean
    im = transforms.Compose([
        transforms.Scale(299),
        transforms.CenterCrop(299),
        transforms.ToTensor(),
        transforms.Normalize(mean = mean,
                             std = std)])(im_orig)
    
    r, loop_i, label_orig, label_pert, pert_image = deepfool(im, net)  # Use deepfool to generate adversarial examples
    
    labels = open(os.path.join('synset_words.txt'), 'r').read().split('\n')
    
    str_label_orig = labels[np.int(label_orig)].split(',')[0] # Original image classification label
    str_label_pert = labels[np.int(label_pert)].split(',')[0] # Perturbed image classification label

    print("Original label = ", str_label_orig)
    print("Perturbed label = ", str_label_pert)
    
    def clip_tensor(A, minv, maxv):
        A = torch.max(A, minv*torch.ones(A.shape))
        A = torch.min(A, maxv*torch.ones(A.shape))
        return A
    
    clip = lambda x: clip_tensor(x, 0, 255)
    
    tf = transforms.Compose([transforms.Normalize(mean=[0, 0, 0], std=map(lambda x: 1 / x, std)),
                            transforms.Normalize(mean=map(lambda x: -x, mean), std=[1, 1, 1]),
                            transforms.Lambda(clip),
                            transforms.ToPILImage(),
                            transforms.CenterCrop(299)])
    
    plt.figure()
    img = tf(pert_image.cpu()[0])
    plt.imshow(img)
    imsave('Adversarial_image/Adv_{}-{}.png'.format(str_label_orig,str_label_pert),img) # Save generated adversarial examples
    
    plt.title(str_label_pert)
    plt.show()
