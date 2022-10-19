from import_file import *

class DisplayContact(Toplevel):
	def __init__(self,record_entry):
		Toplevel.__init__(self)
		self.geometry('700x680+50+0')
		self.title('Phone Book-Update Contact')
		self.resizable(False,False)

		#frames 
		self.top = Frame(self, height=200,bg='#f0d986')
		self.top.pack(fill=X)
		self.bottom = Frame(self, height=480,bg='#ebc334')
		self.bottom.pack(fill=X)

		#top frame design
		self.topImg = PhotoImage(file="icons/myContact.png")
		self.topImgLabel = Label(self.top, image=self.topImg,bg='#f0d986')
		self.topImgLabel.place(x=140,y=50)

		#heading
		self.topHeading = Label(self.top, text='  PERSONAL INFO  ', font='arial 25 bold', bg='#ebc334')
		self.topHeading.place(x=300,y=70)

		#....display query.....
		query = 'select * from directory where f_name="{}" and s_name="{}"'.format(record_entry[2], record_entry[3])
		result = cur.execute(query).fetchone()


		#..................entries....................


		#First name
		self.label_fname = Label(self.bottom, text=' First Name ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_fname.place(x=50, y=50)

		self.entry_fname = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_fname.insert(0,result[1])
		self.entry_fname.config(state='disabled')
		self.entry_fname.place(x=330, y=50)

		#Last name
		self.label_lname = Label(self.bottom, text=' Last Name ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_lname.place(x=50, y=100)

		self.entry_lname = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_lname.insert(0,result[2])
		self.entry_lname.config(state='disabled')
		self.entry_lname.place(x=330, y=100)

		#Phone No
		self.label_mobNo = Label(self.bottom, text=' Mobile No ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_mobNo.place(x=50, y=150)

		self.entry_mobNo = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_mobNo.insert(0,result[3])
		self.entry_mobNo.config(state='disabled')
		self.entry_mobNo.place(x=330, y=150)

		#Email
		self.label_email = Label(self.bottom, text=' Email Id ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_email.place(x=50, y=200)

		self.entry_email = Entry(self.bottom, font='arial 12', width=30, bd=4)
		self.entry_email.insert(0,result[4])
		self.entry_email.config(state='disabled')
		self.entry_email.place(x=330, y=200)

		#Address
		self.label_address = Label(self.bottom, text=' Address ', font='arial 15 bold', bg='#f0d986', width=20)
		self.label_address.place(x=50, y=250)

		self.entry_address = Text(self.bottom, font='arial 12', width=30, height=7, bd=4)
		self.entry_address.insert(1.0,result[5])
		self.entry_address.config(state='disabled')
		self.entry_address.place(x=330, y=250)








