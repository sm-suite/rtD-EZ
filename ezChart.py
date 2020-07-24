import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
plt.style.use(['seaborn-dark'])
plt.style.use(['seaborn-darkgrid'])

import matplotlib.animation as animation
import time

ro = lambda x : round(x, ndigits=2)



def overview():
	fig = plt.figure(figsize=(10, 8))
	ax1, ax2 = fig.add_subplot(331), fig.add_subplot(332)
	ax3, ax4 = fig.add_subplot(333), fig.add_subplot(334)
	ax5, ax6 = fig.add_subplot(335), fig.add_subplot(336)
	ax7, ax8 = fig.add_subplot(337), fig.add_subplot(338)
	ax9 = fig.add_subplot(339)

	def AniOverview(i):
		pullData = open("b1results.txt","r").read()
		pullData1 = open("s1results.txt", "r").read()
		dataArray = pullData.split('\n') 
		dataArray1 = pullData1.split('\n')
		viz_rng, net, b1, s1 = [], [], [], []
		for eachLine in dataArray:
			if len(eachLine)>1: 
				x,y = eachLine.split(',')
				viz_rng.append(float(x))
				b1.append(float(y))
		for eachLine in dataArray1:
			if len(eachLine)>1:
				j,b = eachLine.split(',')
				s1.append(float(b))

		zipped_rez = zip(b1, s1)
		net = [x+y for (x,y) in zipped_rez]
		trisk = abs(min(b1)) + abs(min(s1))
		roi = [(val/trisk)*100 for val in net]
		broi = [(val/trisk)*100 for val in b1]
		sroi = [(val/trisk)*100 for val in s1]
		b1r, s1r, b1w, s1w = ro(abs(min(b1))), ro(abs(min(s1))), ro(max(b1)), ro(max(s1))
		ww, wl, lw = ro(b1w+s1w), ro(b1w-s1r), ro(s1w-b1r)
		wwr, wlr, lwr = ro((ww/trisk)*100), ro((wl/trisk)*100), ro((lw/trisk)*100)

		Lout = [wwr, wlr, lwr]

		ss = sum(Lout)

			
		if min(b1) < min(s1): prmin = int(round(min(b1), ndigits=0))
		else: prmin = int(round(min(s1), ndigits=0))
		if max(b1) < max(s1): prmax = int(round(max(b1), ndigits=0))
		else: prmax = int(round(max(s1), ndigits=0))
		

		Lrisk = [b1r, s1r]
		Lret = [b1w, s1w]
		LL = [b1r, b1w, s1r, s1w]
		LLabel = 'over-risk', 'over-return','under-risk', 'under-return'
		labels='Over-Risk', 'Under-Risk'
		for ax in [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]: ax.clear()

		ax1.clear()

		ax1.barh('Under\n $' + str(s1r), s1r, color='#FF0000')
		ax1.barh('Over\n $' + str(b1r), b1r, color='#009900')

		ax2.clear()
		ax2.barh('Under\n $' + str(s1w), s1w, color='#FF0000')

		ax2.barh('Over\n $' + str(b1w), b1w, color='#009900')

		
		ax3.clear()

		if lwr > wlr:
			ax3.barh('loss-win\n %' + str(lwr), lwr, color='#FFFF00')
			ax3.barh('win-loss\n %' + str(wlr), wlr, color='#FF0000')
			ax3.barh('win-win\n %' + str(wwr), wwr, color='#009900')
		else:
			ax3.barh('loss-win\n %' + str(lwr), lwr, color='#FF0000')
			ax3.barh('win-loss\n %' + str(wlr), wlr, color='#FFFF00')
			ax3.barh('win-win\n %' + str(wwr), wwr, color='#009900')
		


		ax4.clear()
		ax4.pie(Lrisk, labels=['over-risk', 'under-risk'], colors=['#009900', '#FF0000'], autopct='%.0f%%')

		
		ax5.clear()
		ax5.pie(Lret, labels=['over-return', 'under-return'], colors=['#009900', '#FF0000'], autopct='%.0f%%')

		ax6.clear()

		#ax6.scatter(viz_rng, broi, sroi, roi)
		ax6.pie(LL, labels=LLabel, colors=['#336600', '#99FF99', '#CC0000', '#FFCCCC'], autopct='%.0f%%')


		ax7.clear()
		ax7.stem(viz_rng,broi, linefmt='None', markerfmt='g--', use_line_collection=True)
		ax7.plot(viz_rng,broi, 'C7o', alpha=0.5)
		ax7.stem(viz_rng,roi, linefmt='None', markerfmt='yv', use_line_collection=True)

		ax8.clear()

		ax8.stem(viz_rng,sroi, linefmt='None', markerfmt='r--', use_line_collection=True)		
		ax8.plot(viz_rng,sroi, 'C6o', alpha=0.5)
		ax8.stem(viz_rng,roi, linefmt='None', markerfmt='yv', use_line_collection=True)

		ax9.clear()

		ax9.stem(viz_rng,sroi, linefmt='None', markerfmt='r--', use_line_collection=True)		
		ax9.stem(viz_rng,broi, linefmt='None', markerfmt='g--', use_line_collection=True)
		ax9.stem(viz_rng,roi, linefmt='None', markerfmt='yD', use_line_collection=True)



		ax1.set_title("Risk($)", fontsize=12)
		ax2.set_title("Return($)", fontsize=12)

		ax3.set_title("Scenario ROI(%)", fontsize=12)
		#ax4.set_title("Over/Under Risk", fontsize=12)
		#ax5.set_title("Over/Under Return", fontsize=12)
		ax7.set_title("over/net", fontsize=12)
		ax8.set_title("under/net", fontsize=12)
		ax9.set_title("all", fontsize=12)
		for ax in [ax7]: ax.set_ylabel('ROI(%)')
		ax6.set_xticks([])
		#for ax in [ax8, ax9]: ax.set_xticks([])
		#for ax in [ax5, ax6]: ax.set_xlabel('Return', fontsize=14)

	fig.suptitle("Real-Time-Deriv-EZ v1.0", fontsize=16)
	ani = animation.FuncAnimation(fig, AniOverview, interval=1000)
	plt.show()


#overview()
#overunder()
#roi()