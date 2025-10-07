import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-e5e07-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "123":
        {
            "name": "Adittya Saha",
            "major": "Generative AI",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "A",
            "year": 4,
            "last_attendance_time": "2025-10-6 00:54:34"
        },
    "456":
        {
            "name": "Bittu Kumar Azad",
            "major": "Machine Learning",
            "starting_year": 2023,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2025-10-6 00:54:34"
        },
    "789":
        {
            "name": "Akshita Sharma",
            "major": "Data Science",
            "starting_year": 2024,
            "total_attendance": 7,
            "standing": "C",
            "year": 2,
            "last_attendance_time": "2025-10-6 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)