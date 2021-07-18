#problem in line 231
from tkinter import *
import socket
import requests
import bs4
from tkinter.messagebox import *
from tkinter.scrolledtext  import *
from sqlite3 import *
import matplotlib.pyplot as plt


con = None
try:
	con = connect("sms_db.db")
	print("connected")
	cursor = con.cursor()
	sql = "create table if not exists sms(rno int primary key,name text,marks int) "
	cursor.execute(sql)
	print("table created")
except Exception as e:
	print("creation issue",e)
finally:
	if con is not None:
		con.close()
		print("disconnected")


def f1():
	adst.deiconify()
	root.withdraw()
def f2():
	stdata.delete(1.0,END)
	ViewSt.deiconify()
	root.withdraw()
	con = None
	try:
		con = connect("sms_db.db")
		print("connected")
	
		cursor = con.cursor()
		sql = "select * from sms"
		cursor.execute(sql)
		data = cursor.fetchall()
		info = ""
		for d in data :
			info = info + "rno: " + str(d[0])+ "	name : " + str(d[1]) + "	marks " + str(d[2])+"\n"
		stdata.insert(INSERT,info)	
	except Exception as e:
		print("select issue ",e)

	finally:
		if con is not None:
			con.close()
			print("disconnected")

def f3():
	updt.deiconify()
	root.withdraw()


def f4():
	dest.deiconify()
	root.withdraw()

def f5():
	marks_plot = []
	name_plot = []
	con = None
	try:
		con = connect("sms_db.db")
		print("connected")
	
		cursor = con.cursor()
		sql = "select name,marks from sms order by marks desc limit 5"
		cursor.execute(sql)
		data = cursor.fetchall()
		for d in data :
			name_plot.append(d[0])
			marks_plot.append(d[1])
		plt.title("marks of top 5 students ")
		plt.xlabel("names")
		plt.ylabel("Marks")
		plt.bar(name_plot,marks_plot)
		plt.grid()
		plt.show()
	except Exception as e:
		print("chart issue ",e)

	finally:
		if con is not None:
			con.close()
			print("disconnected")
def f6():
	root.deiconify()
	adst.withdraw()
def f7():
	root.deiconify()
	ViewSt.withdraw()
def f8():
	root.deiconify()
	updt.withdraw()
def f9():
	root.deiconify()
	dest.withdraw()
#save function
def f10():
	con = None
	try:
		con=connect("sms_db.db")
		print("connected")
		rno = int(entrno.get())
		if (rno<=0) :
			raise Exception("roll no shud only be +ve integers")
		name =entname.get()
		if len(name) in (0,1):
			raise Exception("name shud be min of 2 letters")
		marks = int(entmarks.get())
		if (marks>100) or (marks<0) or (marks == None):
			raise Exception("marks shud be between 0 & 100 ")
		args = (rno,name,marks)
		cursor = con.cursor()
		sql = "insert into sms values('%d','%s','%d')"
		cursor.execute(sql % args)
		con.commit()
		showinfo("success","record added")
	except 	Exception as e:
		showerror("failure","insert issue--> "+str(e) )
		con.rollback()
	finally:
		if con is not None:
			con.close()
			print("disconnected")
#update function
def f11():
	con = None
	try:
		con = connect("sms_db.db")
		print("connected")
		newrno = int(entrno1.get())
		newname = entname1.get()
		if len(newname) in (0,1):
			raise Exception("name shud be min of 2 letters")
		newmarks = int(entmarks1.get())
		if (newmarks>100) or (newmarks<0) or (newmarks == None):
			raise Exception("marks shud be between 0 & 100 ")
		args=(newname,newmarks,newrno)
		cursor=con.cursor()
		sql="update sms set name = '%s',marks='%d' where rno is '%d' "	
		cursor.execute(sql % args)
		if cursor.rowcount >= 1:
			con.commit()
			showinfo("update","record updated")
		else:
			showerror("update","rno does not exists ")
	except Exception as e:
		showerror("update issue ",e)
		con.rollback()
	
	finally:
		if con is not None:
			con.close()
			print('disconnected')

def f12():
	con = None
	try:
		con = connect("sms_db.db")
		print("connected")
		rno = int(entrno2.get())
		args=(rno)
		cursor=con.cursor()
		sql="delete from sms where rno is '%d' "	
		cursor.execute(sql % args)
		if cursor.rowcount >= 1:
			con.commit()
			showinfo("delete","record deleted")
		else:
			showerror("delete","rno does not exists ")
	except Exception as e:
		showerror("delete issue ",e)
		con.rollback()
	
	finally:
		if con is not None:
			con.close()
			print('disconnected')

# design of root window

try:
	string = []
	socket.create_connection( ("www.google.com", 80))
	res1 = requests.get("https://ipinfo.io/")
	data1 = res1.json()
	city_name = data1['city']
	a1 = "http://api.openweathermap.org/data/2.5/weather?units=metric"
	a2 = "&q=" + city_name 
	a3 = "&appid=c6e315d09197cec231495138183954bd"
	res2 = requests.get(a1+a2+a3)
	data2 = res2.json()
	main1 = data2['main']
	temp = main1['temp']
	res3 = requests.get("https://www.brainyquote.com/quote_of_the_day")
	soup = bs4.BeautifulSoup(res3.text,"lxml")
	data3 = soup.find("img")
	qotd = data3['alt']
	string = qotd.split(".")
		
except Exception as e:
	print("issue",e)
	

#ROOT WINDOW		
root = Tk()
root.title("S.M.S")
root.geometry("600x450+400+200")


		
btnAdd = Button(root,text="Add",width=10,font=("aerial",18,"bold"),command=f1)
btnVeiw = Button(root,text="Veiw",width=10,font=("aerial",18,"bold"),command=f2)
btnUpdate = Button(root,text="Update",width=10,font=("aerial",18,"bold"),command=f3)
btnDelete = Button(root,text="Delete",width=10,font=("aerial",18,"bold"),command=f4)
btnCharts = Button(root,text="Charts",width=10,font=("aerial",18,"bold"),command=f5)
lblLocation = Label(root,text="Location :- ",font=("aerial",18,"bold italic"))
lblLocationa = Label(root,text=city_name ,font=("aerial",18,"bold italic"))
lblTemp = Label(root,text="Temp :- ",font=("aerial",18,"bold italic"))
lblTempa = Label(root,text= temp ,font=("aerial",18,"bold italic"))
lblQotd = Label(root,text="Qotd:- ",font=("aerial",18,"bold italic"))
lblQotda = Label(root,text="" ,font=("aerial",10,"bold italic"))
#string[0]+"."+"\n"+string[1]
btnAdd.pack()
btnVeiw.pack()
btnUpdate.pack()
btnDelete.pack()
btnCharts.pack()
lblLocation.place(x=10,y=270)
lblLocationa.place(x=140,y=270)
lblTempa.place(x=530,y=270)
lblTemp.place(x=420,y=270)
lblQotd.place(x=10,y=350)
lblQotda.place(x=100,y=360)

# add window

adst = Toplevel(root)
adst.title("Add St.")
adst.geometry("600x450+400+200")
adst.withdraw()
lblrno = Label(adst,text="enter rno",font=("aerial",18,"bold italic"))
entrno = Entry(adst,bd=5,font=("aerial",18,"bold italic"))
lblname = Label(adst,text="enter name",font=("aerial",18,"bold italic"))
entname = Entry(adst,bd=5,font=("aerial",18,"bold italic"))
lblmarks = Label(adst,text="enter marks",font=("aerial",18,"bold italic"))
entmarks = Entry(adst,bd=5,font=("aerial",18,"bold italic"))
btnsave  =Button(adst,text="Save",font=("aerial",18,"bold italic"),command =f10)
btnback1 =Button(adst,text="Back",font=("aerial",18,"bold italic"),command=f6)
lblrno.pack(pady=5)
entrno.pack(pady=5)
lblname.pack(pady=5)
entname.pack(pady=5)
lblmarks.pack(pady=5)
entmarks.pack(pady=5)
btnsave.pack(pady=5)
btnback1.pack(pady=5)


ViewSt =Toplevel(root)
ViewSt.title("Veiw St.")
ViewSt.geometry("600x450+400+200")
ViewSt.withdraw()
stdata = ScrolledText(ViewSt,width=60,height=20)
btnback2 = Button(ViewSt,text="Back",font=("aerial",18,"bold italic"),command=f7)
stdata.pack(pady=10)
btnback2.pack(pady=10)

updt = Toplevel(root)
updt.title("Update St.")
updt.geometry("600x450+400+200")
updt.withdraw()
lblrno1 = Label(updt,text="enter rno",font=("aerial",18,"bold italic"))
entrno1 = Entry(updt,bd=5,font=("aerial",18,"bold italic"))
lblname1 = Label(updt,text="enter name",font=("aerial",18,"bold italic"))
entname1 = Entry(updt,bd=5,font=("aerial",18,"bold italic"))
lblmarks1 = Label(updt,text="enter marks",font=("aerial",18,"bold italic"))
entmarks1 = Entry(updt,bd=5,font=("aerial",18,"bold italic"))
btnsave1  =Button(updt,text="Save",font=("aerial",18,"bold italic"),command = f11)
btnback3 =Button(updt,text="Back",font=("aerial",18,"bold italic"),command=f8)
lblrno1.pack(pady=5)
entrno1.pack(pady=5)
lblname1.pack(pady=5)
entname1.pack(pady=5)
lblmarks1.pack(pady=5)
entmarks1.pack(pady=5)
btnsave1.pack(pady=5)
btnback3.pack(pady=5)


dest = Toplevel(root)
dest.title("Delete St.")
dest.geometry("600x450+400+200")
dest.withdraw()
lblrno2 = Label(dest,text="enter rno",font=("aerial",18,"bold italic"))
entrno2 = Entry(dest,bd=5,font=("aerial",18,"bold italic"))
btnsave1=Button(dest,text="SAVE",font=("aerial",18,"bold italic"),command=f12)
btnback4=Button(dest,text="BACK",font=("aerial",18,"bold italic"),command=f9)
lblrno2.pack(pady=10)
entrno2.pack(pady=10)
btnsave1.pack(pady=10)
btnback4.pack(pady=10)

root.mainloop()
