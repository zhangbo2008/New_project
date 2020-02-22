import cv2
import matplotlib.pyplot as plt
import numpy

im = cv2.imread('tmp.jpg')


cv2.rectangle(im, (1, 1), (18,78), (1,1,1), 5)
plt.imshow(im)
plt.axis('off')
plt.show()