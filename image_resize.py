import argparse
import warnings
import os.path as op
from PIL import Image


def resize_image(image_path, output_path, width=None, height=None, scale=None):
    img = Image.open(image_path)
    if scale:
        if width or height:
            raise ValueError("Scale is specified with width or height "
                             "at the same time.")
        else:
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)
    else:
        if width or height:
            new_width = width if width else (img.width * height) // img.height
            new_height = height if height else (img.height * width) // img.width
        else:
            new_width, new_height = img.width, img.height
    if not output_path:
        root_part = op.splitext(image_path)[0]
        ext_part = op.splitext(image_path)[1]
        output_path = "%s__%dx%d%s" % (root_part, new_width,
                                       new_height, ext_part)
    output_img = img.resize((new_width, new_height))
    output_img.save(output_path)
    img.close()
    output_img.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Image resizer")
    parser.add_argument("imagepath", help="path to image you want to resize")
    parser.add_argument("-w", "--width", help="desired width of image",
                        type=int)
    parser.add_argument("-a", "--height", help="desired height of image",
                        type=int)
    parser.add_argument("-s", "--scale", help="desired scale to decrease"
                                              "(increase) image", type=float)
    parser.add_argument("-o", "--output", help="path for resized image")
    args = parser.parse_args()
    try:
        resize_image(args.imagepath, args.output,
                     args.width, args.height, args.scale)
    except (FileNotFoundError, ValueError) as img_error:
        print("Something went wrong!", img_error)
        print("Exiting...")
        exit()
