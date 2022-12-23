import cv2 as cv

path="/home/galactus/Code/Projects Py/PRO-104/Planet_Name/solar-system.jpg"

image=cv.imread(path)

#Names
cv.putText(image,'The',(5,208),fontFace=cv.CALIB_CB_MARKER,fontScale=1,color=(255,255,255))
cv.putText(image,'Sun',(5,250),fontFace=cv.CALIB_CB_MARKER,fontScale=1,color=(255,255,255))

cv.putText(image,'Mercury',(115,218),fontFace=cv.CALIB_CB_MARKER,fontScale=0.5,color=(255,255,255))

cv.putText(image,'Venus',(188,220),fontFace=cv.CALIB_CB_MARKER,fontScale=0.7,color=(255,255,255))

cv.putText(image,'Earth',(295,218),fontFace=cv.CALIB_CB_MARKER,fontScale=0.7,color=(0,255,255))

cv.putText(image,'Mars',(385,218),fontFace=cv.CALIB_CB_MARKER,fontScale=0.5,color=(255,255,255))

cv.putText(image,'Jupiter',(508,218),fontFace=cv.CALIB_CB_MARKER,fontScale=1.2,color=(0,0,255))

cv.putText(image,'Saturn',(758,218),fontFace=cv.CALIB_CB_MARKER,fontScale=1,color=(0,0,0))

cv.putText(image,'Uranus',(950,215),fontFace=cv.CALIB_CB_MARKER,fontScale=0.7,color=(0,0,0))

cv.putText(image,'Neptune',(1102,215),fontFace=cv.CALIB_CB_MARKER,fontScale=0.7,color=(0,0,0))

#Saving
cv.imwrite("SolarSystemWithNames.png",image)

cv.imshow("Solar System", image)
cv.waitKey(0)