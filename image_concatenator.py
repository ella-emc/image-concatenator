# This script attaches two images at a common point.

# This script takes 2 command-line arguments of JPEG, JPG, and PNG format.
# It reads the two images. It flags the point in the second image where the first image ends.
# Then it connects the two images at that point.
# It outputs a third image, which is the merged one.

import sys
import os.path
import PIL


def main():
    extensions = [".png", ".jpeg", ".jpg"]

    if len(sys.argv) == 3:
        img1, img2 = sys.argv[1:]
        # check if file extension is image file
        if img1.endswith(tuple(extensions)) and img2.endswith(tuple(extensions)):
            img1_ext = os.path.splitext(img1)
            img2_ext = os.path.splitext(img2)
            if img1_ext[1] == img2_ext[1]:
                # Check if image1 exists
                try:
                    upper = PIL.Image.open(img1)
                except FileNotFoundError:
                    sys.exit(f"{img1} not found")
                
                # Check if image2 exists
                try:
                    lower = PIL.Image.open(img2)
                except FileNotFoundError:
                    sys.exit(f"{img2} not found")
                
                # Do stuff


            else:
                sys.exit(f"{img1} extension does not match {img2} extension")
        else:
            sys.exit("File format is not supported")
    elif len(sys.argv) < 3:
        sys.exit("Too few arguments")
    else:
        sys.exit("Too many arguments")


def get_end_img1(image1):
    """
    Locate the common point from image1, then crop (separate function)
    """


def crop_image1(arg):
    """
    Crop image1
    """


def get_start_img2(image2):
    """
    Locate the common point from image2
    """


def attach(arg1, arg2):
    """
    Attach image1 and image2
    """


if __name__ == '__main__':
    main()