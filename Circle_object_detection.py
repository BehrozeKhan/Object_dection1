import numpy as nm
import cv2

print("Object Detection by Circle")
color = (0,0,0)
line_width = 4
radius = 50
#height = 10
#width = 20
point = (50,50)

cap = cv2.VideoCapture(0)

def click(event, x, y, flags, param):
	global pressed, point

	if event == cv2.EVENT_RBUTTONDOWN:
		print("Pressed", x, y)
		point = (x,y)


cv2.namedWindow("PointOut")
cv2.setMouseCallback("PointOut",click)

while(True):
	retina,frame = cap.read()
	frame = cv2.resize(frame,(0,0), fx = 0.75, fy = 0.75)
	cv2.circle(frame,point,radius,color,line_width)
	cv2.imshow("PointOut", frame)
	ch = cv2.waitKey(1)
	if ch == ord('b'):
		break
cap.release()
cv2.destroyAllWindows()
