import tkinter as tk
from PIL import Image, ImageTk
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import json
import os
# led command = 0
# Subscribe to this topic subTopic
# Publish to this topic balajiO 
import AWSIoTPythonSDK
# Import the AWS IoT Device SDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient

# Import json for parson endpoint.json file
import json

# Import os for finding name of current directory
import os
endpoint = "E:\\GitHub\\Learn-AWS-IoT\\IoTonAWS2\\environment\\endpoint.json"
# Load the endpoint from file
with open(endpoint) as json_file:  
    data = json.load(json_file)

# Fetch the deviceName from the current folder name
windowsPath = os.path.dirname(os.path.abspath(__file__))
deviceName = os.path.split(windowsPath)[1]
print(deviceName)
# deviceName = os.path.split(os.getcwd())[1]
print('deviceName:'+deviceName )
# Set the destinationDeviceName depending on this deviceName
if deviceName == 'carO':
    destinationDeviceName = 'carX'
    print('deviceName:'+deviceName+' destinationDeviceName:'+destinationDeviceName)
else:
    destinationDeviceName = 'carO'

# Build useful variable for code
subTopic = '@Balaji303/' + deviceName
pubTopic = 'balajiO'
keyPath = "E:\\GitHub\\NodeMCU\\AWS\\x\\28\\private.pem.key"
certPath = "E:\\GitHub\\NodeMCU\\AWS\\x\\28\\certificate.pem.crt"
caPath = 'E:\\GitHub\\Learn-AWS-IoT\\IoTonAWS2\\environment\\root-CA.crt'
clientId = deviceName
host = data['endpointAddress']
port = 8883

# 1: The AWSIoTMQTTClient library to create your AWSIoTMQTTClient 
#         client using the useful variable above and connect it to AWS IoT
# Creating instance of the call 
balajiAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
# Configuring the endpoint with port
balajiAWSIoTMQTTClient.configureEndpoint(host,port)
# Configuring the credentials
balajiAWSIoTMQTTClient.configureCredentials(caPath,keyPath,certPath)
#Now connect the device
balajiAWSIoTMQTTClient.connect()

# 2: A function that will be called when a new message is received 
#         and output its content in the console.
def callBackFunction(client, userdata, message):
     print("----- START of Payload -----")
     print("Received a new message: ")
     print(message.payload.decode())
     print("This message is from the topic:")
     print(message.topic)
     print("----- END of Payload -----\n\n")


# 3: Subscribe to the subTopic IoT Topic and use the function created in
balajiAWSIoTMQTTClient.subscribe(subTopic,1,callBackFunction)


# Function to publish payload to IoT topic
def publishToIoTTopic(topic, payload):
    balajiAWSIoTMQTTClient.publish(topic, payload,1)    
    

# Infinite loop reading console input and publishing what it finds
# while True:
#     message = input('Enter a message on the next line to send to ' + pubTopic + ':\r\n')
    
#     # Calling function to publish to IoT Topic
#     publishToIoTTopic(pubTopic, message)

class AWSIoTGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("AWS IoT GUI")

        # Load LED images
        self.led_off_image = ImageTk.PhotoImage(Image.open("E:\\GitHub\\NodeMCU\\AWS\\o\\carX\\Gen_LED_Array_Off.png"))
        self.led_on_image = ImageTk.PhotoImage(Image.open("E:\\GitHub\\NodeMCU\\AWS\\o\\carX\\Gen_LED_Array_On.png"))

        # Create LED label
        self.led_label = tk.Label(master, image=self.led_off_image)
        self.led_label.pack()

        # Set initial LED state
        self.set_led_state(0)

        # Other GUI elements can be added here...

        # AWS IoT setup
        self.setup_aws_iot()

    def setup_aws_iot(self):
        # Your existing AWS IoT setup code goes here...

        # Modify the callback function to update the LED state
        def callback_function(client, userdata, message):
            payload = message.payload.decode()
            print("Received a new message:", payload)

            if payload == "led command = 1":
                self.set_led_state(1)
            elif payload == "led command = 0":
                self.set_led_state(0)

            print("This message is from the topic:", message.topic)

        # Modify the subscribe function to use the updated callback
        balajiAWSIoTMQTTClient.subscribe(subTopic, 1, callback_function)

    def set_led_state(self, state):
        if state == 0:
            self.led_label.configure(image=self.led_off_image)
        elif state == 1:
            self.led_label.configure(image=self.led_on_image)

def main():
    root = tk.Tk()
    aws_iot_gui = AWSIoTGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
