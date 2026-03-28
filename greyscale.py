import cv2

image = cv2.imread("picture.jpg")

cv2.namedWindow("Picture", cv2.WINDOW_NORMAL)

grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRA34Y)

resized_image = cv2.resizeWindow("grey_image", 200, 300)

cv2.imshow("Picture", grey_image)

key = cv2.waitKey(0)

if key == ord(s):
    
    cv2.imwrite("grey_scale_resized_picture.jpg", resized_image)
    print("image saved")

else:
    
    print("Image not saved")
    
cv2.destroyAllWindows()

