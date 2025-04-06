# Smart-Parking-Space-Detection
A real-time computer vision project using OpenCV and Python to automatically detect available parking spaces from a video feed. This system is based on image thresholding and position-based pixel analysis to count and visualize free/occupied parking slots.

📁 **Project Structure**

├── main.py                  # Main script for detecting and displaying parking space availability

├── ParkingSpacePacker.py   # Tool to mark parking spot positions manually

├── carPark.mp4             # Input video feed of the parking lot

├── carParkImg.png          # Snapshot used for manually tagging parking positions

├── carParkPos.pkl          # Saved positions of parking spots (generated using the packer)

📸 **Demo**


https://github.com/user-attachments/assets/7e682182-6f48-4621-8a5e-03778aaf31af

**Features**

├── Detects and highlights occupied and vacant parking slots in real-time.

├── Adjustable parking slot size (width, height) for different video sources.

├── Easy-to-use GUI for manually marking/removing parking slots.

├── Displays live count of free/total parking spaces.

🛠️ **How It Works**

1. Mark Parking Spots: Use ParkingSpacePacker.py to manually draw parking rectangles on a sample image (carParkImg.png). The positions are saved in a carParkPos.pkl file.

2. Detect Parking Availability: main.py processes each frame from carPark.mp4, performs grayscale conversion, blurring, adaptive thresholding, and dilation. It then checks each marked area to determine if it's occupied based on the number of white pixels (non-zero).


✅ **Requirements**

> Python 3.x

> OpenCV

> Numpy

> cvzone

**$pip install opencv-python numpy cvzone**


**🧪 How to Run:**

**1. Mark Parking Spaces**

**python ParkingSpacePacker.py**

> Left-click to add a parking spot.

> Right-click to remove a spot.

> This creates/updates carParkPos.pkl.

**2. Run Detection**

**python main.py**

Watch the video feed with live parking status indicators:

> Green: Available

> Red: Occupied

> White number in each slot shows white pixel count for that region.

**⚙️ Configuration**

Modify these values inside main.py and ParkingSpacePacker.py to fit your dataset:

**width, height = 107, 48  # Dimensions of parking slots**







