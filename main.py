#©2020 Jerold B. Larson. All Rights Reserved.


import sys
from tkinter import *
import tkinter as tk
import numpy as np
import os
import tkinter.font as font

#range of values for the visual
#viz_rng = np.arange(1.5,1.7,.02) #option range EUR/USD
#viz_rng = np.arange(109,110,.05) #option range USD/JPY
viz_rng = np.arange(35, 46, 1) #total points range NFL


class MyWindow:
	def __init__(self, win):
		#create labels 'lbl' and entry fields 't' for inputs 1-6

		myFont = font.Font(size=18, weight='bold')
		myFontT = font.Font(size=20, weight='bold')
		myFonTit = font.Font(size=24)
		myFont_q = font.Font(size=28, weight='bold')

		self.lblb=Label(win, text='Over', bg='#D6D6D6', fg='black') #lbl1
		self.lbls=Label(win, text='Under', bg='#DEDEDE', fg='#000000') #lbl1


		self.lbl1=Label(win, text='Risk') #lbl1
		self.lbl2=Label(win, text='Odds')
		self.lbl3=Label(win, text='Score')
		self.lbl4=Label(win, text='Risk')
		self.lbl5=Label(win, text='Odds')
		self.lbl6=Label(win, text='Score')

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
		butx = 300
		self.btn1=Button(win, text='Update\nOver') #create button, add text
		self.b1=Button(win, text='Update\nOver', width=9, height=7, bg='#FFFFFF', fg='blue', command=self.b1rez) #connect w/ command / format
		self.b1['font'] = myFontT
		self.b1.place(x=butx, y=0) #spacing for buttons

		self.btn2=Button(win, text='Update\nUnder')
		self.b2=Button(win, text='Update\nUnder', width=9, height=7, bg='#FFFFFF', fg='blue', command=self.s1rez)
		self.b2['font'] = myFontT

		self.b2.place(x=butx, y=150)



		#visual button

		self.btn3=Button(win, text='Display\nPosition\nVisual')
		self.b3=Button(win, text='Display\nPosition\nVisual', width=8, height=7, bg='#FFFFFF', fg='#FF8000', command=self.position)
		self.b3['font'] = myFontT
		self.b3.place(x=420, y=0)



		#quit button
		self.btn4=Button(win, text='Display\nRisk\nVisual')
		self.b4=Button(win, text='Display\nRisk\nVisual', width=8, height=7, bg='#FFFFFF', fg='#FF8000', command=self.risk)
		self.b4['font'] = myFontT
		self.b4.place(x=420, y=150)

		#quit button
		self.btn5=Button(win, text='Quit')
		self.b5=Button(win, text='Quit', width=6, height=10, bg='#FFFFFF', fg='#CC0000', activebackground='#CC0000', command=quit)
		self.b5['font'] = myFont_q
		self.b5.place(x=533, y=0)

	def risk(self):
		from chart import view6
		view6()



	def position(self):
		from chart import view9
		view9()

	def quit(self):
		quit()

	def b1rez(self):
		b1r, b1o, b1stk=float(self.t1.get()), float(self.t2.get()), float(self.t3.get())
		#if b1o > 0: b1oD = (abs(b1o/100) + 1) #american odds instead of decimal
		#else: b1oD = (100/abs(b1o) + 1)
		#b1w=float(b1r*(b1oD-1))
		b1w=float(b1r*(b1o-1))
		b1_rez = [b1w if n > abs(b1stk) else -b1r for n in viz_rng]
		with open('b1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', b1_rez[n], file=f)

	def s1rez(self):
		s1r, s1o, s1stk=float(self.t4.get()), float(self.t5.get()), float(self.t6.get())
		#if s1oD > 0: s1oD = (abs(s1o/100) + 1)
		#else: s1oD = (100/abs(s1o) + 1)
		#s1w=float(s1r*(s1oD-1))
		s1w=float(s1r*(s1o-1))
		s1_rez = [s1w if n < abs(s1stk) else -s1r for n in viz_rng]
		with open('s1results.txt', 'w') as f:
			for n in range(0,len(viz_rng)): print(viz_rng[n], ',', s1_rez[n], file=f)

#GUI
window=Tk() #initialize tcl/tk interpreter
window.title('Real-Time Derivative-EZ v1.3')
window.geometry("950x300-1000-1000")
try:	
	logo=tk.PhotoImage(file="logo.png") 
	w1=tk.Label(window, image=logo).pack(side="right")
except:
	label = Label(window)
	label.img = PhotoImage(file="logo.png")
	label.config(image=label.img)
	label.pack()

finally: pass #open GUI w/out A logo.png



mywin=MyWindow(window) #link MyWindow class and tk interpretter

window.mainloop() #execute infinite loop


