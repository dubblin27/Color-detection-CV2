# HSV - Hue, Saturatrion, Value 
import cv2 
import numpy as np 
def nothing(x):
    pass
cv2.namedWindow("Tracking")
cv2.createTrackbar("LH","Tracking", 0, 255, nothing)
cv2.createTrackbar("LS","Tracking", 0, 255, nothing)
cv2.createTrackbar("LV","Tracking", 0, 255, nothing)
cv2.createTrackbar("UH","Tracking", 255, 255, nothing)
cv2.createTrackbar("US","Tracking", 255, 255, nothing)
cv2.createTrackbar("UV","Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread('opencv\marbles.jpg',1)
    # to convert img to HSV format 
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h = cv2.getTrackbarPos("LH","Tracking")
    l_s = cv2.getTrackbarPos("LS","Tracking")
    l_v = cv2.getTrackbarPos("LV","Tracking")

    u_h = cv2.getTrackbarPos("UH","Tracking")
    u_s = cv2.getTrackbarPos("US","Tracking")
    u_v = cv2.getTrackbarPos("UV","Tracking")

    # to threshold the hsv to blue color 
    l_b = np.array([l_h,l_s,l_v])
    u_b = np.array([u_h,u_s,u_v])
    # l_r = np.array([0,100,100])
    # u_r = np.array([20,255,255])

    mask = cv2.inRange(hsv, l_b, u_b)
    # mask1 = cv2.inRange(hsv, l_r, u_r)
    # to mask the original image
    res = cv2.bitwise_and(frame,frame,mask=mask)
    # res1 = cv2.bitwise_and(frame,frame,mask=mask1)
    

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    # cv2.imshow('res1',res1)
    key = cv2.waitKey(1)
    if key == 27:
        break
cv2.destroyAllWindows()