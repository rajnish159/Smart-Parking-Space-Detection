import cv2
import pickle

# Load a static image (snapshot of parking lot) to mark parking spaces
img = cv2.imread('carParkImg.png')

# Define the width and height of each parking space (in pixels)
width, height = 107, 48

# Try loading existing parking space positions from a pickle file
try:
    with open('carParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []  # If file not found or error, start with an empty list

# Mouse click event function to add or remove parking spaces
def mouseClick(events, x, y, flags, params):
    # Left-click to add a new parking space position
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))

    # Right-click to remove a parking space if the click falls within its boundary
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            # Check if clicked point is inside the rectangle
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    # Save updated positions to pickle file
    with open('carParkPos.pkl', 'wb') as f:
        pickle.dump(posList, f)

# Infinite loop to display image and capture mouse events
while True:
    # Reload the base image every frame to avoid drawing over previous rectangles
    img = cv2.imread('carParkImg.png')

    # Draw rectangles for each saved parking position
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 2)

    # Show image window
    cv2.imshow("Image", img)

    # Set mouse callback for adding/removing parking spaces
    cv2.setMouseCallback("Image", mouseClick)

    # Refresh image every 1ms
    cv2.waitKey(1)
