import wx

class LEDControlFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(LEDControlFrame, self).__init__(*args, **kw)

        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)

        # Create LED status label
        self.led_status_label = wx.StaticText(panel, label='LED Status: OFF', pos=(10, 10))

        # Create LED ON button
        btn_led_on = wx.Button(panel, label='LED ON', pos=(10, 50))
        btn_led_on.Bind(wx.EVT_BUTTON, self.OnLEDOn)

        # Create LED OFF button
        btn_led_off = wx.Button(panel, label='LED OFF', pos=(120, 50))
        btn_led_off.Bind(wx.EVT_BUTTON, self.OnLEDOff)

        self.SetSize((250, 150))
        self.SetTitle('LED Control')
        self.Centre()

    def OnLEDOn(self, event):
        # Code to handle LED ON
        self.led_status_label.SetLabel('LED Status: ON')

    def OnLEDOff(self, event):
        # Code to handle LED OFF
        self.led_status_label.SetLabel('LED Status: OFF')

def main():
    app = wx.App()
    frame = LEDControlFrame(None)
    frame.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
