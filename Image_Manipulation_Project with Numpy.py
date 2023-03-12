import numpy as np

#importing two different packages- io gives us ability to read images
from skimage import io

import matplotlib.pyplot as plt #matplotlib enables us to show the images after modifications

#importing the image we shall be manipulating

camaro = io.imread("camaro.jpg") #numpy imports and reads the image as an array and displays the size
print(camaro)

camaro.shape #running this gives us the size of the image in an array format
#the size here is 1200 rows of pixels, 1600 columns of pixels and 3d arrays of color channels

#taking a look at the object, we can use matplotlib and we can see it in the plots section

plt.imshow(camaro) #calls to show the image
plt.show()

#Manipulating the image

#Cropping the image using slicing an array
"""we want to make sure we are slicing using the rows and columns 
and not the color channels."""

''' if we are cropping from one axis, you still need to refer to the other axes
to still display the rest of the image and we use : to indicate that. 
in the code below, we are cropping by the rows(y-axis)'''

cropped_1 = camaro[0:500, :, :] 
plt.imshow(cropped_1) 
plt.show()
#this crops the x-axis, and that is what we want.

''' Cropping by the columns axis (x-axis), we shall use the code below'''

cropped_2 = camaro[:, 400:1000, :] 
plt.imshow(cropped_2) 
plt.show()

#Cropping out just the vehicle: we shall need to know the exact dimensions where we want to crop
cropped_3 = camaro[350:1100, 200:1400, :] 
plt.imshow(cropped_3) 
plt.show()

#Saving the cropped image to the disk, we can use the ion package to save it and have it in the file

io.imsave("camaro_cropped_image.jpg", cropped_3)

#Flipping the image
''' We can flip the image either horizontally or vertically'''

vertical_flip = camaro[::-1, :, :] #reverse the rows, and keep the columns and color channels untouched
#the -1 reverses the rows and flips the image
plt.imshow(vertical_flip) 
plt.show()

#saving the flipped image
io.imsave("camaro_vertical_flip.jpg", vertical_flip)

#Horizontal flip

horizontal_flip = camaro[:,::-1, :] #reverse the columns, and keep the rows and color channels untouched
#the -1 reverses the columns and flips the image
plt.imshow(horizontal_flip) 
plt.show()

io.imsave("camaro_horizontal_flip.jpg", horizontal_flip)

#Color channels: we can play around changing the colors of the image.
""" we can zero  out the other color channels and fill out the only color we need
we start by creating an array of zeros"""

red = np.zeros(camaro.shape, dtype = 'uint8')
#we use datatype as uint8 because it is what numpy uses to read the color
'''we need to input values just for the red channel, both rows and columns 
and leave the other 2 channels as the zeros of the array '''
red[:,:,0] = camaro[:,:,0]
plt.imshow(red) 
plt.show()

green = np.zeros(camaro.shape, dtype = 'uint8')
#we use datatype as uint8 because it is what numpy uses to read the color
'''we need to input values just for the red channel, both rows and columns 
and leave the other 2 channels as the zeros of the array '''
green[:,:,1] = camaro[:,:,1]
plt.imshow(green) 
plt.show()

blue = np.zeros(camaro.shape, dtype = 'uint8')
#we use datatype as uint8 because it is what numpy uses to read the color
'''we need to input values just for the red channel, both rows and columns 
and leave the other 2 channels as the zeros of the array '''
blue[:,:,2] = camaro[:,:,2]
plt.imshow(blue) 
plt.show()

#Stacking the images together

#Vertical stack

camaro_rainbow = np.vstack((red, green, blue))
plt.imshow(camaro_rainbow) 
plt.show()

io.imsave("camaro_rainbow.jpg", camaro_rainbow)


