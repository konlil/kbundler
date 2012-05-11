# -*- coding: utf8 -*-
import os
from PIL import Image
from PIL.ExifTags import TAGS

def walk_images(path, ext, outfile, topdown=True):
	fp = open(outfile, 'w')
	if not fp:
		print "walking_image: open file failed. %s" % (outfile)
		return
	print "walking dirs:", path
	for root, dirs, files in os.walk(path, topdown):
		for name in files:
			f,e=os.path.splitext(name)
			if e == ext:
				filename = os.path.join(root, name)
				print filename, extract_focal(filename)
				fp.write(os.path.join(root,name) + '\n')
	fp.close()

def get_exif(fn):
	ret = {}
	i = Image.open(fn)
	info = i._getexif()
	for tag, value in info.items():
		decoded = TAGS.get(tag, tag)
		ret[decoded] = value
	print ret
	return ret

def extract_focal(imagefile):
	rt = get_exif(imagefile)
	return rt['FocalLength']

if __name__ == "__main__":
	walk_images( "../examples/ET", ".jpg", "list2.txt" )

