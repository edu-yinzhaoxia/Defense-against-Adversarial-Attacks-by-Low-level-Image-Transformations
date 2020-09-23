# Defense-against-Adversarial-Attacks-by-Low-level-Image-Transformations
This code is the implementation of the adversarial defense method introduced in the paper "Defense against Adversarial Attacks by Low-level Image Transformations".

There are three parts:

1. Generate adversarial examples:
python all_attack.py
 
2. Flip adversarial examples:
python FlipImages.py /Mycode_path/Adversarial_image/

3. Two ways of WebP compression:
- Single image compression
cwebp -q quality_factor input.png -o output.webp
eg: cwebp -q 60 airliner.jpg  -o airliner.webp
- Batch compress images
python __init__.py --c --ignore-transparency-image -q=quality_factor 
eg: python __init__.py --c --ignore-transparency-image -q=60
