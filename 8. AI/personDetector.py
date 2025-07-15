# pip install opencv-python
# pip3 install imutils
import cv2 #is the OpenCV library, which is used for computer vision tasks.
import imutils # is the OpenCV library, which is used for computer vision tasks.
 
# Initializing the HOG person
# detector
hog = cv2.HOGDescriptor() # Initializes a Histogram of Oriented Gradients (HOG) descriptor. HOG is a feature descriptor used in computer vision and image processing for object detection.
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector()) #Sets the SVM (Support Vector Machine) detector with a pre-trained people detector. 

# Reading the Image
image = cv2.imread('running.jpg')

# Resizing the Image
image = imutils.resize(image,
					width=min(400, image.shape[1]))

# Detecting all the regions in the 
# Image that has a pedestrians inside it
(regions, _) = hog.detectMultiScale(image, winStride=(4, 4),padding=(4, 4),scale=1.05)
# winStride: Window stride, the step size in both x and y directions.
# padding: Padding around the detection window.
# scale: Scale factor for the image pyramid.

# Drawing the regions in the Image
for (x, y, w, h) in regions:
	cv2.rectangle(image, (x, y), 
				(x + w, y + h), 
				(0, 0, 255), 2)
#top-left corner at (x, y) and bottom-right corner at (x + w, y + h), with a red color (0, 0, 255)

# Showing the output Image
cv2.imshow("Image", image)
cv2.waitKey(0)

cv2.destroyAllWindows()