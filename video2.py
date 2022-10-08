import cv2
vid=cv2.VideoCapture(0)
while True:
    ret,frame=vid.read()
    grey=cv2.cvtColor(frame,cv2.COLOR_BGR2GREY)
    cv2.imshow("black and white frame",grey)
    if cv2.waitKey(1) & 0xFF == ord('q'):
     break
vid.release()
cv2.destroyAllWindows()