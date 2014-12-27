#Import neccessary modules
import numpy as np
import cv2



#Input capture from camera
def startCamera(resX, resY, vflip=False, hflip=False, camNum=0):
	#Get the video for the given camera
	camera = cv2.VideoCapture(camNum)
	#Set the resolutions
	camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, resX)
	camera.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, resY)
	return camera

#Set the video frame
def setFPS(camera, fps):
	camera.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, fps)
	return camera

#Releasing the camera once done
def releaseCamera(camera):
	camera.release()

#To start a window preview
def startPreview(camera):
	#Display video
	while(True):
		#Frame-by-frame capture
		_ , frame = camera.read()

		#Frame operations
		gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

		#Dispaly the frame\
		cv2.imshow('frame',gray)

		#To quit, press 'q'
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	#Destroy windows
	cv2.dstroyAllWindows()

#TEST window preview
def startPreviewTest(camera):
	import cv
	cv.NamedWindow('window', cv2.cv.CV_WINDOW_AUTOSIZE)
	capture = cv.CaptureFromCAM(0)
	while(True):
		frame = cv.QueryFrame(capture)
		cv.ShowImage('window',frame)
		

