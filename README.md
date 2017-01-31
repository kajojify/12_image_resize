12_image_resize
===================
The script is a console image resizer. It changes the size of image that takes as input. It takes several parameters:

image_resize.py [-h] [-w WIDTH] [-a HEIGHT] [-s SCALE] [-o OUTPUT] imagepath

`imagepath`    -  required parameter. It specifies the path to image for resizing.

`-w --width`   -  optional parameter. Desired width of image.

`-a --height`  -  optional parameter. Desired height of image.

`-s --scale`   -  optional parameter. Desired scale.

`-o --output`  -  optional parameter. The path for resized image.

`-h --help`    -  help reference.

The size of resized image are based on these parameters.

If script takes only width (height) parameter, image will be resized in consideration of ratio.

If script takes width and height parameters, image will be resized excluding the ratio. 

If script takes scale parameter, it can't take width or height parameter(s) at the same time. Otherwise, exception is raised.

If output parameter isn't set, resized image will be put into the same folder with original image and will be named "imagename__widthxheight.extension". 

How to run
----------
Clone this repository. Then go to the repository directory.
Install all requirements:
```
pip3 install -r requirements.txt
```
Run the script with parameters you need:
```
python3 image_resize.py [-h] [-w WIDTH] [-a HEIGHT] [-s SCALE] [-o OUTPUT] imagepath
```

Usage
-----

```
~$ python3 image_resize.py ~/pic.jpg -w 480 -a 580 -s 3
Something went wrong! Scale is specified with width or height at the same time.
Exiting...

~$ python3 image_resize.py ~/pic.jpg -o ~/Документы/pic.jpg -w 480 -a 580

```
