# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.animate

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer1.Add( self.m_textCtrl1, 0, 0, 5 )
		
		self.m_animCtrl1 = wx.animate.AnimationCtrl( self, wx.ID_ANY, wx.animate.NullAnimation, wx.Point( -1,-1 ), wx.Size( -1,-1 ), wx.animate.AC_DEFAULT_STYLE )
		self.m_animCtrl1.LoadFile( u"C:\\Users\\ATUser\\Documents\\GitHub\\Goal_Reach\\loading-animation.gif" )
		
		self.m_animCtrl1.Play()
		bSizer1.Add( self.m_animCtrl1, 0, wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

