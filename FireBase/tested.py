import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase with your credentials and database URL
cred = credentials.Certificate("E:\\GitHub\\nodemcufirebase.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://nodemcufirebase-3f3c7-default-rtdb.firebaseio.com'})

# Get a reference to the database
ref = db.reference()

# Set LED status to "OFF"
ref.child('LED_STATUS').set('OFF')

# Retrieve LED status
fire_status = ref.child('LED_STATUS').get()

print(f"LED Status: {fire_status}")

# Set LED status to "OFF"
ref.child('LED_STATUS').set('ON')

# Retrieve LED status
fire_status = ref.child('LED_STATUS').get()

print(f"LED Status: {fire_status}")