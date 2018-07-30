import numpy as np
import math
import time
from matplotlib import pyplot as plt
from scipy.interpolate import griddata
import cv2
import xmltodict
import urllib.request
from array import array
# import xmltodict


while(1):
	# if active == True:
	   
		file = urllib.request.urlopen('http://192.168.5.119/xml')
		data = file.read()
		file.close()

		data = xmltodict.parse(data)
		#time.sleep(5)

		length = len(data['response'])
		# print(data['response'])
		sensor = data['response']
		# print(type(sensor))
		sensor1 = map(str.strip, sensor.split(','))
	

		Z = [0] * 64
		for x in range(0,64):
			t = list(sensor[6*x] + sensor[6*x+1] + sensor[6*x+2] + sensor[6*x+3] + sensor[6*x+4])
			t = float(''.join(t))
			Z[x] = t
		# print(len(Z))
		# print(t)
		# print(t + 5)
		# print(type(sensor1))

		# Read pixels, convert them to values between 0 and 1, map them to an 8x8 grid
		pixels = Z
		pixmax = max(pixels)
		pixels = [x / pixmax for x in pixels]
		points = [(math.floor(ix / 8), (ix % 8)) for ix in range(0, 64)]
		grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

		# bicubic interpolation of 8x8 grid to make a 32x32 grid
		bicubic = griddata(points, pixels, (grid_x, grid_y), method='cubic')
		image = np.array(bicubic)
		image = np.reshape(image, (32, 32))
		print(image)
		plt.imsave('color_img.png', image)

		# Read image
		img = cv2.imread("color_img.png", cv2.IMREAD_GRAYSCALE)
		img = cv2.bitwise_not(img)

		# Setup SimpleBlobDetector parameters.
		params = cv2.SimpleBlobDetector_Params()

		# Change thresholds
		params.minThreshold = 10
		params.maxThreshold = 255

		# Filter by Area.
		params.filterByArea = True
		params.minArea = 5

		# Filter by Circularity
		params.filterByCircularity = True
		params.minCircularity = 0.1

		# Filter by Convexity
		params.filterByConvexity = False
		params.minConvexity = 0.87

		# Filter by Inertia
		params.filterByInertia = False
		params.minInertiaRatio = 0.01

		# Set up the detector with default parameters.
		detector = cv2.SimpleBlobDetector_create(params)

		# Detect blobs.
		keypoints = detector.detect(img)
		for i in range (0, len(keypoints)):
			x = keypoints[i].pt[0]
			y = keypoints[i].pt[1]
			print(str(len(keypoints)))
	
		
	# else:
	# 	print("idle")
		# channel.send("Idle")
		# time.sleep(5)
		# interval = config.get("channel.active")
		# config.set("channel.active", active)