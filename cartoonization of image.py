
import cv2
#rmport image
img = cv2.imread("d.jpg")
img=cv2.resize(img,(600,600))
#convert into gray scale and use median blur to blur with edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 9)
edges = cv2.adaptiveThreshold(gray, 150, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 4)

#apply bilateral filter to mix the pixels
color = cv2.bilateralFilter(img, 11, 255, 255)
#draw cartoon image
cartoon = cv2.bitwise_and(color, color, mask=edges)

#show real image
cv2.imshow("Image", img)
#after applying cartoon effect
cv2.imshow("Cartoon", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()