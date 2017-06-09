import configparser
import numpy as np
import tkinter as tk #載入tkinter這個library
import tkinter.font as tkFont

class parseini:
	def __init__(self, iniFile):
		self.inifile = iniFile
		
	def calData(self):
		config=configparser.ConfigParser()
		config.read(self.inifile)
		
		dataTitles = config.options('data')	#	'n', 'r1', 'r2', 'r3', 'r4', 'show'
		
		n = int(config['data']['n'])
		
		myMatrix = [] # empty list
		
		for i in dataTitles:
			dataraw = config['data'][i]
			if i[0] == 'r':
				raw = dataraw.split(',')
				row = []
				for r in raw:
					row.append(int(r))
				myMatrix.append(row)
		
		
		print('A=')
		print(myMatrix[0])
		print(myMatrix[1])
		print(myMatrix[2])
		print(myMatrix[3])

		
		numpyMatrix = np.array(myMatrix)
		
		print('A x A=')
		print(np.dot(numpyMatrix, numpyMatrix)) #	點積
		

def click(event):
	x.set(x2.get()+'\n'+str(event.x)+','+str(event.y))
	edTxt2.delete(0, 'end')
	edTxt2.insert(0, x2.get())

def buttonC1():
	x.set("Button1\nClicked!!")


def checkButtonCommand():	#	define function of command. 定義一個命令的function
	s=""	#	empty string(空字串)
	e=lambda i: "\n" if i<2 else ""		#	create anonymous function. 創造一個匿名的函式(功能)
	for i in range(3):
		if valueCheckButton[i].get()==1: s+="Chk"+str(i+4)+ e(i)	#	get checkButton value(拿到檢查按鈕的值)
	x.set(s)	#	update other StringVariable to show something(更新其他字串變數來秀出一些東西)

def listBox1Click(event):
	s=listBox1.get(listBox1.curselection()[0])
	x.set(s)


def listBox2Click(event):
	s=listBox2.get(listBox2.curselection()[0])
	x.set(s)

		
def main():
	p = parseini('0551284_1.ini')
	p.calData()
	
	

	
	
if __name__ == "__main__":
	main()
	root=tk.Tk()	# 創造一個根源(基本)的視窗，是一個起源的視窗
	root.title("期中考0551284")
	root.geometry("600x400")	#	設置一個專屬的視窗尺寸
	label=tk.Label(root, text='Hello')
	label.config(bg='white', fg='#ffffff')
	
	myFont=tkFont.Font(family='標楷體', size=20, underline=True)
	
	
	x=tk.StringVar()
	x.set('土木工程研究所碩士班')
	label=tk.Label(root, textvariable=x, font=myFont, height=3, width=20,
				anchor='ne', bg='#ffffff', fg='#000000', cursor='star')
	label.grid(row=1, column=1, rowspan=1)
	
	button1=tk.Button(root, text='按鈕物件', command=checkButtonCommand)
	button1.grid(row=3, column=3)
	
	valueCheckButton=list()	#	define empty list(定義一個空list)
	for i in range(3):
		valueCheckButton.append(tk.IntVar())	#	append IntVar into list. 把整數變數加到list中標籤為最小且沒東西在的空格中。
	
	location1=['sw', 's', 'se']		#	three checkButtons show in different locations(三個檢查按鈕分別秀出不同的方位)
	

	listBox1=tk.Listbox(root, width=8)
	listBox1.insert(1, 'Python')
	listBox1.insert(2, 'C++')
	listBox1.insert(3, 'Fortran')
	listBox1.insert(4, 'BASIC')
	listBox1.insert(5, 'Javascript')
	
	listBox1.bind("<ButtonRelease-1>", listBox1Click)
	#listBox1.bind("<Button-1>", listBox1Click)
	listBox1.grid(row=2, column=2, sticky='nw')
	
	root.mainloop()	 # 絕對要放最後!!  開啟運行的事件。
	
	
#label.pack()	# 置中
#label.grid()	#	置於左上角，做為起點開始


#button2=tk.Button(root, text="Button2")
#button2.grid(row=3, column=4, sticky='e')

