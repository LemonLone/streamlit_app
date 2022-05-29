import cv2

url = 'rtsp://admin:admin@192.168.1.101:8554/live'
cap = cv2.VideoCapture(url)  # 带有摄像头的笔记本用户将url替换为 0 即可

while(cap.isOpened()):
    ret, frame = cap.read()  # frame为一帧图像，当frame为空时，ret返回false，否则为true
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()  # release the capture  
cv2.destroyAllWindows()
