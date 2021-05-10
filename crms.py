from tkinter import *;
from tkinter import messagebox
from tkinter import simpledialog
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry
from PIL import Image, ImageTk
import sqlite3
from sqlite3 import Error

#---------------------------------------------------------DatabaseFuntions---------------------------------------------------------
#Create Connection 
try:
	global conn 
	conn = sqlite3.connect("C:\SE Project\crime.db")
	print(sqlite3.version)

except Error as e:
	print(e)

#Creating New Admin
def insert_admin(conn, admin):

	sql = ''' INSERT INTO admin(username,password)
			VALUES(?,?) '''
	cur = conn.cursor()
	cur.execute(sql, admin)
	print(cur.lastrowid)

if __name__ == '__main__':
	admin_id=('sharu','sharu123');
	insert_admin(conn, admin_id)
	admin_id=('jagrati','jagrati123');
	insert_admin(conn, admin_id)

#new user
def insert_user(conn, user):

	sql = ''' INSERT INTO user(fname,lname,username,password)
			VALUES(?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, user)
	print(cur.lastrowid)

def insert_fir(conn, fir):
        sql = '''INSERT INTO fir(firno,victimfname,victimlname,dateofincident,criminalfname,criminallname,crimecommitted,placeofincident)
                        VALUES(?,?,?,?,?,?,?,?)'''
        cur = conn.cursor()
        cur.execute(sql,fir)
        print(cur.lastrowid)

if __name__ == '__main__':
        fir_id=('1','abc','def','5/05/2021','pqr','stu','robbery','kalyan');
        insert_fir(conn, fir_id)
        fir_id=('2','sharu','chabukswar','5/06/2021','jagrati','chandwani','kidnapping','ambernath');
        insert_fir(conn, fir_id)
        fir_id=('3','tester1','xyz','5/07/2021','tester2','xyz','murder','watumull');
        insert_fir(conn, fir_id)
        fir_id=('4','sonal','chauhan','5/10/2021','mohit','chabbria','half murder','kalyan');
        insert_fir(conn, fir_id)






#----------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------FIRFunctions----------------------------------------------------------

#Lodge FIR
def addfir():
	tempfirno=StringVar();
	tempvfname=StringVar();
	tempvlname=StringVar();
	tempdate=StringVar();
	tempcfname=StringVar();
	tempclname=StringVar();
	tempcrime=StringVar();
	tempplace=StringVar();
	
	
	

	tempfirno=fir_no.get();
	tempvfname=victim_fname.get();
	tempvlname=victim_lname.get();
	tempdate=date_of_incident.get();
	tempcfname=criminal_fname.get();
	tempclname=criminal_lname.get();
	tempcrime=crime_committed.get();
	tempplace=place_of_incident.get();
	
	
	

	if tempfirno==''or tempvfname=='' or tempvlname=='' or tempdate==''or tempcfname=='' or tempclname=='' or tempcrime=='' or tempplace=='':
		tkinter.messagebox.showinfo("Warning!","One or more fields are empty!")
		lodgefirview()

	else: 
		cur=conn.cursor();
		cur.execute(''' SELECT firno FROM fir WHERE firno='%s' ''' % (tempfirno))
		if cur.fetchone() is not None:
			tkinter.messagebox.showinfo("Warning!","Fir No. Already Exists! Enter New FIR No.!")
			lodgefirview()
		else:
			cur.execute(''' INSERT INTO fir(firno,victimfname,victimlname,dateofincident,criminalfname,criminallname,crimecommitted,placeofincident)
					VALUES('%s','%s','%s','%s','%s','%s','%s','%s') ''' % (tempfirno,tempvfname,tempvlname,tempdate,tempcfname,tempclname,tempcrime,tempplace))
			print(tempfirno)
			tkinter.messagebox.showinfo("FIR","New FIR Added Successfully!")

#Update FIR
def updatefir():
	uptempfirno=StringVar();
	uptempvfname=StringVar();
	uptempvlname=StringVar();
	uptempdate=StringVar();
	uptempcfname=StringVar();
	uptempclname=StringVar();
	uptempcrime=StringVar();
	uptempplace=StringVar();
	

	uptempfirno=afindby1
	print("up",uptempfirno)
	uptempvfname=avictim_fname.get();
	uptempvlname=avictim_lname.get();
	uptempdate=adate_of_incident.get();
	uptempcfname=acriminal_fname.get();
	uptempclname=acriminal_lname.get();
	uptempcrime=acrime_committed.get();
	uptempplace=aplace_of_incident.get();
	

	if uptempvfname=='' or uptempvlname=='' or uptempdate==''or uptempcfname=='' or uptempclname=='' or uptempcrime=='' or uptempplace=='':
		tkinter.messagebox.showinfo("Warning!","One or more fields are empty!")
	else:
		cur=conn.cursor();
		cur.execute(''' UPDATE fir SET victimfname='%s',victimlname='%s',dateofincident='%s',criminalfname='%s',criminallname='%s',crimecommitted='%s',placeofincident='%s'
				WHERE firno='%s' ''' % (uptempvfname,uptempvlname,uptempdate,uptempcfname,uptempclname,uptempcrime,uptempplace,uptempfirno))
		tkinter.messagebox.showinfo("Update FIR","FIR Updated Successfully!")

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------RootViews-----------------------------------------------------------------------------------------------

global root;
root=Tk()
root.title("MUMBAI POLICE");
root.geometry("1350x750+0+0");
root.configure(background='gold');

global image;
global photo;
global label;
image = Image.open("logos1.jpg")
photo = ImageTk.PhotoImage(image)
label=Label(image=photo)
label.image=photo
label.pack()

top1=Frame(root,relief='raise',height=1500,width=1000,bg='gold',bd=3,padx=40,pady=20);
top1.pack(side=TOP);

#----------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------adminViews-----------------------------------------------------------------
def adminview():

	
	global adminview1;
	adminview1=Toplevel(sign1);
	adminview1.geometry('1350x750+0+0');
	adminview1.configure(background='gold');
	Label(adminview1,image=photo).pack()
	top=Frame(adminview1,height=700,width=800,bg='white',bd=15,relief='raise');
	top.pack(side=TOP);

	Button(top,font=('aerial',12,'bold'),text='LODGE FIR',bg='white',bd=7,width=25,pady=10,command=lodgefirview).grid(row=0,column=0)
	Button(top,font=('aerial',12,'bold'),text='VIEW FIR',bg='white',bd=7,width=25,pady=10,command=viewfir).grid(row=1,column=0)
	Button(top,font=('aerial',12,'bold'),text='UPDATE FIR',bg='white',bd=7,width=25,pady=10,command=updatefirview).grid(row=2,column=0)
	Button(top,font=('aerial',12,'bold'),text='EXIT',bg='white',bd=7,width=25,pady=10,command=adminview1.destroy).grid(row=5,column=0)

#Lodge fir
def lodgefirview():
	global lodgefir1;
	lodgefir1=Toplevel();
	lodgefir1.geometry('1350x750+0+0');
	lodgefir1.configure(background='gold');
	Label(lodgefir1,image=photo).pack()
	top=Frame(lodgefir1,height=900,width=900,bg='white',bd=25,relief='raise');
	top.pack(side=TOP);

	#variables
	global fir_no;
	global victim_fname;
	global victim_lname;
	global criminal_fname;
	global criminal_lname;
	global crime_committed;
	global date_of_incident;
	global place_of_incident;
	fir_no=StringVar();
	victim_fname=StringVar();
	victim_lname=StringVar();
	criminal_fname=StringVar();
	criminal_lname=StringVar();
	date_of_incident=StringVar();
	place_of_incident=StringVar();
	crime_committed=StringVar();
	crime_committed.set('Select')
	crimes={'Robbery',
		'Murder',
		'Rape',
		'Half Murder',
                'kidnapping',
                'shoplifting'
		}

	Label(top,font=('aerial',15,'bold'),text="Enter FIR Details",bg='white',bd=7).grid(row=0,column=3)

	#firno
	Label(top,font=('aerial',10,'bold'),text="FIR Number:",bg='white',bd=7).grid(row=2,column=0);
	Entry(top,textvariable=fir_no,bg='white',bd=5).grid(row=3,column=0);

	#victimfname
	Label(top,font=('aerial',10,'bold'),text="Victim First Name:",bg='white',bd=7).grid(row=5,column=0);
	Entry(top,textvariable=victim_fname,bg='white',bd=5).grid(row=6,column=0);

	#victimlname
	Label(top,font=('aerial',10,'bold'),text="Victim Last Name:",bg='white',bd=7).grid(row=8,column=0);
	Entry(top,textvariable=victim_lname,bg='white',bd=5).grid(row=9,column=0);

	#dateofincident
	Label(top,font=('aerial',10,'bold'),text="Date of Incident:",bg='white',bd=7).grid(row=11,column=0);
	DateEntry(top,textvariable=date_of_incident, width=12, background='grey',foreground='white', borderwidth=5, year=2021).grid(row=12,column=0);
	
	#criminalfname
	Label(top,font=('aerial',10,'bold'),text="Criminal First Name:",bg='white',bd=7).grid(row=2,column=4);
	Entry(top,textvariable=criminal_fname,bg='white',bd=5).grid(row=3,column=4);

	#criminallname
	Label(top,font=('aerial',10,'bold'),text="Criminal Last Name:",bg='white',bd=7).grid(row=5,column=4);
	Entry(top,textvariable=criminal_lname,bg='white',bd=5).grid(row=6,column=4);

	#crimecommitted
	Label(top,font=('aerial',10,'bold'),text="Crime Committed:",bg='white',bd=7).grid(row=8,column=4);
	OptionMenu(top,crime_committed,*crimes).grid(row=9,column=4);

	#placeofincident
	Label(top,font=('aerial',10,'bold'),text="Place of Incident:",bg='white',bd=7).grid(row=11,column=4);
	Entry(top,textvariable=place_of_incident,bg='white',bd=5).grid(row=12,column=4);
	#status
	#Label(top,font=('aerial',10,'bold'),text="status:",bg='white',bd=7).grid(row=12,column=4);
	
	

	Button(top,font=('aerial',10,'bold'),text='Lodge',bg='white',bd=5,width=10,command=addfir).grid(row=20,column=0)

	Button(top,font=('aerial',10,'bold'),text='Exit',bg='white',bd=5,width=10,command=lodgefir1.destroy).grid(row=20,column=4)

#View FIR
def viewfir2():
	global viewfir2;
	global fno;
	global fname;
	global lname;
	global findby1;
	global fir_no1;
	global victim_fname1;
	global victim_lname1;
	global criminal_fname1;
	global criminal_lname1;
	global crime_committed1;
	global date_of_incident1;
	global place_of_incident1;
	fir_no1=StringVar();
	victim_fname1=StringVar();
	victim_lname1=StringVar();
	criminal_fname1=StringVar();
	criminal_lname1=StringVar();
	date_of_incident1=StringVar();
	place_of_incident1=StringVar();
	crime_committed1=StringVar();
	fno=StringVar();
	fname=StringVar();
	lname=StringVar();
	findby1=StringVar();
	findby1=findby.get();

	viewfir2=Toplevel();
	viewfir2.geometry('1350x750+0+0');
	viewfir2.configure(background='gold');
	Label(viewfir2,image=photo).pack()
	top=Frame(viewfir2,height=700,width=800,bg='white',bd=25,relief='raise');
	top.pack(side=TOP);
	print(findby1);

	if findby1=='Select':
		tkinter.messagebox.showinfo("Warning!","Please Select An Option!")
		viewfir2.destroy();
	else:
		if findby1=='FIR No.':
			fno=simpledialog.askinteger("View FIR", "Enter FIR No.", parent=viewfir2,minvalue=0,maxvalue=1000)
			if fno is not None:
				cur=conn.cursor();
				cur.execute(''' SELECT firno FROM fir WHERE firno='%s' ''' % (fno))
				if cur.fetchone() is not None:
					cur=conn.cursor();
					cur.execute(''' SELECT * FROM fir WHERE firno='%s' ''' % (fno))
					data=cur.fetchall()
					Button(top,font=('aerial',10,'bold'),text='Exit',bg='white',bd=5,width=10,command=viewfir2.destroy).grid(row=20,column=1)
					for dat in enumerate(data):
						#print(dat)
						fir_no1=dat[1][0];
						victim_fname1=dat[1][1];
						victim_lname1=dat[1][2];
						criminal_fname1=dat[1][4];
						criminal_lname1=dat[1][5];
						crime_committed1=dat[1][6];
						date_of_incident1=dat[1][3];
						place_of_incident1=dat[1][7];
						
						
						
						
					#firno
					Label(top,font=('aerial',10,'bold'),text="FIR Number:",bg='white',bd=7).grid(row=2,column=0);
					Label(top,font=('aerial',10,'bold'),text=fir_no1,bg='white',bd=5).grid(row=2,column=1);
					#victimfname
					Label(top,font=('aerial',10,'bold'),text="Victim First Name:",bg='white',bd=7).grid(row=4,column=0);
					Label(top,font=('aerial',10,'bold'),text=victim_fname1,bg='white',bd=5).grid(row=4,column=1);
					#victimlname
					Label(top,font=('aerial',10,'bold'),text="Victim Last Name:",bg='white',bd=7).grid(row=6,column=0);
					Label(top,font=('aerial',10,'bold'),text=victim_lname1,bg='white',bd=5).grid(row=6,column=1);
					#dateofincident
					Label(top,font=('aerial',10,'bold'),text="Date of Incident:",bg='white',bd=7).grid(row=8,column=0);
					Label(top,font=('aerial',10,'bold'),text=date_of_incident1,bg='white',bd=5).grid(row=8,column=1);
					#criminalfname
					Label(top,font=('aerial',10,'bold'),text="Criminal First Name:",bg='white',bd=7).grid(row=10,column=0);
					Label(top,font=('aerial',10,'bold'),text=criminal_fname1,bg='white',bd=5).grid(row=10,column=1);
					#criminallname
					Label(top,font=('aerial',10,'bold'),text="Criminal Last Name:",bg='white',bd=7).grid(row=12,column=0);
					Label(top,font=('aerial',10,'bold'),text=criminal_lname1,bg='white',bd=5).grid(row=12,column=1);
					#crimecommitted
					Label(top,font=('aerial',10,'bold'),text="Crime Committed:",bg='white',bd=7).grid(row=14,column=0);
					Label(top,font=('aerial',10,'bold'),text=crime_committed1,bg='white',bd=5).grid(row=14,column=1);
					#placeofincident
					Label(top,font=('aerial',10,'bold'),text="Place of Incident:",bg='white',bd=7).grid(row=16,column=0);
					Label(top,font=('aerial',10,'bold'),text=place_of_incident1,bg='white',bd=5).grid(row=16,column=1);
					#status
					#Label(top,font=('aerial',10,'bold'),text="Status:",bg='white',bd=7).grid(row=18,column=0);
					#Label(top,font=('aerial',10,'bold'),text=astatus1,bg='white',bd=7).grid(row=18,column=1);
				else:
					tkinter.messagebox.showinfo("View FIR","FIR No. Does Not Exist!")
					viewfir2.destroy();
		else:
			fname=simpledialog.askstring("View FIR", "Enter Victim's First Name", parent=viewfir2)
			lname=simpledialog.askstring("View FIR", "Enter Victim's Last Name", parent=viewfir2)	
			if fname and lname is not None:
				cur=conn.cursor();
				cur.execute(''' SELECT victimfname FROM fir WHERE victimfname='%s' AND victimlname='%s' ''' % (fname,lname))
				if cur.fetchone() is not None:
					cur=conn.cursor();
					cur.execute(''' SELECT * FROM fir WHERE victimfname='%s' AND victimlname='%s' ''' % (fname,lname))
					data=cur.fetchall()
					Button(top,font=('aerial',10,'bold'),text='Exit',bg='white',bd=5,width=10,command=viewfir2.destroy).grid(row=18,column=1)
					for dat in enumerate(data):
						#print(dat)
						fir_no1=dat[1][0];
						victim_fname1=dat[1][1];
						victim_lname1=dat[1][2];
						criminal_fname1=dat[1][4];
						criminal_lname1=dat[1][5];
						crime_committed1=dat[1][6];
						date_of_incident1=dat[1][3];
						place_of_incident1=dat[1][7];
						
						
						
					#firno
					Label(top,font=('aerial',10,'bold'),text="FIR Number:",bg='white',bd=7).grid(row=2,column=0);
					Label(top,font=('aerial',10,'bold'),text=fir_no1,bg='white',bd=5).grid(row=2,column=1);
					#victimfname
					Label(top,font=('aerial',10,'bold'),text="Victim First Name:",bg='white',bd=7).grid(row=4,column=0);
					Label(top,font=('aerial',10,'bold'),text=victim_fname1,bg='white',bd=5).grid(row=4,column=1);
					#victimlname
					Label(top,font=('aerial',10,'bold'),text="Victim Last Name:",bg='white',bd=7).grid(row=6,column=0);
					Label(top,font=('aerial',10,'bold'),text=victim_lname1,bg='white',bd=5).grid(row=6,column=1);
					#dateofincident
					Label(top,font=('aerial',10,'bold'),text="Date of Incident:",bg='white',bd=7).grid(row=8,column=0);
					Label(top,font=('aerial',10,'bold'),text=date_of_incident1,bg='white',bd=5).grid(row=8,column=1);
					#criminalfname
					Label(top,font=('aerial',10,'bold'),text="Criminal First Name:",bg='white',bd=7).grid(row=10,column=0);
					Label(top,font=('aerial',10,'bold'),text=criminal_fname1,bg='white',bd=5).grid(row=10,column=1);
					#criminallname
					Label(top,font=('aerial',10,'bold'),text="Criminal Last Name:",bg='white',bd=7).grid(row=12,column=0);
					Label(top,font=('aerial',10,'bold'),text=criminal_lname1,bg='white',bd=5).grid(row=12,column=1);
					#crimecommitted
					Label(top,font=('aerial',10,'bold'),text="Crime Committed:",bg='white',bd=7).grid(row=14,column=0);
					Label(top,font=('aerial',10,'bold'),text=crime_committed1,bg='white',bd=5).grid(row=14,column=1);
					#placeofincident
					Label(top,font=('aerial',10,'bold'),text="Place of Incident:",bg='white',bd=7).grid(row=16,column=0);
					Label(top,font=('aerial',10,'bold'),text=place_of_incident1,bg='white',bd=5).grid(row=16,column=1);
					#status
					#Label(top,font=('aerial',10,'bold'),text="Status:",bg='white',bd=7).grid(row=18,column=0);
					#Label(top,font=('aerial',10,'bold'),text=astatus1,bg='white',bd=7).grid(row=18,column=1);
				else:
					tkinter.messagebox.showinfo("View FIR","Victim Does Not Exist!")
					viewfir2.destroy();

def viewfir():
	
	global viewfir1;
	viewfir1=Toplevel();
	viewfir1.geometry('1350x750+0+0');
	viewfir1.configure(background='gold');
	Label(viewfir1,image=photo).pack()
	top=Frame(viewfir1,height=900,width=900,bg='white',bd=25,relief='raise');
	top.pack(side=TOP);

	global findby;
	findby=StringVar();
	findby.set('Select')
	finds={'FIR No.',
		'Victim Name',	
		}
	
	Label(top,font=('aerial',15,'bold'),text="Enter FIR Details",bg='white',bd=7).grid(row=0,column=2)
	
	Label(top,font=('aerial',15,'bold'),text="View FIR By",bg='white',bd=7).grid(row=2,column=2)
	OptionMenu(top,findby,*finds).grid(row=3,column=2);
	
	Button(top,font=('aerial',10,'bold'),text='OK',bg='white',bd=5,width=10,command=viewfir2).grid(row=4,column=0)
	Button(top,font=('aerial',10,'bold'),text='Cancel',bg='white',bd=5,width=10,command=viewfir1.destroy).grid(row=4,column=3)

#Update FIR
def updatefir2():
	global updatefir2;
	updatefir2=Toplevel();
	updatefir2.geometry('1350x750+0+0');
	updatefir2.configure(background='gold');
	Label(updatefir2,image=photo).pack()

	global afindby1;
	global afir_no;
	global avictim_fname;
	global avictim_lname;
	global acriminal_fname;
	global acriminal_lname;
	global acrime_committed;
	global adate_of_incident;
	global aplace_of_incident;
	

	afindby1=StringVar();
	afir_no=StringVar();
	avictim_fname=StringVar();
	avictim_lname=StringVar();
	acriminal_fname=StringVar();
	acriminal_lname=StringVar();
	adate_of_incident=StringVar();
	aplace_of_incident=StringVar();
	acrime_committed=StringVar();
	acrime_committed.set('Select')
	acrimes={'Robbery',
		'Murder',
		'Rape',
		'Half Murder',
                'kidnapping',
                'shoplifting',
		}
	afindby1=afindby.get();

	top=Frame(updatefir2,height=700,width=800,bg='white',bd=25,relief='raise');
	top.pack(side=TOP);
	print("FIR:",afindby1);

	if afindby1=='':
		tkinter.messagebox.showinfo("Warning!","Please Enter FIR No.!")
		updatefir2.destroy();
	else:
		cur=conn.cursor();
		cur.execute(''' SELECT firno FROM fir WHERE firno='%s' ''' % (afindby1))
		if cur.fetchone() is not None:
			cur=conn.cursor();
			cur.execute(''' SELECT * FROM fir WHERE firno='%s' ''' % (afindby1))
			adata=cur.fetchall()
			for adat in enumerate(adata):
				#print(dat)
				afir_no=adat[1][0];

			print("FIR:",afir_no);
			Label(top,font=('aerial',15,'bold'),text="Enter FIR Details to Update",bg='white',bd=7).grid(row=0,column=3)
			#firno
			Label(top,font=('aerial',10,'bold'),text="FIR Number:",bg='white',bd=7).grid(row=2,column=0);
			Label(top,font=('aerial',10,'bold'),text=afir_no,bg='white',bd=5).grid(row=3,column=0);
			#victimfname
			Label(top,font=('aerial',10,'bold'),text="Victim First Name:",bg='white',bd=7).grid(row=5,column=0);
			Entry(top,textvariable=avictim_fname,bg='white',bd=5).grid(row=6,column=0);
			#victimlname
			Label(top,font=('aerial',10,'bold'),text="Victim Last Name:",bg='white',bd=7).grid(row=8,column=0);
			Entry(top,textvariable=avictim_lname,bg='white',bd=5).grid(row=9,column=0);
			#dateofincident
			Label(top,font=('aerial',10,'bold'),text="Date of Incident:",bg='white',bd=7).grid(row=11,column=0);
			DateEntry(top,textvariable=adate_of_incident, width=12, background='grey',foreground='white', borderwidth=5, year=2019).grid(row=12,column=0);
			#criminalfname
			Label(top,font=('aerial',10,'bold'),text="Criminal First Name:",bg='white',bd=7).grid(row=2,column=4);
			Entry(top,textvariable=acriminal_fname,bg='white',bd=5).grid(row=3,column=4);
			#criminallname
			Label(top,font=('aerial',10,'bold'),text="Criminal Last Name:",bg='white',bd=7).grid(row=5,column=4);
			Entry(top,textvariable=acriminal_lname,bg='white',bd=5).grid(row=6,column=4);
			#crimecommitted
			Label(top,font=('aerial',10,'bold'),text="Crime Committed:",bg='white',bd=7).grid(row=8,column=4);
			OptionMenu(top,acrime_committed,*acrimes).grid(row=9,column=4);
			#placeofincident
			Label(top,font=('aerial',10,'bold'),text="Place of Incident:",bg='white',bd=7).grid(row=11,column=4);
			Entry(top,textvariable=aplace_of_incident,bg='white',bd=5).grid(row=12,column=4);
                        #status
			#Label(top,font=('aerial',10,'bold'),text="Status:",bg='white',bd=7).grid(row=13,column=4);
			#Entry(top,textvariable=astatus,bg='white',bd=7).grid(row=14,column=4);

			Button(top,font=('aerial',10,'bold'),text='Update FIR',bg='white',bd=5,width=10,command=updatefir).grid(row=20,column=0)
			Button(top,font=('aerial',10,'bold'),text='Exit',bg='white',bd=5,width=10,command=updatefir2.destroy).grid(row=20,column=4)
		else:
			tkinter.messagebox.showinfo("Update FIR","FIR No. Does Not Exist!")
			updatefir2.destroy();
def updatefirview():
	
	global updatefir1;
	updatefir1=Toplevel();
	updatefir1.geometry('1350x750+0+0');
	updatefir1.configure(background='gold');
	Label(updatefir1,image=photo).pack()
	top=Frame(updatefir1,height=900,width=900,bg='white',bd=25,relief='raise');
	top.pack(side=TOP);

	global afindby;
	afindby=StringVar();

	Label(top,font=('aerial',15,'bold'),text="Update FIR",bg='white',bd=7).grid(row=0,column=2)
	
	Label(top,font=('aerial',15,'bold'),text="Enter FIR No. to Search FIR:",bg='white',bd=7).grid(row=2,column=2)
	Entry(top,textvariable=afindby,bg='white',bd=5).grid(row=3,column=2);
	
	Button(top,font=('aerial',10,'bold'),text='OK',bg='white',bd=5,width=20,command=updatefir2).grid(row=4,column=0)
	Button(top,font=('aerial',10,'bold'),text='Cancel',bg='white',bd=5,width=20,command=updatefir1.destroy).grid(row=4,column=3)


#------------------------------------------------------------------------------------------------------------------------------------------------
#User view
def userview():
	
	global userview1;
	userview1=Toplevel(sign2);
	userview1.geometry('1350x750+0+0');
	userview1.configure(background='gold');
	Label(userview1,image=photo).pack()
	top=Frame(userview1,height=700,width=800,bg='white',bd=5,relief='raise');
	top.pack(side=TOP);

       
	Button(top,font=('aerial',12,'bold'),text='VIEW FIR',bg='white',bd=7,width=25,pady=10,command=viewfir).grid(row=1,column=0)
	Button(top,font=('aerial',12,'bold'),text='LODGE FIR',bg='white',bd=7,width=25,pady=10,command=lodgefirview).grid(row=3,column=0)
	Button(top,font=('aerial',12,'bold'),text='EXIT',bg='white',bd=7,width=25,pady=10,command=userview1.destroy).grid(row=5,column=0)

	
       

#View FIR
def userviewfir1():
	global uviewfir3;
	global ufno;
	global ufname;
	global ulname;
	global ufindby1;
	global ufir_no1;
	global uvictim_fname1;
	global uvictim_lname1;
	global ucriminal_fname1;
	global ucriminal_lname1;
	global ucrime_committed1;
	global udate_of_incident1;
	global uplace_of_incident1;
	ufir_no1=StringVar();
	uvictim_fname1=StringVar();
	uvictim_lname1=StringVar();
	ucriminal_fname1=StringVar();
	ucriminal_lname1=StringVar();
	udate_of_incident1=StringVar();
	uplace_of_incident1=StringVar();
	ucrime_committed1=StringVar();
	ufno=StringVar();
	ufname=StringVar();
	ulname=StringVar();
	ufindby1=StringVar();
	ufindby1=findby.get();

	viewfir3=Toplevel(viewfir2);
	viewfir3.geometry('1350x750+0+0');
	viewfir3.configure(background='gold');
	Label(viewfir3,image=photo).pack()
	top=Frame(viewfir3,height=700,width=800,bg='white',bd=25,relief='raise');
	top.pack(side=TOP);
	print(ufindby1);

	if ufindby1=='Select':
		tkinter.messagebox.showinfo("Warning!","Please Select An Option!")
		viewfir2.destroy();
	else:
		if ufindby1=='FIR No.':
			ufno=simpledialog.askinteger("View FIR", "Enter FIR No.", parent=viewfir3,minvalue=0,maxvalue=1000)
			if ufno is not None:
				cur=conn.cursor();
				cur.execute(''' SELECT firno FROM fir WHERE firno='%s' ''' % (ufno))
				if cur.fetchone() is not None:
					cur=conn.cursor();
					cur.execute(''' SELECT * FROM fir WHERE firno='%s' ''' % (ufno))
					udata=cur.fetchall()
					Button(top,font=('aerial',12,'bold'),text='Exit',bg='white',bd=5,width=10,command=viewfir3.destroy).grid(row=18,column=1)
					for udat in enumerate(udata):
						#print(udat)
						ufir_no1=udat[1][0];
						uvictim_fname1=udat[1][1];
						uvictim_lname1=udat[1][2];
						ucriminal_fname1=udat[1][4];
						ucriminal_lname1=udat[1][5];
						ucrime_committed1=udat[1][6];
						udate_of_incident1=udat[1][3];
						uplace_of_incident1=udat[1][7];
						
					#firno
					Label(top,font=('aerial',12,'bold'),text="FIR Number:",bg='white',bd=7).grid(row=2,column=0);
					Label(top,font=('aerial',12,'bold'),text=ufir_no1,bg='white',bd=5).grid(row=2,column=1);
					#victimfname
					Label(top,font=('aerial',12,'bold'),text="Victim First Name:",bg='white',bd=7).grid(row=4,column=0);
					Label(top,font=('aerial',12,'bold'),text=uvictim_fname1,bg='white',bd=5).grid(row=4,column=1);
					#victimlname
					Label(top,font=('aerial',12,'bold'),text="Victim Last Name:",bg='white',bd=7).grid(row=6,column=0);
					Label(top,font=('aerial',12,'bold'),text=uvictim_lname1,bg='white',bd=5).grid(row=6,column=1);
					#dateofincident
					Label(top,font=('aerial',12,'bold'),text="Date of Incident:",bg='white',bd=7).grid(row=8,column=0);
					Label(top,font=('aerial',12,'bold'),text=udate_of_incident1,bg='white',bd=5).grid(row=8,column=1);
					#criminalfname
					Label(top,font=('aerial',12,'bold'),text="Criminal First Name:",bg='white',bd=7).grid(row=10,column=0);
					Label(top,font=('aerial',12,'bold'),text=ucriminal_fname1,bg='white',bd=5).grid(row=10,column=1);
					#criminallname
					Label(top,font=('aerial',12,'bold'),text="Criminal Last Name:",bg='white',bd=7).grid(row=12,column=0);
					Label(top,font=('aerial',12,'bold'),text=ucriminal_lname1,bg='white',bd=5).grid(row=12,column=1);
					#crimecommitted
					Label(top,font=('aerial',12,'bold'),text="Crime Committed:",bg='white',bd=7).grid(row=14,column=0);
					Label(top,font=('aerial',12,'bold'),text=ucrime_committed1,bg='white',bd=5).grid(row=14,column=1);
					#placeofincident
					Label(top,font=('aerial',12,'bold'),text="Place of Incident:",bg='white',bd=7).grid(row=16,column=0);
					Label(top,font=('aerial',12,'bold'),text=uplace_of_incident1,bg='white',bd=5).grid(row=16,column=1);
				else:
					tkinter.messagebox.showinfo("View FIR","FIR No. Does Not Exist!")
					viewfir3.destroy();
		else:
			fname=simpledialog.askstring("View FIR", "Enter Victim's First Name", parent=viewfir3)
			lname=simpledialog.askstring("View FIR", "Enter Victim's Last Name", parent=viewfir3)	
			if fname and lname is not None:
				cur=conn.cursor();
				cur.execute(''' SELECT victimfname FROM fir WHERE victimfname='%s' AND victimlname='%s' ''' % (ufname,ulname))
				if cur.fetchone() is not None:
					cur=conn.cursor();
					cur.execute(''' SELECT * FROM fir WHERE victimfname='%s' AND victimlname='%s' ''' % (ufname,ulname))
					udata=cur.fetchall()
					Button(top,font=('aerial',10,'bold'),text='Exit',bg='white',bd=5,width=20,command=viewfir3.destroy).grid(row=18,column=1)
					for udat in enumerate(udata):
						#print(dat)
						ufir_no1=udat[1][0];
						uvictim_fname1=udat[1][1];
						uvictim_lname1=udat[1][2];
						ucriminal_fname1=udat[1][4];
						ucriminal_lname1=udat[1][5];
						ucrime_committed1=udat[1][6];
						udate_of_incident1=udat[1][3];
						uplace_of_incident1=udat[1][7];
					#firno
					Label(top,font=('aerial',12,'bold'),text="FIR Number:",bg='white',bd=7).grid(row=2,column=0);
					Label(top,font=('aerial',12,'bold'),text=ufir_no1,bg='white',bd=5).grid(row=2,column=1);
					#victimfname
					Label(top,font=('aerial',12,'bold'),text="Victim First Name:",bg='white',bd=7).grid(row=4,column=0);
					Label(top,font=('aerial',12,'bold'),text=uvictim_fname1,bg='white',bd=5).grid(row=4,column=1);
					#victimlname
					Label(top,font=('aerial',12,'bold'),text="Victim Last Name:",bg='white',bd=7).grid(row=6,column=0);
					Label(top,font=('aerial',12,'bold'),text=uvictim_lname1,bg='white',bd=5).grid(row=6,column=1);
					#dateofincident
					Label(top,font=('aerial',12,'bold'),text="Date of Incident:",bg='white',bd=7).grid(row=8,column=0);
					Label(top,font=('aerial',12,'bold'),text=udate_of_incident1,bg='white',bd=5).grid(row=8,column=1);
					#criminalfname
					Label(top,font=('aerial',12,'bold'),text="Criminal First Name:",bg='white',bd=7).grid(row=10,column=0);
					Label(top,font=('aerial',12,'bold'),text=ucriminal_fname1,bg='white',bd=5).grid(row=10,column=1);
					#criminallname
					Label(top,font=('aerial',12,'bold'),text="Criminal Last Name:",bg='white',bd=7).grid(row=12,column=0);
					Label(top,font=('aerial',12,'bold'),text=ucriminal_lname1,bg='white',bd=5).grid(row=12,column=1);
					#crimecommitted
					Label(top,font=('aerial',12,'bold'),text="Crime Committed:",bg='white',bd=7).grid(row=14,column=0);
					Label(top,font=('aerial',12,'bold'),text=ucrime_committed1,bg='white',bd=5).grid(row=14,column=1);
					#placeofincident
					Label(top,font=('aerial',12,'bold'),text="Place of Incident:",bg='white',bd=7).grid(row=16,column=0);
					Label(top,font=('aerial',12,'bold'),text=uplace_of_incident1,bg='white',bd=5).grid(row=16,column=1);
					#astatus
					#Label(top,font=('aerial',10,'bold'),text="Status:",bg='white',bd=7).grid(row=18,column=0);
					#Label(top,font=('aerial',10),text=astatus,bg='white',bd=7).grid(row=18,column=1);

				else:
					tkinter.messagebox.showinfo("View FIR","Victim Does Not Exist!")
					viewfir3.destroy();

def userviewfir():
	
	global viewfir2;
	viewfir2=Toplevel();
	viewfir2.geometry('2000x1500+0+0');
	viewfir2.configure(background='gold');
	Label(viewfir2,image=photo).pack()
	top=Frame(viewfir2,height=2000,width=2000,bg='white',bd=15,relief='raise');
	top.pack(side=TOP);

	global findby;
	findby=StringVar();
	findby.set('Select')
	finds={'FIR No.',
		'Victim Name',	
		}
	
	Label(top,font=('aerial',15,'bold'),text="Enter FIR Details",bg='white',bd=7).grid(row=0,column=2)
	
	Label(top,font=('aerial',15,'bold'),text="View FIR By",bg='white',bd=7).grid(row=2,column=2)
	OptionMenu(top,findby,*finds).grid(row=3,column=2);
	
	Button(top,font=('aerial',10,'bold'),text='OK',bg='white',bd=5,width=20,command=userviewfir1).grid(row=6,column=0)
	Button(top,font=('aerial',10,'bold'),text='Cancel',bg='white',bd=5,width=20,command=viewfir2.destroy).grid(row=6,column=3)


#------------------------------------------------------------------------------------------------------------------------------------------------


#---------------------------------------------------------------------SignInViews------------------------------------------------------------------

def createacc():
        global createacc1;
        createacc1=Toplevel(root)
        createacc1.geometry('1350x750+0+0');
        createacc1.configure(background='gold');
        Label(createacc1,image=photo).pack()
        top=Frame(createacc1,height=1500,width=1000,bg='white',bd=5,relief='raise');
        top.pack(side=TOP);
        global utempfname
        global utemplname
        global utemploginid
        global utemppass
        utempfname=StringVar();
        utemplname=StringVar();
        utemploginid=StringVar();
        utemppass=StringVar();
        
	
			
        Label(top,font=('aerial',12,'bold'),text="First Name:",bg='white',bd=7).grid(row=2,column=0)
        Entry(top,textvariable=utempfname,bg='white',bd=5).grid(row=2,column=1)

        Label(top,font=('aerial',12,'bold'),text="Last Name:",bg='white',bd=7).grid(row=3,column=0)
        Entry(top,textvariable=utemplname,bg='white',bd=5).grid(row=3,column=1)

        Label(top,font=('aerial',12,'bold'),text="Username:",bg='white',bd=7).grid(row=4,column=0)
        Entry(top,textvariable=utemploginid,bg='white',bd=5).grid(row=4,column=1)

        Label(top,font=('aerial',12,'bold'),text="Password:",bg='white',bd=7).grid(row=5,column=0)
        Entry(top,textvariable=utemppass,bg='white',bd=5,show="*").grid(row=5,column=1)

        b=Button(top,font=('aerial',12,'bold'),text='Confirm',bg='white',bd=5,width=20,command=cacc).grid(row=6,column=0,sticky=W);
	
        Button(top,font=('aerial',12,'bold'),text='Exit',bg='white',bd=5,width=20,command=createacc1.destroy).grid(row=6,column=1);

        
       


def cacc():
        fname=StringVar();
        lname=StringVar();
        username=StringVar();
        password=StringVar();
        fname=utempfname.get();
        lname=utemplname.get();
        username=utemploginid.get();
        password=utemppass.get();
        if fname==''or lname=='' or username=='' or password=='':
                tkinter.messagebox.showinfo("Warning!","One or more fields are empty!")
                

        else: 
                cur=conn.cursor();
                cur.execute(''' SELECT username FROM user WHERE username='%s' ''' % (username))
                if cur.fetchone() is not None:
                        tkinter.messagebox.showinfo("Warning!","Username Already Exists! Try Again!")
                        
                else:
                        cur.execute(''' INSERT INTO user(fname,lname,username,password)
					VALUES('%s','%s','%s','%s') ''' % (fname,lname,username,password))
                        
                        
                        tkinter.messagebox.showinfo("user Account Creation!","New user Added Successfully!")
        
                        



#Admin signin 
def sign1():

	global sign1;
	sign1=Toplevel(root)
	sign1.title("MUMBAI POLICE");
	sign1.geometry("2000x1500+0+0");
	sign1.configure(background='gold');
	Label(sign1,image=photo).pack()
	top1=Frame(sign1,height=1500,width=1000,bg='white',bd=5,relief='raise');
	top1.pack(side=TOP);

	#variables
	global admin_username;
	global admin_password;
	global admin_login;
	admin_username=StringVar();
	admin_password=StringVar();
	admin_login=(admin_username,admin_password);

	Label(top1,font=('aerial',25,'bold'),text="LOGIN",bg='white',bd=7).grid(row=0,column=3)

	Label(top1,font=('aerial',12,'bold'),text="USERNAME:",bg='white',bd=7).grid(row=2,column=0);#username
	Entry(top1,textvariable=admin_username,bg='white',bd=5,width=20).grid(row=2,column=4);

	Label(top1,font=('aerial',12,'bold'),text="PASSWORD:",bg='white',bd=7).grid(row=5,column=0);#password
	Entry(top1,textvariable=admin_password,bg='white',bd=5,show="*",width=20).grid(row=5,column=4);

	b=Button(top1,font=('aerial',12,'bold'),text='SIGN IN',bg='white',bd=7,width=20,command=adminlogin).grid(row=9,column=0,sticky=W);#sign button
	#b.bind(adminlogin(conn)).pack()
	Button(top1,font=('aerial',12,'bold'),text='EXIT',bg='white',bd=6,width=20,command=sign1.destroy).grid(row=9,column=4);#exit

#user signin 
def sign2():

	global sign2;
	sign2=Toplevel(root)
	sign2.title("MUMBAI POLICE");
	sign2.geometry("1350x750+0+0");
	sign2.configure(background='gold');
	Label(sign2,image=photo).pack()
	top1=Frame(sign2,height=700,width=800,bg='white',bd=5,relief='raise');
	top1.pack(side=TOP);

	#variables
	global user_username;
	global user_password;
	global user_login;
	user_username=StringVar();
	user_password=StringVar();
	user_login=(user_username,user_password);

	Label(top1,font=('aerial',25,'bold'),text="USER LOGIN",bg='white',bd=7).grid(row=0,column=3)

	Label(top1,font=('aerial',12,'bold'),text="USERNAME:",bg='white',bd=7).grid(row=2,column=0);#username
	Entry(top1,textvariable=user_username,bg='white',bd=5).grid(row=2,column=4);

	Label(top1,font=('aerial',12,'bold'),text="PASSWORD:",bg='white',bd=7).grid(row=5,column=0);#password
	Entry(top1,textvariable=user_password,bg='white',bd=5,show="*").grid(row=5,column=4);

	b=Button(top1,font=('aerial',12,'bold'),text='SIGN IN',bg='white',bd=7,width=20,command=userlogin).grid(row=9,column=0,sticky=W);#sign button
	#b.bind(userlogin(conn)).pack()
	Button(top1,font=('aerial',10,'bold'),text='EXIT',bg='white',bd=6,width=20,command=sign2.destroy).grid(row=9,column=4);#create account



#Button of Admin,User and user
Button(top1,  font=('aerial',12,'bold'),text='ADMIN', bg='white',bd=7,width=30,command=sign1).grid(row=8, column=0,pady=5);#Admin account
Button(top1,  font=('aerial',12,'bold'),text='USER', bg='white',bd=7,width=30,command=sign2).grid(row=10, column=0,pady=5);#user account
Button(top1,  font=('aerial',12,'bold'),text='EXIT',  bg='white',bd=7,width=30,command=root.destroy).grid(row=14,column=0,pady=10);
Button(top1,  font=('aerial',12,'bold'),text='CREATE ACCOUNT',  bg='white',bd=7,width=30,command=createacc).grid(row=12,column=0,pady=5);



	
#--------------------------------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------LoginFunctions---------------------------------------------------------------------

#Admin Login Function
def adminlogin():
	aname=StringVar();
	apass=StringVar();
	aname=admin_username.get();
	apass=admin_password.get();
	cur=conn.cursor();
	cur.execute(''' SELECT username FROM admin WHERE username='%s' AND password='%s' ''' % (aname,apass))
	if cur.fetchone() is not None:
		adminview()
	else:
		tkinter.messagebox.showinfo("Warning!","Username or Password Incorrect! Try Again!")

#user Login Function
def userlogin():
	fname=StringVar();
	fpass=StringVar();
	fname=user_username.get();
	fpass=user_password.get();
	cur=conn.cursor();
	cur.execute(''' SELECT username FROM user WHERE username='%s' AND password='%s' ''' % (fname,fpass))
	if cur.fetchone() is not None:
		userview()
	else:
		tkinter.messagebox.showinfo("Warning!","Username or Password Incorrect! Try Again!")


#----------------------------------------------------------------------------------------------------------------------------------

root.mainloop()
