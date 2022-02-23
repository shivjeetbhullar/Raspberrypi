import cv2 as cv
import numpy as np

cv_p = "/home/pi/.local/lib/python3.5/site-packages/cv2/data"

face_c = cv.CascadeClassifier(cv_p+"/haarcascade_frontalface_default.xml")

def face_ex(img):
	gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
	faces = face_c.detectMultiScale(gray,1.3,5)

	if faces is ():return None

	for (x,y,w,h) in faces:
	   cropped_face = img[y:y+h,x:x+w]
	return cropped_face


cap = cv.VideoCapture(0)

count = 0

while True:
	ret,frame = cap.read()
	if face_ex(frame) is not None:
		count+=1
		face = cv.resize(face_ex(frame),(200,200))
		face = cv.cvtColor(face,cv.COLOR_BGR2GRAY)

		f_path = './faces/'+str(count)+'.jpg'
		cv.imwrite(f_path,face)

		cv.putText(face,str(count),(50,50),cv.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

		cv.imshow('Face Crop',face)

	else:
		print('Face Not Found')
	if cv.waitKey(1)==13 or count == 200:break

cap.release()
cv.destroyAllWindows()
print('Done')


