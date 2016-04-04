import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('Flight130_target5.jpg')
print img.shape
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.equalizeHist(img)
img = cv2.bilateralFilter(img, 11, 17, 17)

edges = cv2.imread('Flight130_target5.jpg')
edges = cv2.cvtColor(edges,cv2.COLOR_BGR2GRAY)
edges = cv2.bilateralFilter(edges, 11, 17, 17)
#ret,edges = cv2.threshold(edges.copy(),127,255,0)
edges = cv2.Canny(edges, 30, 200)
im2, contours, hierarchy = cv2.findContours(edges.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#print cnts
#print cv2.contourArea(cnts)
#cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]
#clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
#img = clahe.apply(img)



plt.subplot(121),plt.imshow(img)
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()