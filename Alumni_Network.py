import Tkinter as tk 
from Tkinter import * 
import tkMessageBox


class Alumni_Network(tk.Tk) : 
	def __init__(self,*args,**kwargs):
		tk.Tk.__init__(self,*args,**kwargs) # for the super class
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
	def open_message_box(self):
		tkMessageBox.showinfo("Invalid Entry","Enter Again")
		regn_no.delete(0, END)

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
		submit = tk.Button(self,text = "Submit",command = lambda : self.storedata(bdate_var.get(),regn_no_var.get()) )
		submit.grid(row = 7, sticky = E)
		Label(self,text = 'If Not registered',width = 40).grid(row = 10,column = 0,sticky = W)
		register = tk.Button(self,text = "Register",command = lambda: controller.show_frame(StudentRegister))
		register.grid(row = 10, sticky = SE)	
		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 12, sticky = E)	

	def storedata(self,bd,rn):
		if len(bd) == 10:
			if bd[2]!='/' or bd[5]!='/' or int(bd[6:]) < 2010 or rn%100000000 < 0 : 
				self.open_message_box()
		else :
			self.open_message_box()	
		#CODE TO LOGIN, DEPENDING ON THE DATABASE, i.e. EXECUTE QUERY FOR THESE PRIMARY KEYS, AND OPEN THE STUDENT PAGE..
	def open_message_box(self):
		tkMessageBox.showinfo("Invalid Entry","Enter Again")
		regn_no.delete(0, END)

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

		submit =Button(self,text = "Submit",command = lambda: self.storedata(username_var.get(),pass_var.get()) )
		submit.grid(row = 7, sticky = E)

		Label(self,text = 'If Not registered',width = 40).grid(row = 10,column = 0,sticky = W)
		register = Button(self,text = "Register",command = lambda: controller.show_frame(AlumniRegister))
		register.grid(row = 10, sticky = SE)	

		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 12, sticky = E)	


	def storedata(self,us,pa):
		if len(us) == 0 :
			self.open_message_box()
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

		submit =tk.Button(self,text = "Submit",command = lambda: self.storedata(controller))
		submit.grid(row = 13, sticky = W)
		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(StudentPage))
		back.grid(row = 13, sticky = E)	
	def storedata(self,controller): 
		#code to check for constraints and store the data 
		controller.show_frame(StudentFinal)

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

		submit =tk.Button(self,text = "Submit",command = lambda: self.storedata(controller))
		submit.grid(row = 13, sticky = E)

		back = tk.Button(self,text ="Go Back",command = lambda: controller.show_frame(AlumniPage))
		back.grid(row = 12, sticky = E)	

	def storedata(self,controller): 
		#code to check for constraints and store the data 
		controller.show_frame(AlumniFinal)

class StudentFinal(tk.Frame) :
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		
		Label(self,text = ' Birth Date ').grid(row = 1,sticky = W,padx = 4)
		bd_var = StringVar()
		bdate = Entry(self,textvariable = bd_var)
		bdate.grid(row = 1,column = 1, sticky = E,pady = 4)

		Label(self,text = ' Branch ').grid(row = 2,sticky = W,padx = 4)
		branch_var = StringVar()
		branch = Entry(self,textvariable = branch_var)
		branch.grid(row = 2,column = 1,pady = 4)

		Label(self,text = ' GPA ').grid(row = 2,column = 5,sticky = W,padx = 4)
		gpa_var = StringVar() # needs to be changed, to float while passing
		gpa = Entry(self,textvariable = gpa_var)
		gpa.grid(row = 2,column = 6, sticky = E,pady = 4)

		Label(self,text = ' Link to CV ').grid(row = 3,sticky = W,padx = 4)
		cv_var = StringVar()
		cv = Entry(self,textvariable = cv_var)
		cv.grid(row = 3,column = 1, sticky = E,pady = 4)

		Label(self,text = ' Email Address ' ).grid(row = 4,sticky = W,padx = 4)
		email_var = StringVar()
		email = Entry(self,textvariable = email_var)
		email.grid(row = 4,column = 1, sticky = E,pady = 4)

		updateinfo = tk.Button(self,text = " Update Profile ",command = self.quit) # to be written later
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
		
		searchinfo = tk.Button(self,text = " Search ",command = self.quit) # to be written later
		searchinfo.grid(row = 10,sticky = W)		

		back = tk.Button(self,text ="Log Out",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 14, sticky = E)	


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

		updateinfo = tk.Button(self,text = " Update Profile ",command = self.quit) # to be written later
		updateinfo.grid(row = 5,sticky = W)		

		back = tk.Button(self,text ="Log Out",command = lambda: controller.show_frame(StartPage))
		back.grid(row = 12, sticky = E)	

app = Alumni_Network()
app.mainloop()