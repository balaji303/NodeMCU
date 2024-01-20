# led command = 0
# Subscribe to this topic subTopic
# Publish to this topic balajiO 

import wx
import AWSIoTPythonSDK
# Import the AWS IoT Device SDK
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
# Import json for parson endpoint.json file
import json
deviceName = 'carX'
subTopic = '@Balaji303/' + deviceName
pubTopic = 'balajiO'
keyPath = "E:\\GitHub\\NodeMCU\\AWS\\x\\28\\private.pem.key"
certPath = "E:\\GitHub\\NodeMCU\\AWS\\x\\28\\certificate.pem.crt"
caPath = 'E:\\GitHub\\Learn-AWS-IoT\\IoTonAWS2\\environment\\root-CA.crt'
clientId = deviceName
port = 8883
endpoint = "E:\\GitHub\\Learn-AWS-IoT\\IoTonAWS2\\environment\\endpoint.json"

# Load the endpoint from file
with open(endpoint) as json_file:  
    data = json.load(json_file)
host = data['endpointAddress']


class LEDControlFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(LEDControlFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        # Create a wx.Locale object to set the locale
        loc = wx.Locale(wx.LANGUAGE_ENGLISH)

        # Load LED images
        self.led_on_image = wx.Image("E:\\GitHub\\NodeMCU\\AWS\\GPIO_Console\\LED_ON.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.led_off_image = wx.Image("E:\\GitHub\\NodeMCU\\AWS\\GPIO_Console\\LED_OFF.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

        # Create LED status bitmap
        self.led_status_bitmap = wx.StaticBitmap(panel, -1, self.led_off_image, pos=(60, 10))

        # Create LED ON button
        btn_led_on = wx.Button(panel, label='LED ON', pos=(40, 130))
        btn_led_on.Bind(wx.EVT_BUTTON, self.OnLEDOn)

        # Create LED OFF button
        btn_led_off = wx.Button(panel, label='LED OFF', pos=(120, 130))
        btn_led_off.Bind(wx.EVT_BUTTON, self.OnLEDOff)

        self.SetSize((250, 200))
        self.SetTitle('LED Control')
        self.Centre()

    def OnLEDOn(self, event):
        # Code to handle LED ON
        self.led_status_bitmap.SetBitmap(self.led_on_image)
        message = "led command = 1"
        # Calling function to publish to IoT Topic
        publishToIoTTopic(pubTopic, message)

    def OnLEDOff(self, event):
        # Code to handle LED OFF
        self.led_status_bitmap.SetBitmap(self.led_off_image)
        message = "led command = 0"
        # Calling function to publish to IoT Topic
        publishToIoTTopic(pubTopic, message)


# Function to publish payload to IoT topic
def publishToIoTTopic(topic, payload):
    balajiAWSIoTMQTTClient.publish(topic, payload,1)    


def main():
    app = wx.App()
    frame = LEDControlFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    balajiAWSIoTMQTTClient = AWSIoTMQTTClient(clientId)
    # Configuring the endpoint with port
    balajiAWSIoTMQTTClient.configureEndpoint(host,port)
    # Configuring the credentials
    balajiAWSIoTMQTTClient.configureCredentials(caPath,keyPath,certPath)
    #Now connect the device
    balajiAWSIoTMQTTClient.connect()
    main()
