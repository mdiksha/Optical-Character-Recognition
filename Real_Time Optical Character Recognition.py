import cv2
from PIL import Image
import pytesseract as pt

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def recText(filename):
    text = pt.image_to_string(Image.open(filename))
    return text

cam = cv2.VideoCapture(0)

while True:
    _,img = cam.read()
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    text = "Normal"

    cv2.imshow("CameraCapture",img)
    cv2.imwrite('test.png',img)
    key = cv2.waitKey(1)
    if key == 27:
        info = recText('test.png')
        print("Image to text:\n",info)
        break

cam.release()
cv2.destroyAllWindows()

file = open("assignmentresult.txt","a")
file.write(info)
file.close()
print("Written Successful")
