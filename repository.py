# This project is authored by Vaibhav Agarwal and Anish Shah from BITS Pilani for a industrial manufacturing unit. This code is free to use, distribute and share

# repository.py

import wx
import sys
import sqlite3
import project
import search
import datetime
from wx.lib.mixins.listctrl import CheckListCtrlMixin, ListCtrlAutoWidthMixin

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# This part is used to connect to the database

conn = sqlite3.connect('C:\Python27(32bit)\ps1\db\MyDb')
c = conn.cursor()
currdate = "%s"%(datetime.date.today())
oldesttime= datetime.date.today()-datetime.timedelta(weeks=260)
previous_week=datetime.date.today()-datetime.timedelta(weeks=4)
oldesttime= "%s"%oldesttime
previous_week = "%s"%previous_week

c.execute("DELETE FROM Plant WHERE d<='%s'"%oldesttime)
conn.commit()

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# CheckListCtrl

class CheckListCtrl(wx.ListCtrl, CheckListCtrlMixin, ListCtrlAutoWidthMixin):
    def __init__(self, parent):
        wx.ListCtrl.__init__(self, parent, -1, size=(0,1024),style=wx.LC_REPORT | wx.SUNKEN_BORDER)
        CheckListCtrlMixin.__init__(self)
        ListCtrlAutoWidthMixin.__init__(self)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Main Class

class Repository(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title, size=(1024, 768))

        panel = wx.Panel(self, -1)

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        leftPanel = wx.Panel(panel, -1)
        rightPanel = wx.Panel(panel, -1)

        self.log = wx.TextCtrl(rightPanel, -1,size=(400,100), style=wx.TE_MULTILINE)
        self.list = CheckListCtrl(rightPanel)
        self.list.InsertColumn(0, '', width=20)
        self.list.InsertColumn(1, 'Date', width=100)
        self.list.InsertColumn(2, 'Unit',width = 140)
        self.list.InsertColumn(3, 'Machine',width = 140)
        self.list.InsertColumn(4, 'Maintenance',width = 150)
        self.list.InsertColumn(5, 'Complain',width = 200)
                
        c.execute("SELECT * FROM Plant WHERE d>=? AND d<=?",(previous_week,currdate))
        rows=c.fetchall()
        for i in reversed(rows):
            index = self.list.InsertStringItem(sys.maxint, i[1])
            self.list.SetStringItem(index, 0, str(i[0]))
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])
            self.list.SetStringItem(index, 3, i[3])
            self.list.SetStringItem(index, 4, i[4])
            self.list.SetStringItem(index, 5, i[5])
            
        vbox2 = wx.BoxSizer(wx.VERTICAL)

        sel = wx.Button(leftPanel, -1, 'Search', size=(100, -1))
        des = wx.Button(leftPanel, -1, 'New Entry', size=(100, -1))
        delete = wx.Button(leftPanel, -1, 'Delete', size=(100, -1))

        rightPanel.Bind ( wx.EVT_LIST_ITEM_SELECTED, self.OnItemSelect, self.list ) 
        self.Bind(wx.EVT_BUTTON, self.OnSelectAll, id=sel.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnClick, id=des.GetId())
        self.Bind(wx.EVT_BUTTON, self.OnDel, id=delete.GetId())

        vbox2.Add(sel, 0, wx.ALL, 5)
        vbox2.Add(des, 0, wx.ALL, 5)
        vbox2.Add(delete, 0, wx.ALL, 5)

        leftPanel.SetSizer(vbox2)

        vbox.Add(self.list, 1, wx.EXPAND | wx.TOP, 3)
        vbox.Add((-1, 10))
        vbox.Add(self.log, 0.5, wx.EXPAND)
        vbox.Add((-1, 10))

        rightPanel.SetSizer(vbox)

        hbox.Add(leftPanel, 0, wx.EXPAND | wx.RIGHT, 5)
        hbox.Add(rightPanel, 1, wx.EXPAND)
        hbox.Add((3, -1))

        panel.SetSizer(hbox)

        self.Centre()
        self.Show(True)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Search Call Method

    def OnSelectAll(self, event):
        search.Example(None)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClicked,id=4)

#------------------------------------------------------------------------------------------------------------------------------------------------------------
# Searching and Populating the main frame

    def OnButtonClicked(self, e):        
        self.list.DeleteAllItems()
        if((search.date1)==(currdate) and (search.date2)==(currdate)):
            if(search.entry1=='All' and search.entry2=='All' and search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE d>=? AND d<=?",(previous_week,currdate))
            elif(search.entry1=='All' and search.entry2=='All'):
                c.execute("SELECT * FROM Plant WHERE maintenance='%s'"%(search.entry3))
            elif(search.entry2=='All' and search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE unit='%s'"%(search.entry1))
            elif(search.entry1=='All' and search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE machine='%s'"%(search.entry2))
            elif(search.entry1=='All'):
                c.execute("SELECT * FROM Plant WHERE machine='%s' AND maintenance='%s'"%(search.entry2,search.entry3))
            elif(search.entry2=='All'):
                c.execute("SELECT * FROM Plant WHERE unit='%s' AND maintenance='%s'"%(search.entry1,search.entry3))
            elif(search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE unit='%s' AND machine='%s'"%(search.entry1,search.entry2))
            else:
                c.execute("SELECT * FROM Plant WHERE unit='%s' AND machine='%s' AND maintenance='%s'"%(search.entry1,search.entry2,search.entry3))
        else:
            if(search.entry1=='All' and search.entry2=='All' and search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE d>=? AND d<=?",(search.date1,search.date2))
            elif(search.entry1=='All' and search.entry2=='All'):
                c.execute("SELECT * FROM Plant WHERE maintenance='%s' AND d>=? AND d<=?"%(search.entry3),(search.date1,search.date2))
            elif(search.entry2=='All' and search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE unit='%s' AND d>=? AND d<=?"%(search.entry1),(search.date1,search.date2))
            elif(search.entry1=='All' and search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE machine='%s' AND d>=? AND d<=?"%(search.entry2),(search.date1,search.date2))
            elif(search.entry1=='All'):
                c.execute("SELECT * FROM Plant WHERE machine='%s' AND maintenance='%s' AND d>=? AND d<=?"%(search.entry2,search.entry3),(search.date1,search.date2))
            elif(search.entry2=='All'):
                c.execute("SELECT * FROM Plant WHERE unit='%s' AND maintenance='%s' AND d>=? AND d<=?"%(search.entry1,search.entry3),(search.date1,search.date2))
            elif(search.entry3=='All'):
                c.execute("SELECT * FROM Plant WHERE unit='%s' AND machine='%s' AND d>=? AND d<=?"%(search.entry1,search.entry2),(search.date1,search.date2))
            else:
                c.execute("SELECT * FROM Plant WHERE unit='%s' AND machine='%s' AND maintenance='%s' AND d>=? AND d<=?"%(search.entry1,search.entry2,search.entry3),(search.date1,search.date2))
            
        rows=c.fetchall()
        self.OnApply(True,rows)
        e.Skip()
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Add New Entry Method
       
    def OnClick(self, event):
        project.Example(None)
        self.Bind(wx.EVT_BUTTON, self.OnLaunchCommandOk,id=3)

    def OnLaunchCommandOk(self, e):
        c.execute("SELECT * FROM Plant WHERE d>=? AND d<=?",(previous_week,currdate))
        rows=c.fetchall()
        self.OnApply(True,rows)
        e.Skip()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Delete Method

    def OnDel(self, event):
        num = self.list.GetItemCount()
        for i in range(num):
            if self.list.IsChecked(i):
                query = "DELETE FROM Plant WHERE id='%s'"%(self.list.GetItemText(i,0))
                c.execute(query)
                conn.commit()
        c.execute("SELECT * FROM Plant WHERE d>=? AND d<=?",(previous_week,currdate))
        rows=c.fetchall()
        self.OnApply(True,rows)

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Lower TextCtrl Box Method

    def OnItemSelect ( self, event): 
        item = event.GetIndex()
        self.log.Clear()
        self.log.AppendText(self.list.GetItemText(item,5) + '\n')
         
#-------------------------------------------------------------------------------------------------------------------------------------------------------------
# Refresh and Update Method

    def OnApply(self, event,rows):
        self.list.DeleteAllItems()
        for i in reversed(rows):
            index = self.list.InsertStringItem(sys.maxint, i[1])
            self.list.SetStringItem(index, 0, str(i[0]))
            self.list.SetStringItem(index, 1, i[1])
            self.list.SetStringItem(index, 2, i[2])
            self.list.SetStringItem(index, 3, i[3])
            self.list.SetStringItem(index, 4, i[4])
            self.list.SetStringItem(index, 5, i[5])

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
            
app = wx.App()
Repository(None, -1, 'Plant(Manufacturing Line)')
app.MainLoop()

