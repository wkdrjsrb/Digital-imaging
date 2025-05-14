import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\PC\Downloads\BSDS300-images\BSDS300\images\test\3096.jpg", cv2.IMREAD_GRAYSCALE)


sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 3)
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 3)
sobel = cv2.magnitude(sobel_x, sobel_y)

plt.subplot(1, 3, 1); plt.title('Sobel X'); plt.imshow(sobel_x, cmap = 'gray')
plt.subplot(1, 3, 2); plt.title('Sobel Y'); plt.imshow(sobel_y, cmap = 'gray')
plt.subplot(1, 3, 3); plt.title('Combined'); plt.imshow(sobel, cmap = 'gray')
plt.tight_layout(); plt.show()