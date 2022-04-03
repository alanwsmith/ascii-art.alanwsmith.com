#!/usr/bin/env python3

import PIL.Image
import os

from pathlib import Path


ASCII_CHARS = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']



# def list_dir(root_dir, recursive=True, show_hidden=False, subdir='', fileList=[]):
#     # Make sure it's a full path
#     root_dir = Path(root_dir).resolve()
#     subdir_expanded = os.path.join(root_dir, subdir)





def resize_image(image, new_width):
    width, height = image.size
    ratio = height / width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


def make_grayscale(image):
    grayscaled = image.convert('L')
    return grayscaled


def make_ascii(image):
    pixels = image.getdata()
    characters = ''.join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return characters


def main():
    desired_width = 100
    path = "/Users/alan/Graphics/thinker.jpg"
    image = PIL.Image.open(path)
    new_sized = resize_image(image, desired_width)
    new_grayscale = make_grayscale(new_sized)
    raw_ascii = make_ascii(new_grayscale)

    with open('thinker-100.txt', 'w') as f:
        for indx, i in enumerate(raw_ascii):
            if indx % desired_width == 0:
                f.write("\n")
            f.write(i)









if __name__ == '__main__':
    main()

    # for root, dirs, files in os.walk('/Users/alan/workshop/_delete_after_checking/dotfiles/espanso'):
    #     print(root)
    #     print(dirs)
    #     print(files)


