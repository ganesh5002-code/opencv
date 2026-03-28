import cv2 

picture = cv2.imread("picture.jpg")

cv2.namedWindow("My picture", cv2.WINDOW_NORMAL)
cv2.resizeWindow("My picture", 200, 300)

cv2.imshow("My picture", picture)

cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"image dimensions: {picture.shape}")