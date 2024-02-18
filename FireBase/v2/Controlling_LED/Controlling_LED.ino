#include <ESP8266WiFi.h>
#include <FirebaseArduino.h>

#define FIREBASE_HOST "nodemcufirebase-3f3c7-default-rtdb.firebaseio.com"
#define FIREBASE_AUTH "aZHv3rn1WrAU2jlcTqp3KalL7Nm7tQYqBSYDRlJU"

#define WIFI_SSID "DoIT"
#define WIFI_PASSWORD "123Balaji"

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Initialize Firebase
  Firebase.begin(FIREBASE_HOST, FIREBASE_AUTH);

  // Check Firebase connection status
  if (Firebase.failed()) {
    Serial.print("Firebase connection failed: ");
    Serial.println(Firebase.error());
    while (1);
  } else {
    Serial.println("Connected to Firebase");
  }
}

void loop() {
//  // Set data on Firebase
//  Firebase.setString("LED_STATUS", "OFF");
//  delay(1000);
//
//  // Read data from Firebase
//  String fireStatus = Firebase.getString("LED_STATUS");
//  Serial.println("LED Status: " + fireStatus);
//
//  delay(5000);
///////////////////////////////////////////////////////

  // Get a reference to the database
//  FirebaseData data;
  Firebase.get(data, "/LED_STATUS");

  // Check if the request was successful
  if (data.success()) {
    Serial.print("LED Status: ");
    Serial.println(data.stringData());
  } else {
    Serial.print("Failed to retrieve LED status: ");
    Serial.println(data.errorReason());
  }

  delay(5000);

}
