import cv2
import matplotlib.pyplot as plt

image_path = (r"C:\Users\PC\Downloads\BSDS300-images\BSDS300\images\test\3096.jpg")

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(img, threshold1=100, threshold2=200)

plt.figure(figsize = (10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(img, cmap = 'gray')

plt.subplot(1, 2, 2)
plt.title('Canny Edge')
plt.imshow(edges, cmap = 'gray')