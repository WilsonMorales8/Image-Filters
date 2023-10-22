import copy

'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is an inverted version of the input image. That is to say each 
    pixel's grayscale value should be inverted relative to the maximum value of 255.
'''
def invert(image):
	l = []
	for i in range(len(image)):
		k = []
		for i2 in range(len(image[i])):
			y = 255 - image[i][i2]
			k.append(y)
		l.append(k)
	return l
'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a blurred version of the input image. The blur function 
    uses a weighted kernel which is applied the pixels centered on 
    image[i][j]. The value in the kernel is multiplied by the corresponding
    pixels in the image and the eighted average is used as new_image[i][j].
'''
def blur(image):
	kernel = [
        [1, 1, 1],
        [1, 7, 1],
        [1, 1, 1],
    ]
	x = []
	k = [] 
	t = 0
	for i in range(len(kernel)):
		for i2 in kernel[i]:
			t += i2
	for i in range(len(image)):
		x = []
		for i2 in range(len(image[i])):
				if i == 0 or i2 == 0 or i == len(image) - 1 or i2 == len(image[i]) - 1:
					y = 0 
				else:
					y = (image[i][i2] * kernel[1][1]) + (image[i - 1][i2 - 1] * kernel[0][0]) +(image[i - 1][i2] * kernel[0][1]) + (image[i - 1][i2 + 1] * kernel[0][2]) + (image[i][i2 - 1] * kernel[1][0]) + (image[i][i2 + 1] * kernel[1][2]) + (image[i + 1][i2 - 1] * kernel[2][0]) + (image[i + 1][i2] * kernel[2][1]) + (image[i + 1][i2 + 1] * kernel[2][2])
				l = y / t
				x.append(l)
		k.append(x)
	return k
'''
    This function takes as input a grayscale image (2D list of ints).

    This function will take in an image and will return a NEW image
    which is a vertically flipped version of the input image. 
'''
def flip(image):
  x = []
  for i in range(1, len(image) + 1):
    y = image[-i]
    x.append(y)
  return x
'''
