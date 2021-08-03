import cv2
from pprint import pprint
import array as arr
import numpy as np
import argparse
from imutils.object_detection import non_max_suppression
import pyautogui
import time
from ctypes import *
import autoit

def clickImage(imagePath):
	time.sleep(3)
	imagePath = cv2.imread(imagePath)
	# smaillGray = cv2.cvtColor(imagePath, cv2.COLOR_BGR2GRAY)
	imageLevel = pyautogui.screenshot()
	imageLevel = cv2.cvtColor(np.array(imageLevel), cv2.COLOR_RGB2BGR)
	#imageGray = cv2.cvtColor(imageLevel, cv2.COLOR_BGR2GRAY)
	#result = cv2.matchTemplate(smaillGray, imageGray, cv2.TM_SQDIFF_NORMED)
	result = cv2.matchTemplate(imagePath, imageLevel, cv2.TM_SQDIFF_NORMED)
	mn,_,mnLoc,_ = cv2.minMaxLoc(result)
	pprint((mn,_,mnLoc));
	MPx,MPy = mnLoc
	trows,tcols = imagePath.shape[:2]
	if mn < 0.2:
		pyautogui.click(MPx+int(tcols/2), MPy+int(trows/2))
		return True
	return False

def level():
	pprint('level');
	clickImage('close.png')
	if clickImage('continue.png') == True:
		if clickImage('close.png') == True:
			clickImage('yes.png')
	clickImage('close.png')
	clickImage('close.png')

def main():
	time.sleep(3)
	# print("[INFO] loading images...")
	# # image = cv2.imread('game.png')
	template = cv2.imread('game2.png')
	templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
	(tH, tW) = template.shape[:2]
	miss = 0
	while True:
		miss = miss + 1;
		ok = windll.user32.BlockInput(True)
		autoit.win_activate("City Island 5")
		# pyautogui.keyDown('alt')  # hold down the shift key
		# pyautogui.keyDown('tab')
		# pyautogui.keyUp('alt')
		# pyautogui.keyUp('tab')
		# # convert both the image and template to grayscale
		image = pyautogui.screenshot()
		image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
		imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# # perform template matching
		# print((tH, tW))
		result = cv2.matchTemplate(imageGray, templateGray,
			cv2.TM_CCOEFF_NORMED)
		rects = []

		(yCoords, xCoords) = np.where(result >= 0.8)
		# loop over the starting (x, y)-coordinates again
		for (x, y) in zip(xCoords, yCoords):
			# update our list of rectangles
			rects.append((x, y, x + tW, y + tH))
		pick = non_max_suppression(np.array(rects))
		clone = image.copy()

		# loop over our starting (x, y)-coordinates
		for (startX, startY, endX, endY) in pick:
			miss = 0;
			# print((startX, startY))
			# draw the bounding box on the image
			# cv2.rectangle(clone, (startX, startY), (endX, endY),
			# 	(255, 0, 0), 3)
			# pyautogui.moveTo(x + 10, y + 10, 2)
			pyautogui.click(startX + 10, startY + 10)
			# time.sleep(0.1)
		if miss > 4:
			level()

		pyautogui.keyDown('alt')  # hold down the shift key
		pyautogui.keyDown('tab')
		pyautogui.keyUp('alt')
		pyautogui.keyUp('tab')
		ok = windll.user32.BlockInput(False)
		time.sleep(60)


main()






# show our output image *before* applying non-maxima suppression
# cv2.imshow("Before NMS", clone)
# cv2.waitKey(0)




# method = cv2.TM_SQDIFF_NORMED
# # method = cv2.TM_CCOEFF_NORMED

# # Read the images from the file
# # small_image = cv2.imread('image_small.jpg')
# # large_image = cv2.imread('image.jpg')

# small_image = cv2.imread('game2.png')
# large_image = cv2.imread('game.png')

# result = cv2.matchTemplate(small_image, large_image, method)
# # print(type(cv2.minMaxLoc(result)))
# # a=arr.array('asd',[1.2,1.3,2.3])
# # print(a[0])
# # print vars(cv2.minMaxLoc(result)), vars(cv2.minMaxLoc(result))
# # We want the minimum squared difference
# mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# # Draw the rectangle:
# # Extract the coordinates of our best match
# MPx,MPy = mnLoc

# # Step 2: Get the size of the template. This is the same size as the match.
# trows,tcols = small_image.shape[:2]

# # Step 3: Draw the rectangle on large_image
# cv2.rectangle(large_image, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

# # Display the original image with the rectangle around the match.
# cv2.imshow('output', large_image)

# # The image is only displayed if we call this
# cv2.waitKey(0)
