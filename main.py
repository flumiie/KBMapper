import wx

class windowClass(wx.Frame):
    def __init__(self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)
        self.basicGUI()
    
    def basicGUI(self):
        menuBar = wx.MenuBar()
        fileButton = wx.Menu()
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit', 'Exit this program')

        menuBar.Append(fileButton, 'Import')
        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        # nameBox = wx.TextEntryDialog(None, 'Your name?', 'Name', 'name')
        # if nameBox.ShowModal() == wx.ID_OK:
        #     userName = nameBox.GetValue()
        
        self.KeyButtons()

        self.SetTitle('KBMapper')
        self.SetSize(850,600)
        # self.Style(wx.MINIMIZE_BOX | wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
        self.Centre()
        self.Show(True)

    def KeyButtons(self):
        panel = wx.Panel(self)
        wx.Button(panel, pos=(10,10), size=(50,50), label='ESC')
        wx.Button(panel, pos=(65,10), size=(50,50), label='1')
        wx.Button(panel, pos=(120,10), size=(50,50), label='2')
        wx.Button(panel, pos=(175,10), size=(50,50), label='3')
        wx.Button(panel, pos=(230,10), size=(50,50), label='4')
        wx.Button(panel, pos=(285,10), size=(50,50), label='5')
        wx.Button(panel, pos=(340,10), size=(50,50), label='6')
        wx.Button(panel, pos=(395,10), size=(50,50), label='7')
        wx.Button(panel, pos=(450,10), size=(50,50), label='8')
        wx.Button(panel, pos=(505,10), size=(50,50), label='9')
        wx.Button(panel, pos=(560,10), size=(50,50), label='0')
        wx.Button(panel, pos=(615,10), size=(50,50), label='-')
        wx.Button(panel, pos=(670,10), size=(50,50), label='=')
        wx.Button(panel, pos=(725,10), size=(100,50), label='Backspace')

        wx.Button(panel, pos=(10,65), size=(75,50), label='Tab')
        wx.Button(panel, pos=(90,65), size=(50,50), label='Q')
        wx.Button(panel, pos=(145,65), size=(50,50), label='W')
        wx.Button(panel, pos=(200,65), size=(50,50), label='E')
        wx.Button(panel, pos=(255,65), size=(50,50), label='R')
        wx.Button(panel, pos=(310,65), size=(50,50), label='T')
        wx.Button(panel, pos=(365,65), size=(50,50), label='Y')
        wx.Button(panel, pos=(420,65), size=(50,50), label='U')
        wx.Button(panel, pos=(475,65), size=(50,50), label='I')
        wx.Button(panel, pos=(530,65), size=(50,50), label='O')
        wx.Button(panel, pos=(585,65), size=(50,50), label='P')
        wx.Button(panel, pos=(640,65), size=(50,50), label='[')
        wx.Button(panel, pos=(695,65), size=(50,50), label=']')
        wx.Button(panel, pos=(750,65), size=(75,50), label='\\')

        wx.Button(panel, pos=(10,120), size=(90,50), label='Caps Lock')
        wx.Button(panel, pos=(105,120), size=(50,50), label='A')
        wx.Button(panel, pos=(160,120), size=(50,50), label='S')
        wx.Button(panel, pos=(215,120), size=(50,50), label='D')
        wx.Button(panel, pos=(270,120), size=(50,50), label='F')
        wx.Button(panel, pos=(325,120), size=(50,50), label='G')
        wx.Button(panel, pos=(380,120), size=(50,50), label='H')
        wx.Button(panel, pos=(435,120), size=(50,50), label='J')
        wx.Button(panel, pos=(490,120), size=(50,50), label='K')
        wx.Button(panel, pos=(545,120), size=(50,50), label='L')
        wx.Button(panel, pos=(600,120), size=(50,50), label=';')
        wx.Button(panel, pos=(655,120), size=(50,50), label='\'')
        wx.Button(panel, pos=(710,120), size=(115,50), label='Enter')

        wx.Button(panel, pos=(10,175), size=(115,50), label='Shift')
        wx.Button(panel, pos=(130,175), size=(50,50), label='Z')
        wx.Button(panel, pos=(185,175), size=(50,50), label='X')
        wx.Button(panel, pos=(240,175), size=(50,50), label='C')
        wx.Button(panel, pos=(295,175), size=(50,50), label='V')
        wx.Button(panel, pos=(350,175), size=(50,50), label='B')
        wx.Button(panel, pos=(405,175), size=(50,50), label='N')
        wx.Button(panel, pos=(460,175), size=(50,50), label='M')
        wx.Button(panel, pos=(515,175), size=(50,50), label=',')
        wx.Button(panel, pos=(570,175), size=(50,50), label='.')
        wx.Button(panel, pos=(625,175), size=(50,50), label='/')
        wx.Button(panel, pos=(680,175), size=(145,50), label='Shift')

        wx.Button(panel, pos=(10,230), size=(64,50), label='Ctrl')
        wx.Button(panel, pos=(78,230), size=(64,50), label='Super')
        wx.Button(panel, pos=(147,230), size=(64,50), label='Alt')
        wx.Button(panel, pos=(216,230), size=(330,50), label='-')
        wx.Button(panel, pos=(553,230), size=(64,50), label='Alt')
        wx.Button(panel, pos=(623,230), size=(64,50), label='Fn')
        wx.Button(panel, pos=(693,230), size=(64,50), label='Menu')
        wx.Button(panel, pos=(763,230), size=(63,50), label='Ctrl')

    # def keyPress(self):
    #     if keyboard.is_pressed('q'):
    #         print('you pressed q')

    def Quit(self, e):
        confirmDialog = wx.MessageDialog(None, 'Are you sure?', 'Exit', wx.YES_NO)
        if confirmDialog.ShowModal() == wx.ID_YES:
            self.Close()
        confirmDialog.Destroy()

def main():
    app = wx.App()
    windowClass(None)
    app.MainLoop()

main()