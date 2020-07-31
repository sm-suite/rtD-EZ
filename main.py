#©2020 Jerold B. Larson. All Rights Reserved.


import sys
from tkinter import *
import tkinter as tk
import numpy as np
import os
import tkinter.font as font

dType = 'tp'
#dType = 'fx'


#viz_rng = np.arange(1.5,1.7,.02) #option range EUR/USD
#viz_rng = np.arange(109,110,.05) #option range USD/JPY
#viz_rng = np.arange(5, 16, 1) #total points range MLB
viz_rng = np.arange(40, 51, 1) #total points range NFL


class MyWindow:
	def __init__(self, win):
		#create labels 'lbl' and entry fields 't' for inputs 1-6

		myFont = font.Font(size=18, weight='bold')
		myFont_disp = font.Font(size=16, weight='bold')

		myFontT = font.Font(size=20, weight='bold')
		myFonTit = font.Font(size=24)
		myFont_q = font.Font(size=28, weight='bold')

		if dType == 'fx':
			self.lblb=Label(win, text='Buy', bg='#D6D6D6', fg='black') #lbl1
			self.lbls=Label(win, text='Sell', bg='#DEDEDE', fg='#000000') #lbl1
			self.lbl1=Label(win, text='Size', bg='white', fg='black') #lbl1
			self.lbl2=Label(win, text='Price', bg='white', fg='black')
			self.lbl3=Label(win, text='Strike', bg='white', fg='black')
			self.lbl4=Label(win, text='Size', bg='white', fg='black')
			self.lbl5=Label(win, text='Price', bg='white', fg='black')
			self.lbl6=Label(win, text='Strike', bg='white', fg='black')

		elif dType == 'tp':
			self.lblb=Label(win, text='Over', bg='#D6D6D6', fg='black') #lbl1
			self.lbls=Label(win, text='Under', bg='#DEDEDE', fg='#000000') #lbl1
			self.lbl1=Label(win, text='Risk', bg='white', fg='black') #lbl1
			self.lbl2=Label(win, text='Odds', bg='white', fg='black')
			self.lbl3=Label(win, text='Score', bg='white', fg='black')
			self.lbl4=Label(win, text='Risk', bg='white', fg='black')
			self.lbl5=Label(win, text='Odds', bg='white', fg='black')
			self.lbl6=Label(win, text='Score', bg='white', fg='black')

		self.t1=Entry(bd=1, bg='white', fg='black')#t1
		self.t2=Entry(bd=1, bg='white', fg='black')
		self.t3=Entry(bd=1, bg='white', fg='black')
		self.t4=Entry(bd=1, bg='white', fg='black')
		self.t5=Entry(bd=1, bg='white', fg='black')
		self.t6=Entry(bd=1, bg='white', fg='black')

		#simplify spacing adjustments with spacing variables.
		t1x, label1x, label1y, label4y = 100, 40, 50, 175
		
		#spacing for 6 lbl and 6 t.
		self.lblb.place(x=label1x-15, y=5, height=40, width=80)
		self.lblb['font']=myFonTit

		self.lbls.place(x=label1x-15, y=label4y-45, height=40, width=80)
		self.lbls['font']=myFonTit

		self.lbl1.place(x=label1x, y=label1y)
		self.lbl2.place(x=label1x, y=label1y+25)
		self.lbl3.place(x=label1x, y=label1y+50)
		self.t1.place(x=t1x, y=label1y)
		self.t2.place(x=t1x, y=label1y+25)
		self.t3.place(x=t1x, y=label1y+50)
		self.lbl4.place(x=label1x, y=label4y)
		self.lbl5.place(x=label1x, y=label4y+25)
		self.lbl6.place(x=label1x, y=label4y+50)
		self.t4.place(x=t1x, y=label4y)
		self.t5.place(x=t1x, y=label4y+25)
		self.t6.place(x=t1x, y=label4y+50)

		self.lbl1['font'] = myFont
		self.lbl2['font'] = myFont
		self.lbl3['font'] = myFont
		self.lbl4['font'] = myFont
		self.lbl5['font'] = myFont
		self.lbl6['font'] = myFont

		#update buttons
		butx = 317

		if dType == 'fx':			
			self.btn1=Button(win, text='Update\nBuy\n') #create button, add text
			self.b1=Button(win, text='Update\nBuy\n', width=9, height=7, bg='#FFFFFF', fg='blue', command=self.b1rez) #connect w/ command / format
			self.b1['font'] = myFontT
			self.b1.place(x=butx, y=0) #spacing for buttons
			self.btn2=Button(win, text='Update\nSell\n')
			self.b2=Button(win, text='Update\nSell\n', width=9, height=7, bg='#FFFFFF', fg='blue', command=self.s1rez)
			self.b2['font'] = myFontT
			self.b2.place(x=butx, y=150)


		elif dType == 'tp':

			self.btn1=Button(win, text='Update\nOver\n') #create button, add text
			self.b1=Button(win, text='Update\nOver\n', width=6, height=8, bg='#FFFFFF', fg='blue', command=self.b1rez) #connect w/ command / format
			self.b1['font'] = myFontT
			self.b1.place(x=butx, y=-3) #spacing for buttons
			self.btn2=Button(win, text='Update\nUnder\n')
			self.b2=Button(win, text='Update\nUnder\n', width=6, height=8, bg='#FFFFFF', fg='blue', command=self.s1rez)
			self.b2['font'] = myFontT
			self.b2.place(x=butx, y=147)

		#visual buttons
		self.btn3=Button(win, text='View\nRisk')
		self.b3=Button(win, text='View\nRisk', width=12, height=5, bg='#FFFFFF', fg='#FF8000', command=self.risk)
		self.b3['font'] = myFont
		self.b3.place(x=400, y=-3)

		self.btn4=Button(win, text='View\nPosition')
		self.b4=Button(win, text='View\nPosition', width=12, height=5, bg='#FFFFFF', fg='#FF8000', command=self.pos)
		self.b4['font'] = myFont
		self.b4.place(x=400, y=97)

		self.btn5=Button(win, text='View\nScenario')
		self.b5=Button(win, text='View\nScenario', width=12, height=5, bg='#FFFFFF', fg='#FF8000', command=self.scenario)
		self.b5['font'] = myFont
		self.b5.place(x=400, y=197)




		#quit button
		self.btn7=Button(win, text='Quit')
		self.b7=Button(win, text='Quit', width=5, height=10, bg='#FFFFFF', fg='#CC0000', activebackground='#CC0000', command=quit)
		self.b7['font'] = myFont_q
		self.b7.place(x=555, y=-15)


	def scenario(self):
		if dType=='tp': from tp_chart import scene
		elif dType=='fx': from fx_chart import scene

		scene()

	def risk(self):
		if dType=='tp': from tp_chart import risk
		elif dType=='fx': from fx_chart import risk

		risk()

	def pos(self):
		
		if dType=='tp': from tp_chart import pos
		elif dType=='fx': from fx_chart import pos

		pos()

	def quit(self):
		quit()

		
	def b1rez(self):
		if dType == 'tp':
			b1r, b1o, b1stk=float(self.t1.get()), float(self.t2.get()), float(self.t3.get())
			b1w=float(b1r*(b1o-1))
		elif dType == 'fx':
			b1sz, b1p, b1stk=float(self.t1.get()), float(self.t2.get()), float(self.t3.get())
			b1r=float(b1p * b1sz)
			b1w=float(100*b1sz + (-b1r))
		b1_rez = [b1w if n > abs(b1stk) else -b1r for n in viz_rng]
		with open('b1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', b1_rez[n], file=f)


	def s1rez(self):
		if dType == 'tp':
			s1r, s1o, s1stk=float(self.t4.get()), float(self.t5.get()), float(self.t6.get())
			s1w=float(s1r*(s1o-1))
		elif dType == 'fx':
			s1sz, s1p, s1stk=float(self.t4.get()), float(self.t5.get()), float(self.t6.get())
			s1r= float((100-s1p)*s1sz)
			s1w= float(s1p*(s1sz))
		s1_rez = [s1w if n < abs(s1stk) else -s1r for n in viz_rng]
		with open('s1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', s1_rez[n], file=f)



#GUI
window=Tk() #initialize tcl/tk interpreter
window.title('Real-Time Derivative-EZ v1.5')
window.geometry("650x300-1000-1000")
pass #open GUI w/out A logo.png


mywin=MyWindow(window) #link MyWindow class and tk interpretter

window.mainloop() #execute infinite loop


