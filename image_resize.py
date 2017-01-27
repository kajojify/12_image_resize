import argparse
import warnings
import os.path as op
from PIL import Image


def resize_image(image_path, output_path, width=None, height=None, scale=None):
    if not op.exists(image_path):
        raise FileNotFoundError("The image %s doesn't exist." % image_path)
    img = Image.open(image_path)
    if scale:
        if width or height:
            raise ValueError("Scale is specified with width or height "
                             "at the same time.")
        else:
            new_width = int(img.width * scale)
            new_height = int(img.height * scale)
    else:
        if not width and height:
            new_width = (img.width * height) // img.height
            new_height = height
        elif width and not height:
            new_height = (img.height * width) // img.width
            new_width = width
        elif width and height:
            new_width, new_height = width, height
            ratio = img.height / img.width
            new_ratio = new_height / new_width
            if ratio != new_ratio:
                message = """Aspect ratio of resized image will be
                             different from ratio of original image!"""
                warnings.warn(message)
        else:
            new_width, new_height = img.width, img.height
    if not output_path:
        root_part = op.splitext(image_path)[0]
        ext_part = op.splitext(image_path)[1]
        output_path = "%s__%dx%d%s" % (root_part, new_width,
                                       new_height, ext_part)
    else:
        output_dir = op.split(output_path)[0]
        if not op.isdir(output_dir):
            raise FileNotFoundError("The dir %s doesn't exist." % output_dir)
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
