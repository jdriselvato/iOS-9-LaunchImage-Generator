#!/usr/bin/python
import urllib, os, argparse
from argparse import RawTextHelpFormatter

#defaults
color_arg = "33ccff" # background color

# Setting up command line arguments
parser = argparse.ArgumentParser(
	description = "LaunchImage - LaunchImage generator support iOS 9\n\nExample: ./LaunchImage-Generator.py --color 007300",
	formatter_class=RawTextHelpFormatter
	)
parser.add_argument('--color', help='To set the color use a HEX formated color without hashtag (#)', action='store_true')

parsed, args = parser.parse_known_args()

# Handling arguments
# if parsed == True:
if len(args) == 1:
	color_arg = args[0]

# images_dict = {file_name : size}
images_dict = { 
	'iphone_Retina-HD-5_5-Portrait': '1242x2208',
	'iphone_Retina-HD-4_7-Portrait': '750x1334',
	'iphone_Retina-HD-5_5-Landscape': '2208x1242',
	'iphone_iOS7-9@2x-Portrait': '640x960',
	'iphone_iOS7-9_Retina-4-Portrait': '640x1136',
	'ipad_iOS7-9@1x-Portrait': '768x1024',
	'ipad_iOS7-9@2x-Portrait': '1536x2048',
	'ipad_iOS7-9@1x-Landscape': '1024x768',
	'ipad_iOS7-9@2x-Landscape': '2048x1536',
	'iphone_iOS5-6@1x-Portrait': '320x480',
	'iphone_iOS5-6@2x-Portrait': '640x960',
	'iphone_iOS5-6_Retina-4-Portrait': '640x1136',
	'ipad_without_statusbar_iOS5-6@1x-Portrait': '768x1004',
	'ipad_without_statusbar_iOS5-6@2x-Portrait': '1536x2008',
	'ipad_iOS5-6@1x-Portrait': '768x1024 ',
	'ipad_iOS5-6@2x-Portrait': '1536x2048',
	'ipad_without_statusbar_iOS5-6@1x-Landscape': '1024x748',
	'ipad_without_statusbar_iOS5-6@2x-Landscape': '2048x1496',
	'ipad_iOS5-6@1x-Landscape': '1024x768',
	'ipad_iOS5-6@2x-Landscape': '2048x1536',
};

# Check if LaunchImages folder exists if not make it
# we store the images in this folder
storage_folder = "./LaunchImages"
if not os.path.exists(storage_folder) :
	os.makedirs(storage_folder)

# loop through the images_dict to generate the images and store them in /LaunchImages
# http://dummyimage.com/{size}/{background-color}/{forground-color}.png
for key, value in images_dict.iteritems() :
	file_name = os.path.join(storage_folder, "{}.png".format(key))
	urllib.urlretrieve("http://dummyimage.com/{}/{}/{}.png".format(value, color_arg, color_arg), file_name)

