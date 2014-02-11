# This project is authored by Vaibhav Agarwal and Anish Shah from BITS Pilani for industrial manufacturing unit. This code is free to use, distribute, and share

import wx
import  wx.calendar
import sqlite3
import datetime

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# This part is used to connect to the database

conn = sqlite3.connect('C:\Python27\db\MyDb') # add the path to your database file 
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS Plant(id INTEGER PRIMARY KEY, d date, unit TEXT, machine TEXT, maintenance TEXT, complain TEXT)")
APP_EXIT = 1

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Class for Search Entries

class Example(wx.Frame):
    
    def __init__(self,*args,**kw):
        super(Example, self).__init__(wx.GetApp().TopWindow,**kw) 
          
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
        unit = ['All','CodeLine Phase1', 'CodeLine Phase2', 'CodeLine Phase3', 'CodeLine Phase4', 'FRP', 'Composite', 'Polyglass', 'HRO', 'MBL', 'Utility']
        self.cb1 = wx.ComboBox(pnl2, pos=(50, 50), choices=unit, value='All',
            style=wx.CB_READONLY)
        self.cb1.SetSize((200,25))
        self.cb1.Bind(wx.EVT_COMBOBOX, self.OnSelect)

        machinename = wx.StaticText(pnl2, label='Machine:', pos=(400, 30))
        machine = ['All','Winding M/C', 'Oven', 'Barrier', 'Extraction', 'Cutoff', 'Sanding', 'Miling', 'Painting', 'Packing', 'Cranes', 'None']
        self.cb2 = wx.ComboBox(pnl2, pos=(400, 50), choices=machine, value='All',
            style=wx.CB_READONLY)
        self.cb2.SetSize((200,25))
        self.cb2.Bind(wx.EVT_COMBOBOX, self.OnSelect)
        
        maintenancename = wx.StaticText(pnl2, label='Type of maintenance:', pos=(750, 30))
        maintenance = ['All','Preventive Maintenance', 'Breakdown Maintenance', 'Predictive Maintenance']
        self.cb3 = wx.ComboBox(pnl2, pos=(750, 50), choices=maintenance, value='All',
            style=wx.CB_READONLY)
        self.cb3.SetSize((200,25))
        self.cb3.Bind(wx.EVT_COMBOBOX, self.OnSelect)

	wx.StaticText(pnl2, label='Start Date:', pos=(50, 130))
        cal2 = wx.calendar.CalendarCtrl(pnl2, -1, wx.DateTime_Now(), pos = (50,160))
        self.date = "%s"%datetime.date.today()
        self.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.OnCalSelChanged, cal2)
        
	

	wx.StaticText(pnl2, label='End Date:', pos=(350, 130))
	cal3 = wx.calendar.CalendarCtrl(pnl2, -1, wx.DateTime_Now(), pos = (350,160))
	self.date2 = "%s"%datetime.date.today()
        self.Bind(wx.calendar.EVT_CALENDAR_SEL_CHANGED, self.OnCalSelChanged2, cal3)
        

        btn = wx.Button(pnl2, 4, 'OK', size=(100, 50),pos=(850,180))      
        self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk, btn,id=4)

        
            
        self.SetSize((1024,450))
        self.SetPosition((200,300))
        self.SetTitle('Search')
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
            machine=['All','Winding M/C', 'Oven', 'Barrier', 'Extraction', 'Cutoff', 'Sanding', 'Miling', 'Painting', 'Packing', 'Cranes', 'None']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('All')
            
        elif i=='FRP':
            machine= ['All','Rotarory M/C','SWB M/C','Dome Preform Assembly','Molding','Oven','Tapping','Air Testing','Packing','Screen Cleaning']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('All')

        elif i=='Composite':
            machine= ['All','Roto Molding','Pulveriser','Mandrel Loading','Winding','Oven 1','Oven 2','Hydrotesting','Crane']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('All')

        elif i=='Polyglass':
            machine= ['All','Blow Molding','Facing and Flaming','Winding','Oven','Air Testing','Grinder','Cutting M/C','Crane']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('All')

        elif i=='HRO':
            machine = ['All','SARM 006','SARM 007','Spacer 006','Spacer 007','Membrane Testing Stand','Curing Oven 1','Curing Oven 2','Brine Sealing 006','Brine Sealing 007','Labeling M/C 006','Labeling M/C 007','Sealing M/C New','Sealing M/C Old','HRO Lift','AHU 1','AHU 2','HRO Crane']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('All')
            
        elif i=='Utility':
            machine = ['All','Boiler 1', 'Boiler 2', 'New MLD Compressor', 'Old MLD Compressor', 'XF 75 Compressor', 'Vaccumm Pump', 'Air Dryer', '4 Ton Diesel Fork Lift', '3 Ton Diesel Fork Lift', '2.5 Ton battery Fork Lift', 'Maint Battery Fork Lift', '15T2 Compressor number 1', '15T2 Compressor number 2', 'Diesel Generator 1', 'Diesel Generator 2', 'Main Hydrant Pump', 'Jockey Pump', 'LPG unloading Pump', 'LPG vacumm Pump', 'CodeLine cycle Tester', 'CodeLine Chardon cycle Tester', 'FRP cycle Tester', 'Composite Cycle Tester', 'Main LT Panel', 'Sewage Treatment Plant', 'Floor Mopping Machine', 'Stacker Machine 1', 'Stacker Machine 2']
            self.cb2.Clear()
            self.cb2.AppendItems(machine)
            self.cb2.SetValue('All')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------

    def OnCalSelected(self, evt):
        print 'OnCalSelected: %s' % evt.GetDate()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Getting Previous Date And Next Date Method

    def OnCalSelChanged(self, evt):
        cal = evt.GetEventObject()
        self.date = cal.PyGetDate()
        print "OnCalSelChanged:\n\t%s: %s\n\t%s: %s\n\t%s: %s\n\t" % ("EventObject", cal, "Date       ", cal.PyGetDate(),
                                                                      "Ticks      ", cal.GetDate().GetTicks())
        
    def OnCalSelChanged2(self, evt):

        cal = evt.GetEventObject()
        self.date2 = cal.PyGetDate()
        print "OnCalSelChanged:\n\t%s: %s\n\t%s: %s\n\t%s: %s\n\t" % ("EventObject", cal, "Date       ", cal.PyGetDate(),
                                                                      "Ticks      ", cal.GetDate().GetTicks())

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
# Ok Button Pressed Method

    def OnLaunchCommandOk(self, event):
        
        global entry1,entry2,entry3,entry4,date1,date2
        self.entry1= self.cb1.GetValue()
        entry1 = self.entry1
        self.entry2= self.cb2.GetValue()
        entry2 = self.entry2
        self.entry3= self.cb3.GetValue()
        entry3 = self.entry3
        date1 = self.date
        date2 = self.date2
        event.Skip()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
        
        
def main():
    ex = wx.App()
    Example(None)
    ex.MainLoop()    

if __name__ == '__main__':
    main()
