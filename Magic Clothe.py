import cv2
import numpy as np
cap=cv2.VideoCapture(0)										#start reading video

for i in range(60):														#saving background 
	_,background=cap.read()
	if ( _==False):														#if video not yet started to be read
		continue
	background = np.flip(background,axis=1)
	# background=cv2.resize(background,(512,512))							#resizing video's image to standard size

while(cap.isOpened()):													#if video is being read
	_,img=cap.read()
	if (_==False):														#at end of video _ is set to false and thus end automatically
		break
	img = np.flip(img,axis=1)
	# img=cv2.resize(img,(512,512))
	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)								#converting image to hsv for easier color detection and segmentation
	
	lower_red = np.array([0,120,50])
	upper_red = np.array([10,255,255])								#upper bound for color to be segmented
	mask1=cv2.inRange(hsv,lower_red,upper_red)						#mask1 returns white area for color to be removed elsewhere is black

	lower_red = np.array([170,120,70])
	upper_red = np.array([180,255,255])
	mask2 = cv2.inRange(hsv,lower_red,upper_red)

	mask1 = mask1+mask2
	
	kernel=np.ones((3,3),np.uint8)										#kernel for erosion(Erodes away the boundaries of foreground object) & dilation(Increases the object area) 
	mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,kernel,iterations=2)	#erosion then dilation
	mask1=cv2.dilate(mask1,kernel,iterations=1)							#dilation

	mask2=cv2.bitwise_not(mask1)										#black for segment color and white for rest

	res1=cv2.bitwise_and(background,background,mask=mask1)				#loads from background at color to be segmented
	res2=cv2.bitwise_and(img,img,mask=mask2)							#loads from img in background
	final=cv2.addWeighted(res1,1,res2,1,0)								#adding both res1 and res2

	cv2.imshow("frame",final)

	if (cv2.waitKey(10)==27):
		break
cap.release()
cv2.destroyAllWindows()