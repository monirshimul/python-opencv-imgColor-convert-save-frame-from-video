
import cv2
import argparse
import glob

parser = argparse.ArgumentParser()
parser.add_argument("s")
parser.add_argument("d")
args = parser.parse_args()

# sourceFld = glob.glob(args.s)
sourceFld = args.s
print("Source======", sourceFld)
desFld = args.d
print("des=======", desFld)

# Opens the Video file
cap = cv2.VideoCapture(sourceFld)
print("Cap======", cap)
i = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    # cv2.imwrite('kang' + str(i) + '.jpg', frame)
    sp = 'fake'+str(i)+'.png'
    cv2.imwrite('{}/{}'.format(desFld, sp), frame)
    i += 1

cap.release()
cv2.destroyAllWindows()
