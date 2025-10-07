# Smart Attendance System

A real-time face recognition attendance system built with Python, OpenCV, and Firebase. This application uses computer vision to detect faces via webcam, matches them against a database of known students, and automatically updates attendance records in a Firebase Realtime Database.

## Features

- *Real-time Face Detection*: Captures video from webcam and detects faces in real-time.
- *Face Recognition*: Matches detected faces against pre-encoded student faces.
- *Attendance Tracking*: Automatically updates attendance count and timestamp in Firebase Database.
- *Firebase Integration*: Stores student data and images in Firebase Realtime Database and Storage.
- *Visual Feedback*: Displays attendance information on a custom background with different modes (e.g., loading, success, already marked).
- *Duplicate Prevention*: Prevents marking attendance multiple times within a 30-second window.

## Prerequisites

- Python 3.7 or higher
- Webcam (built-in or external)
- Firebase project with Realtime Database and Storage enabled
- Service account key from Firebase (provided as serviceAccountKey.json)

## Installation

1. *Clone the repository*:
   bash
   git clone https://github.com/your-username/face-attendance-system.git
   cd face-attendance-system
   

2. *Install dependencies*:
   bash
   pip install -r requirements.txt
   

3. *Set up Firebase*:
   - Create a Firebase project at [Firebase Console](https://console.firebase.google.com/).
   - Enable Realtime Database and Storage.
   - Generate a service account key and save it as serviceAccountKey.json in the project root.
   - Update the database URL and storage bucket in the code if necessary.

4. *Prepare student data*:
   - Add student images to the Images/ folder (e.g., 123.png, 456.png).
   - Run AddDataToDatabase.py to populate the Firebase Database with student information.
   - Run EncodeGenerator.py to generate face encodings and upload images to Firebase Storage.

## Usage

1. *Run the attendance system*:
   bash
   python main.py
   

2. *How it works*:
   - The application opens a window displaying the webcam feed overlaid on a background.
   - When a known face is detected, it fetches student data from Firebase and displays it.
   - Attendance is marked if more than 30 seconds have passed since the last mark.
   - Press any key to exit the application.

## Adding New Students

1. Add the student's image to the Images/ folder (name it as the student ID, e.g., 789.png).
2. Update AddDataToDatabase.py with the new student's information.
3. Run AddDataToDatabase.py to add to Firebase Database.
4. Run EncodeGenerator.py to encode the new face and upload the image.

## Project Structure


.
├── main.py                    # Main application script
├── EncodeGenerator.py         # Script to generate face encodings
├── AddDataToDatabase.py       # Script to add student data to Firebase
├── requirements.txt           # Python dependencies
├── serviceAccountKey.json     # Firebase service account key
├── EncodeFile.p               # Pickle file with face encodings
├── Images/                    # Folder for student images
│   ├── 123.png
│   ├── 456.png
│   └── 789.png
└── Resources/                 # Background and mode images
    ├── background.png
    └── Modes/
        ├── 1.png
        ├── 2.png
        ├── 3.png
        └── 4.png


## Dependencies

- OpenCV: Computer vision library
- face-recognition: Face detection and recognition
- Firebase Admin: Firebase SDK for Python
- cvzone: Computer vision utilities
- NumPy: Numerical computing

## Troubleshooting

- *Camera not found*: Ensure your webcam is connected and not in use by another application. Change cv2.VideoCapture(0) to cv2.VideoCapture(1) if using an external camera.
- *Firebase errors*: Verify your serviceAccountKey.json is correct and Firebase project is set up properly.
- *Encoding issues*: Ensure student images are clear face photos in PNG format.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

<img width="1920" height="1080" alt="Screenshot (228)" src="https://github.com/user-attachments/assets/55fa5ee7-7383-40a2-a74b-ab853b44c829" />

<img width="1920" height="1080" alt="Screenshot (229)" src="https://github.com/user-attachments/assets/cdc8e520-0c13-4156-a989-50c58e0cbee6" />