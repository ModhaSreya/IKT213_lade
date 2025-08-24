import cv2

def print_image_information(image):
    img = cv2.imread(image)

    if img is None:
        print("Could not load image.")
        return

    height, width, channels = img.shape
    print("Height:", height)
    print("Width:", width)
    print("Channels:", channels)
    print("Size (number of values):", img.size)
    print("Data type:", img.dtype)

print_image_information(r"C:\Users\MODHASREYA\Downloads\lena-1.png"
                        )
