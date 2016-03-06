# _*_ coding=utf-8 _*_
__author__ = 'patrick'

from PIL import Image
from PIL.ImageDraw import ImageDraw

def read_content():
    with open('content.txt', 'r') as f:
        readmeText = f.read();

    return f, readmeText


def generate_image():
    '''Create our references.'''
    img = Image.new("RGBA", (100, 80), "white")
    '''Draw the images size and background to the screen.'''
    draw = ImageDraw.Draw(img)
    '''Position the text with an x/y of 10 x 10, assign it the text value and text color of red.'''
    output = draw.text((10, 10), readmeText, fill=(255, 0, 0, 255))
    '''Draw the text to the screen.'''
    draw = ImageDraw.Draw(img)
    '''Save the image.'''
    img.save("output.png")
    '''Return the results to each as a reference variable.'''
    return draw, img, output


openFile, readmeText = read_content()
draw, img, output = generate_image()

