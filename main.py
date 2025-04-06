import cv2
import pickle
import cvzone
import numpy as np

# Load video feed of the parking area
cap = cv2.VideoCapture('carPark.mp4')

# Load previously saved parking space positions from file
with open('CarParkPos', 'rb') as f:
    posList = pickle.load(f)

# Define width and height of a parking spot (in pixels)
width, height = 107, 48

# Function to check parking availability
def checkParkingSpace(imgPro):
    spaceCounter = 0  # Counter to keep track of free spaces

    # Iterate through all parking space positions
    for pos in posList:
        x, y = pos

        # Crop the processed image to the region of each parking space
        imgCrop = imgPro[y:y + height, x:x + width]

        # Count non-zero (white) pixels — indicates presence of vehicle
        count = cv2.countNonZero(imgCrop)

        # If pixel count is low, the spot is considered empty
        if count < 900:
            color = (0, 255, 0)  # Green for available
            spaceCounter += 1
        else:
            color = (0, 0, 255)  # Red for occupied

        # Draw rectangle around each spot on the original image
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, 2)

        # Show pixel count for each spot (debugging/analysis)
        cvzone.putTextRect(img, str(count), (x, y + height - 3), scale=1,
                           thickness=2, offset=0, colorR=color)

    # Display number of available parking spots
    cvzone.putTextRect(img, f'Free: {spaceCounter}/{len(posList)}', (100, 50), scale=3,
                       thickness=5, offset=20, colorR=(0, 200, 0))


# Infinite loop to process video frames
while True:

    # Restart video from beginning if it reaches the end
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    # Read the next frame
    success, img = cap.read()

    # Convert frame to grayscale
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)

    # Apply adaptive thresholding to detect objects
    imgThreshold = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                         cv2.THRESH_BINARY_INV, 25, 16)

    # Apply median blur to smooth image
    imgMedian = cv2.medianBlur(imgThreshold, 5)

    # Define kernel for dilation and apply it to emphasize shapes
    kernel = np.ones((3, 3), np.uint8)
    imgDilate = cv2.dilate(imgMedian, kernel, iterations=1)

    # Analyze each parking spot based on the processed image
    checkParkingSpace(imgDilate)

    # Show the final output image with parking information
    cv2.imshow("Image", img)

    # Wait for 10ms and proceed to next frame
    cv2.waitKey(10)
