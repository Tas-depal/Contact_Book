from import_file import*
class AddContact(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.geometry('700x680+50+0')
		self.title('Phone Book-Add Contact')
		self.resizable(False,False)

		#frames 
		self.top = Frame(self, height=200,bg='#f0d986')
		self.top.pack(fill=X)
		self.bottom = Frame(self, height=480,bg='#ebc334')
		self.bottom.pack(fill=X)

		#top frame design
		self.topImg = PhotoImage(file="icons/addContact.png")
		self.topImgLabel = Label(self.top, image=self.topImg,bg='#f0d986')
		self.topImgLabel.place(x=140,y=50)

		#heading
		self.topHeading = Label(self.top, text='  Add Contact  ', font='arial 25 bold', bg='#ebc334')
		self.topHeading.place(x=300,y=70)

		#..................entries....................

		#First name
		self.label_fname = Label(self.bottom, text=' First Name ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_fname.place(x=50, y=50)

		self.entry_fname = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_fname.place(x=330, y=50)

		#Last name
		self.label_lname = Label(self.bottom, text=' Last Name ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_lname.place(x=50, y=100)

		self.entry_lname = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_lname.place(x=330, y=100)

		#Phone No
		self.label_mobNo = Label(self.bottom, text=' Mobile No ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_mobNo.place(x=50, y=150)

		self.entry_mobNo = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_mobNo.place(x=330, y=150)

		#Email
		self.label_email = Label(self.bottom, text=' Email Id ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_email.place(x=50, y=200)

		self.entry_email = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_email.place(x=330, y=200)

		#Address
		self.label_address = Label(self.bottom, text=' Address ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_address.place(x=50, y=250)

		self.entry_address = Text(self.bottom, font='arial 12', width=30, height=7, bd=4)
		self.entry_address.place(x=330, y=250)

		#add button 
		addBtn=Button(self.bottom, text=' ADD ', width=10, font='arial 18 bold', bg='#f0d986', command=self.add_people)
		addBtn.place(x=270, y=420)


	def add_people(self):
		fName = self.entry_fname.get().upper()
		lName = self.entry_lname.get().upper()
		mobNo = self.entry_mobNo.get()
		email = self.entry_email.get()
		address = self.entry_address.get(1.0,'end-1c').upper()

		if fName and lName and mobNo and email and address !="":
			try:
				# Pass data to database
				query = "insert into 'directory' (f_name, s_name, mobNo, email, address) values (?,?,?,?,?);"
				cur.execute(query, (fName, lName, mobNo, email, address));
				con.commit()
				messagebox.showinfo('SUCCESS','Contact added successfully!!')
				self.destroy()

			except Exception as e:
				messagebox.showerror('ERROR',str(e))

		else:
			messagebox.showerror('ERROR','Fill all the fields!!',icon='warning')


