import Tkinter as tk 
from Tkinter import * 
import tkMessageBox
import sqlite3 
import atexit
import time

conn = sqlite3.connect('datastored.db')
studentregn = 0
def closer() :
	print " Ending the Application "
	conn.close()
atexit.register(closer)
#change self.quit to a method which also closes the database. 

class Alumni_Network(tk.Tk) : 
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs) # for the super class
		global alumniuser;
		alumniuser = StringVar()
		container = tk.Frame(self) 		#Contains all the components of a window
		container.pack(side = "top",fill = "both",expand = True)
		container.grid_rowconfigure(0,weight =1)
		container.grid_columnconfigure(0,weight =1)
		self.frames = {} # specifies the frames that we have 
		for F in (StartPage,StudentPage,AlumniPage,StudentRegister,AlumniRegister,StudentFinal,AlumniFinal) :
			frame = F(container,self)
			self.frames[F] = frame ; 
			frame.grid(row = 0,column = 0,sticky = "nsew")
		self.show_frame(StartPage)
	def show_frame(self,cont) :
		frame = self.frames[cont] # show the frame, passed
		frame.tkraise()			#built in functionality which allows that	
class StartPage(tk.Frame) : 
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)#initializing the parent
		Label(self,text = "Welcome to the Alumni-Student relations portal").grid(row = 1,pady = 20,padx = 20)
		stud = tk.Button(self,text = " Enter as STUDENT ",command= lambda:controller.show_frame(StudentPage))	
		stud.grid(row = 5,column = 8,sticky = W)
		alum = tk.Button(self,text = " Enter as ALUMNI ",command = lambda:controller.show_frame(AlumniPage))
		alum.grid(row = 7,column = 8)
		quit = tk.Button(self,text = " EXIT Application ",command = self.quit)
		quit.grid(row = 10,column = 8)

class StudentPage(tk.Frame) : 
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		
		Label(self,text = 'Registration Number').grid(row = 5,sticky = W,padx = 4)
		regn_no_var = IntVar()
		regn_no = Entry(self,textvariable = regn_no_var)
		regn_no.grid(row = 5,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Birth Date').grid(row = 6,sticky = W,padx = 4)
		bdate_var = StringVar()
		bdate = Entry(self,textvariable = bdate_var)
		bdate.grid(row = 6,column = 1, sticky = E,pady = 4)
		
		submit = tk.Button(self,text = "Submit",command = lambda : self.storedata(controller,bdate_var.get(),regn_no_var.get()) )
		submit.grid(row = 7, sticky = E)
		
		Label(self,text = 'If Not registered',width = 40).grid(row = 10,column = 0,sticky = W)
		register = tk.Button(self,text = "Register",command = lambda: controller.show_frame(StudentRegister))
		register.grid(row = 10, sticky = SE)	
		
		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 12, sticky = E)	

	def storedata(self,controller,bd,rn):
		cur = conn.execute('select name from STUDENT where REGN_NO = ?',(rn,))
		i = 0 
		for row in cur : 
			i = i+1 
		if len(bd) == 10:
			if bd[2]!='/' or bd[5]!='/' or int(bd[6:]) > 2010 : 
				self.open_message_box()
			elif i == 0 : 
				 self.open_message_box()
			else : 
				studentregn = rn 
				controller.show_frame(StudentFinal)
		else :
			self.open_message_box()	
		#CODE TO LOGIN, DEPENDING ON THE DATABASE, i.e. EXECUTE QUERY FOR THESE PRIMARY KEYS, AND OPEN THE STUDENT PAGE..
	def open_message_box(self):
		tkMessageBox.showinfo("Invalid Entry","Enter Again")

class AlumniPage(tk.Frame) : 
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		Label(self,text = 'Username').grid(row = 5,sticky = W,padx = 4)
		username_var = StringVar()
		username = Entry(self,textvariable = username_var)
		username.grid(row = 5,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Password').grid(row = 6,sticky = W,padx = 4)
		pass_var = StringVar()
		password= Entry(self,textvariable = pass_var)
		password.grid(row = 6,column = 1, sticky = E,pady = 4)

		submit =Button(self,text = "Submit",command = lambda: self.storedata(controller,username_var.get(),pass_var.get()) )
		submit.grid(row = 7, sticky = E)

		Label(self,text = 'If Not registered',width = 40).grid(row = 10,column = 0,sticky = W)
		register = Button(self,text = "Register",command = lambda: controller.show_frame(AlumniRegister))
		register.grid(row = 10, sticky = SE)	

		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 12, sticky = E)	


	def storedata(self,controller,us,pa):
		cur = conn.execute('select name from ALUMNI where username = ?',(us,))
		i = 0 
		for row in cur : 
			i = i+1 
		if i==0  : # sort of
			self.open_message_box()
		else :
			alumniuser.set(us)
			controller.show_frame(AlumniFinal)
			#CODE TO LOGIN, EXECUTE QUERY FOR THESE PRIMARY KEYS, AND OPEN the Alumni page.

	def open_message_box(self):
		tkMessageBox.showinfo("Invalid Entry","Enter Again")

class StudentRegister(tk.Frame) :
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		Label(self,text = 'Enter Registration Number').grid(row = 1,sticky = W,padx = 4)
		regn_var = IntVar()
		regn_no = Entry(self,textvariable = regn_var)
		regn_no.grid(row = 1,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Birth Date').grid(row = 3,sticky = W,padx = 4)
		bd_var = StringVar()
		bdate = Entry(self,textvariable = bd_var)
		bdate.grid(row = 3,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Name        ').grid(row = 4,sticky = W,padx = 4)
		name_var = StringVar()
		name = Entry(self,textvariable = name_var)
		name.grid(row = 4,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Branch').grid(row = 5,sticky = W,padx = 4)
		branch_var = StringVar()
		branch = Entry(self,textvariable = branch_var)
		branch.grid(row = 5,column = 1, sticky = E,pady = 4)

		Label(self,text = ' Enter GPA ').grid(row = 7,sticky = W,padx = 4)
		gpa_var = StringVar() # needs to be changed, to float while passing
		gpa = Entry(self,textvariable = gpa_var)
		gpa.grid(row = 7,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Link to CV').grid(row = 9,sticky = W,padx = 4)
		cv_var = StringVar()
		cv = Entry(self,textvariable = cv_var)
		cv.grid(row = 9,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Email Address').grid(row = 11,sticky = W,padx = 4)
		email_var = StringVar()
		email = Entry(self,textvariable = email_var)
		email.grid(row = 11,column = 1, sticky = E,pady = 4)

		submit =tk.Button(self,text = "Submit",command = lambda: self.storedata(controller,regn_var.get(),bd_var.get(),name_var.get(),branch_var.get(),gpa_var.get(),cv_var.get(),email_var.get()))
		submit.grid(row = 13, sticky = W)
		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(StudentPage))
		back.grid(row = 13, sticky = E)	
	
	def storedata(self,controller,rn,bd,n,b,g,l2cv,e): 
		try : 
			conn.execute("insert into STUDENT values (?,?,?,?,?,?,?)",(rn,bd,n,b,e,l2cv,g))
			conn.commit()
			studentregn = rn 
			controller.show_frame(StudentFinal)
			#c = conn.execute('select bdate,branch,cv_link,email_add,gpa from STUDENT where regn_no = ?',(studentregn,))
			"""for row in c : 
				bd_var.set(row[0].encode('ascii','ignore'))
				branch_var.set(row[1].encode('ascii','ignore'))
				cv_var.set(row[2].encode('ascii','ignore'))
				email_var.set(row[3].encode('ascii','ignore'))
				gpa_var.set(str(row[4]))"""
		except : 
			self.open_message_box()
		
	def open_message_box(self):
		tkMessageBox.showinfo(" Invalid Entry "," Enter Credentials properly ")

class AlumniRegister(tk.Frame) :
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		Label(self,text = 'Enter Username').grid(row = 1,sticky = W,padx = 4)		
		username_var = StringVar()
		username = Entry(self,textvariable = username_var)
		username.grid(row = 1,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Password').grid(row = 3,sticky = W,padx = 4)
		pass_var = StringVar()
		password = Entry(self,textvariable = pass_var)
		password.grid(row = 3,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Name').grid(row = 4,sticky = W,padx = 4)
		name_var = StringVar()
		name = Entry(self,textvariable = name_var)
		name.grid(row = 4,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Field of Work').grid(row = 5,sticky = W,padx = 4)
		field_var = StringVar()
		field = Entry(self,textvariable = field_var)
		field.grid(row = 5,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Company Name -').grid(row = 7,sticky = W,padx = 4)
		comp_var = StringVar()
		company = Entry(self,textvariable = comp_var)
		company.grid(row = 7,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Position at the company').grid(row = 9,sticky = W,padx = 4)
		pos_var = StringVar()
		position = Entry(self,textvariable = pos_var)
		position.grid(row = 9,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Enter Email Address').grid(row = 11,sticky = W,padx = 4)
		email_var = StringVar()
		email = Entry(self,textvariable = email_var)
		email.grid(row = 11,column = 1, sticky = E,pady = 4)

		submit =tk.Button(self,text = "Submit",command = lambda: self.storedata(controller,username_var.get(),pass_var.get(),name_var.get(),field_var.get(),comp_var.get(),pos_var.get(),email_var.get()))
		submit.grid(row = 13, sticky = E)

		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(AlumniPage))
		back.grid(row = 12, sticky = E)	

	def storedata(self,controller,u,p,n,f,c,po,e): 
		try: 
			conn.execute("insert into ALUMNI values (?,?,?,?,?,?,?)",(u,p,n,f,c,po,e))
			conn.commit()
			alumniuser.set(u)
			controller.show_frame(AlumniFinal)
		except : 
			self.open_message_box()

	def open_message_box(self):
		tkMessageBox.showinfo(" Invalid Entry "," Enter Credentials properly ")

class StudentFinal(tk.Frame) :
	text_results = " No results to show "
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		
		Label(self,text = ' Birth Date ').grid(row = 1,sticky = W,padx = 4)
		global bd_var ; 
		bd_var = StringVar()
		bdate = Entry(self,textvariable = bd_var)
		bdate.grid(row = 1,column = 1, sticky = E,pady = 4)

		Label(self,text = ' Branch ').grid(row = 2,sticky = W,padx = 4)
		global branch_var; 
		branch_var = StringVar()
		branch = Entry(self,textvariable = branch_var)
		branch.grid(row = 2,column = 1,pady = 4)

		Label(self,text = ' GPA ').grid(row = 2,column = 5,sticky = W,padx = 4)
		global gpa_var; 
		gpa_var = StringVar() # needs to be changed, to float while passing
		gpa = Entry(self,textvariable = gpa_var)
		gpa.grid(row = 2,column = 6, sticky = E,pady = 4)

		Label(self,text = ' Link to CV ').grid(row = 3,sticky = W,padx = 4)
		global cv_var
		cv_var = StringVar()
		cv = Entry(self,textvariable = cv_var)
		cv.grid(row = 3,column = 1, sticky = E,pady = 4)

		Label(self,text = ' Email Address ' ).grid(row = 4,sticky = W,padx = 4)
		global email_var 
		email_var = StringVar()
		email = Entry(self,textvariable = email_var)
		email.grid(row = 4,column = 1, sticky = E,pady = 4)

		updateinfo = tk.Button(self,text = " Update Profile ",command = lambda :self.updateinfo(bd_var.get(),branch_var.get(),gpa_var.get(),cv_var.get(),email_var.get(),result))
		updateinfo.grid(row = 5,sticky = W)

		Label(self,text = ' Field ').grid(row = 7,sticky = W,padx = 4)
		field_var = StringVar()
		field = Entry(self,textvariable = field_var)
		field.grid(row = 7,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Company Name -').grid(row = 8,sticky = W,padx = 4)
		comp_var = StringVar()
		company = Entry(self,textvariable = comp_var)
		company.grid(row = 8,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Position in the company').grid(row = 9,sticky = W,padx = 4)
		pos_var = StringVar()
		position = Entry(self,textvariable = pos_var)
		position.grid(row = 9,column = 1, sticky = E,pady = 4)
		
		searchinfo = tk.Button(self,text = " Search ",command = lambda : self.search_info(field_var.get(),comp_var.get(),pos_var.get(),result)) # to be written later
		searchinfo.grid(row = 10,sticky = W)		

		back = tk.Button(self,text ="Log Out",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 14, sticky = E)	

		result = Text(self,height = 4, width = 40)
		result.grid(row = 16,sticky = S)
		#sc = Scrollbar(self).grid(row = 16,sticky = E)
		#sc.config(command= result.yview)
		#result.config(yscrollcommand = sc.set)
		result.insert(END,self.text_results)
	def updateinfo(self,bd,b,g,l2cv,e,result) : 
		try : 
			conn.execute('update STUDENT set bdate = ?,branch = ?,gpa = ?,cv_link = ?,email_add = ? where regn_no = ?',(bd,b,g,l2cv,e,studentregn))
			conn.commit()
			self.insert_in_text(result," Updated Successfully ")
		except : 
			print "Failed update"
	def search_info(self,f,co,p,result) : 
		try : 
			if len(f) == 0 : 
				if len(co) == 0 : 
					if len(p) == 0 : 
					 	self.open_message_box()
					else : 
						c = conn.execute('select name,email_add from ALUMNI where position = ?',(p,))
						self.create_text(c,result)
				elif len(p) == 0: 
					c = conn.execute('select name,email_add from ALUMNI where company = ?',(co,))
					self.create_text(c,result)
				else : 
					c = conn.execute('select name,email_add from ALUMNI where company = ? and position = ?',(co,p)) 
					self.create_text(c,result)
			elif len(co) == 0 : 
				if len(p) == 0 : 
					c = conn.execute('select name,email_add from ALUMNI where field = ?',(f,))
					self.create_text(c,result)
				else : 
					c = conn.execute('select name,email_add from ALUMNI where field = ? and position = ?',(f,p))
					self.create_text(c,result)
			else : 
				if len(p) == 0 : 
					c = conn.execute('select name,email_add from ALUMNI where field = ? and company = ?',(f,co))
					self.create_text(c,result)
				else : 
					c = conn.execute('select name,email_add from ALUMNI where field = ? and company = ? and position = ?',(f,co,p)) 
					self.create_text(c,result)
		except : 
			self.open_message_box()
	def insert_in_text(self,result,tr):
		result.delete(1.0,END)
		result.insert(END,tr)
	def create_text(self,cursor,result) : 
		tr = ""
		for row in cursor : 
			tr = tr + row[0].encode('ascii','ignore') + " - " + row[1].encode('ascii','ignore') 
			tr = tr + "\n"
		self.insert_in_text(result,tr)
	def open_message_box(self):
		tkMessageBox.showinfo(" Invalid Entry "," Enter Credentials properly ")

class AlumniFinal(tk.Frame) :
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)

		Label(self,text = 'Position in the company').grid(row = 1,sticky = W,padx = 4)
		pos_var = StringVar()
		position = Entry(self,textvariable = pos_var)
		position.grid(row = 1,column = 1, sticky = E,pady = 4)

		Label(self,text = ' Field ').grid(row = 2,sticky = W,padx = 4)
		field_var = StringVar()
		field = Entry(self,textvariable = field_var)
		field.grid(row = 2,column = 1, sticky = E,pady = 4)

		Label(self,text = 'Company Name -').grid(row = 3,sticky = W,padx = 4)
		comp_var = StringVar()
		company = Entry(self,textvariable = comp_var)
		company.grid(row = 3,column = 1, sticky = E,pady = 4)

		Label(self,text = ' Email Address ' ).grid(row = 4,sticky = W,padx = 4)
		email_var = StringVar()
		email = Entry(self,textvariable = email_var)
		email.grid(row = 4,column = 1, sticky = E,pady = 4)

		updateinfo = tk.Button(self,text = " Update Profile ",command = lambda :self.update_info(pos_var.get(),field_var.get(),comp_var.get(),email_var.get(),result)) # to be written later
		updateinfo.grid(row = 5,sticky = W)		

		back = tk.Button(self,text ="Log Out",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 12, sticky = E)	
		result = Text(self,height = 4, width = 40)
		result.grid(row = 16,sticky = S)
		result.insert(END," Status Window ")

	def update_info(self,p,f,c,e,re) : 
		try : 
			conn.execute('update ALUMNI set field = ?,company = ?,position = ?,email_add = ? where username = ?',(f,c,p,e,alumniuser.get()))
			conn.commit()
			re.delete(1.0,END)
			re.insert(END," Updated ")

		except : 
			print "Failed update"

app = Alumni_Network()
app.mainloop()
