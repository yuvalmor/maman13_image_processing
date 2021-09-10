import cv2


def display_images(original_image, improved_image):
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Improved Image', improved_image)
    cv2.waitKey(0)

if __name__ == '__main__':
    # Loading the image
    original_image = cv2.imread("embedded_squares.JPG", 0)
    # Create a CLAHE object without clipLimit and tile size 100x100
    clahe = cv2.createCLAHE(clipLimit=0, tileGridSize=(100, 100))
    # Applying the histogram improvement
    improved_image = clahe.apply(original_image)
    display_images(original_image, improved_image)

