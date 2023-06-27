import cv2
from filter import ascii_filter
vid = cv2.VideoCapture(0)

vid.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, 400)


while(True):
    ret, frame = vid.read()

    frame = ascii_filter(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
vid.release()
cv2.destroyAllWindows()
