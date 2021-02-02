import numpy as numpy
import cv2


face_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('data/cascades/haarcascade_eye.xml')
nose_cascade = cv2.CascadeClassifier('data/cascades/Nariz.xml')
cap = cv2.VideoCapture('video.mp4')
b = 0
def writee(a,b):
		img_item = 'data/models/' + str(a) +'___'+ str(b) +'.jpg'
		cv2.imwrite(img_item, roi_color)

while(True):
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 2, 2)
	a = 0
	for (x, y, w, h) in faces:
		roi_color = frame[y:y+h,x:x+w]
		writee(a,b)
		a = a + 1
		roi_gray = gray[y:y+h,x:x+w]#[cord1-height,cord2-height]
		color = (0,250,0)
		stroke = 2
		width = x + w
		height = y + h
		cv2.rectangle(frame,(x,y),(width,height),color, stroke)
		eyes = eye_cascade.detectMultiScale(gray, 3, 3)
		noses = nose_cascade.detectMultiScale(gray,2.5, 6)
		for ex, ey, ew, eh in eyes:
			if ey > y + h/2:
				continue
			eye_gray = gray[ey:ey+eh,ex:ex+ew]
			eye_color = frame[ey:ey+eh,ex:ex+ew]
			ewidth = ex + ew
			eheight = ey + eh
			cv2.rectangle(frame,(ex,ey),(ewidth,eheight),color,stroke)
		for nx, ny, nw, nh in noses:
			nose_gray = gray[ny:ny+nh,nx:nx+nw]
			nose_color = frame[ny:ny+nh,nx:nx+nw]
			nwidth = nx + nw
			nheight = ny + nh
			cv2.rectangle(frame,(nx,ny),(nwidth,nheight),color,stroke)
	cv2.imshow('frame',frame)
	b = b + 1
	if cv2.waitKey(20) & 0xFF==ord('q'):
		break

cap.release()
cv2.destroyAllWindows()