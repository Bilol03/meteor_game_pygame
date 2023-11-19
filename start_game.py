import wx
import main

class MainScreen(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title='Game', size=(300,300))
        self.panel = wx.Panel(self)

        
        self.easy = wx.Button(self.panel, label='Easy')
        self.easy.Bind(wx.EVT_BUTTON, self.easy_button)
        
        self.medium = wx.Button(self.panel, label='Medium')
        self.medium.Bind(wx.EVT_BUTTON, self.medium_button)
        
        self.hard = wx.Button(self.panel, label='Hard')
        self.hard.Bind(wx.EVT_BUTTON, self.hard_button)
        
        self.easy.SetPosition((100,50))
        self.medium.SetPosition((100,100))
        self.hard.SetPosition((100,150))
        
        
        
    def easy_button(self, event):
        print('Starting game...')
        game = main.main(level='easy')
        print('Game Over')
    
    def medium_button(self, event):
        print('Starting game...')
        game = main.main(level='medium')
        print('Game Over')
        
    def hard_button(self, event):
        print('Starting game...')
        game = main.main(level='hard')
        print('Game Over')

        


class Show(wx.App):
    def OnInit(self):
        frame = MainScreen()
        frame.Show()
        return True
    

app = Show()
app.MainLoop()