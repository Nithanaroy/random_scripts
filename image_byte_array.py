import base64

def image_to_byte_array(image):
	with open(image, "rb") as imageFile:
		return base64.b64encode(imageFile.read())

if __name__ == '__main__':
	image = '/Volumes/350GB/Projects/DynamicTimeLapse/Software/mapnik-stylesheets/tiles/0/1/0/0.png'
	print image_to_byte_array(image)