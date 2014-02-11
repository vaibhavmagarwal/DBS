# This project is authored by Vaibhav Agarwal and Anish Shah from BITS Pilani for industrial manufacturing unit. This code is free to use, distribute and share

import wx
import  wx.calendar
import sqlite3
import datetime

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# This part is used to connect to the database

conn = sqlite3.connect('C:\Python27(32bit)\ps1\db\MyDb')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Plant(id INTEGER PRIMARY KEY, d date, unit TEXT, machine TEXT, maintenance TEXT, complain TEXT)")

APP_EXIT = 1

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Class for New Entries

class Example(wx.Frame):
    
    def __init__(self,*args):
        super(Example, self).__init__(wx.GetApp().TopWindow)   
        self.InitUI()
        
    def InitUI(self):    

        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        qmi = wx.MenuItem(fileMenu,APP_EXIT,'&Quit\tCtrl+Q')
        qmi.SetBitmap(wx.Bitmap('image/exit.png'))
        fileMenu.AppendItem(qmi)
        menubar.Append(fileMenu, '&File')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.OnQuit, id=APP_EXIT)
        
        pnl2 = wx.Panel(self)
        
        unitname = wx.StaticText(pnl2, label='Unit:', pos=(50, 30))
        unit = ['CodeLine Phase1', 'CodeLine Phase2', 'CodeLine Phase3', 'CodeLine Phase4', 'FRP', 'Composite', 'Polyglass', 'HRO', 'MBL', 'Utility']
        self.cb1 = wx.ComboBox(pnl2, pos=(50, 50), choices=unit, value='CodeLine Phase1',
            style=wx.CB_READONLY)
        self.cb1.SetSize((200,25))
        self.cb1.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        machinename = wx.StaticText(pnl2, label='Machine:', pos=(400, 30))
        machine = ['Winding M/C', 'Oven', 'Barrier', 'Extraction', 'Cutoff', 'Sanding', 'Miling', 'Painting', 'Packing', 'Cranes', 'None']
        self.cb2 = wx.ComboBox(pnl2, pos=(400, 50), choices=machine, value='None',
            style=wx.CB_READONLY)
        self.cb2.SetSize((200,25))
        self.cb2.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        
        maintenancename = wx.StaticText(pnl2, label='Type of maintenance:', pos=(750, 30))
        maintenance = ['Preventive Maintenance', 'Breakdown Maintenance', 'Predictive Maintenance']
        self.cb3 = wx.ComboBox(pnl2, pos=(750, 50), choices=maintenance, value='Preventive Maintenance',
            style=wx.CB_READONLY)
        self.cb3.SetSize((200,25))
        self.cb3.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        wx.StaticText(pnl2, label='Enter your complain:', pos=(50, 130))
        self.complainbox = wx.TextCtrl(pnl2, wx.ID_ANY, size=(900,200), pos=(50,150),
                          style = wx.TE_MULTILINE|wx.HSCROLL)
        
        cal2 = wx.calendar.CalendarCtrl(pnl2, -1, wx.DateTime_Now(), pos = (50,400))
        self.date = "%s"%datetime.date.today()
        self.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.OnCalSelChanged, cal2)
        
        btn = wx.Button(pnl2,3, 'OK', size=(100, 50),pos=(850,400))      
        self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk, btn,id=3)

        self.SetSize((1024,768))
        self.SetPosition((200,300))
        self.SetTitle('New Entry')
        self.Show(True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------        
# On Quit Method

    def OnQuit(self, e):
        self.Close()
        
#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Combobox Values

    def OnSelect(self, e):
        i = e.GetString()
        
        if(i=='CodeLine Phase1' or i=='CodeLine Phase2' or i=='CodeLine Phase3' or i=='CodeLine Phase4'):
            machine=['Winding M/C', 'Oven', 'Barrier', 'Extraction', 'Cutoff', 'Sanding', 'Miling', 'Painting', 'Packing', 'Cranes', 'None']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('None')
            
        elif i=='FRP':

            machine= ['Rotarory M/C','SWB M/C','Dome Preform Assembly','Molding','Oven','Tapping','Air Testing','Packing','Screen Cleaning']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('Rotarory M/C')

        elif i=='Composite':

            machine= ['Roto Molding','Pulveriser','Mandrel Loading','Winding','Oven 1','Oven 2','Hydrotesting','Crane']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('Roto Molding')

        elif i=='Polyglass':

            machine= ['Blow Molding','Facing and Flaming','Winding','Oven','Air Testing','Grinder','Cutting M/C','Crane']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('Blow Molding')
            
        elif i=='HRO':
            machine = ['SARM 006','SARM 007','Spacer 006','Spacer 007','Membrane Testing Stand','Curing Oven 1','Curing Oven 2','Brine Sealing 006','Brine Sealing 007','Labeling M/C 006','Labeling M/C 007','Sealing M/C New','Sealing M/C Old','HRO Lift','AHU 1','AHU 2','HRO Crane']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('SARM 006')

        elif i=='Utility':
            machine = ['Boiler 1', 'Boiler 2', 'New MLD Compressor', 'Old MLD Compressor', 'XF 75 Compressor', 'Vaccumm Pump', 'Air Dryer', '4 Ton Diesel Fork Lift', '3 Ton Diesel Fork Lift', '2.5 Ton battery Fork Lift', 'Maint Battery Fork Lift', '15T2 Compressor number 1', '15T2 Compressor number 2', 'Diesel Generator 1', 'Diesel Generator 2', 'Main Hydrant Pump', 'Jockey Pump', 'LPG unloading Pump', 'LPG vacumm Pump', 'CodeLine cycle Tester', 'CodeLine Chardon cycle Tester', 'FRP cycle Tester', 'Composite Cycle Tester', 'Main LT Panel', 'Sewage Treatment Plant', 'Floor Mopping Machine', 'Stacker Machine 1', 'Stacker Machine 2']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('Boiler 1')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Getting Date Method

    def OnCalSelected(self, evt):
        print 'OnCalSelected: %s' % evt.GetDate()

    def OnCalSelChanged(self, evt):

        cal = evt.GetEventObject()
        self.date = cal.PyGetDate()
        print "OnCalSelChanged:\n\t%s: %s\n\t%s: %s\n\t%s: %s\n\t" % ("EventObject", cal, "Date       ", cal.PyGetDate(),
                                                                      "Ticks      ", cal.GetDate().GetTicks())

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ok Button Pressed Method

    def OnLaunchCommandOk(self, event):
        
        dial = wx.MessageDialog(None, 'Are you sure you want to add this entry?', 'Confirm',
            wx.YES|wx.NO)
        result = dial.ShowModal()
        if(result == wx.ID_YES):
            self.entry1= self.cb1.GetValue()
            self.entry2= self.cb2.GetValue()
            self.entry3= self.cb3.GetValue()
            self.entry4= self.complainbox.GetValue()
            c.execute ("INSERT INTO Plant(d,unit,machine,maintenance,complain) VALUES (?,?,?,?,?)",(self.date,self.entry1,self.entry2,self.entry3,self.entry4))
            conn.commit()
            event.Skip()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------        
        
def main():    
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__': main()
