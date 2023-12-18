import image_dehazer									# Load the library
import cv2
import numpy as np
HazeImg = cv2.imread('./input.jpg')						# read input image -- (**must be a color image**)
HazeCorrectedImg = (image_dehazer.remove_haze(HazeImg))[0]		# Remove Haze
print(HazeCorrectedImg.dtype)
print(np.min(HazeCorrectedImg), np.max(HazeCorrectedImg))
cv2.imshow('input image', HazeImg);						# display the original hazy image
cv2.imshow('enhanced_image', HazeCorrectedImg);			# display the result
cv2.waitKey(0)