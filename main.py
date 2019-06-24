import wx

class windowClass(wx.Frame):
    def __init__(self, parent, title):
        super(windowClass, self).__init__(parent, title=title, size=(1200,600), style = wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
        self.Show()

app = wx.App()
windowClass(None, title='KBMapper')

app.MainLoop()