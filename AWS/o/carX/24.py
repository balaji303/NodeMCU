import wx

class LEDControlFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(LEDControlFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        # Create a wx.Locale object to set the locale
        loc = wx.Locale(wx.LANGUAGE_ENGLISH)

        # Load LED images
        self.led_on_image = wx.Image("E:\\GitHub\\NodeMCU\\AWS\\o\\carX\\LED_ON.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.led_off_image = wx.Image("E:\\GitHub\\NodeMCU\\AWS\\o\\carX\\LED_OFF.png", wx.BITMAP_TYPE_PNG).ConvertToBitmap()

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

    def OnLEDOff(self, event):
        # Code to handle LED OFF
        self.led_status_bitmap.SetBitmap(self.led_off_image)

def main():
    app = wx.App()
    frame = LEDControlFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
