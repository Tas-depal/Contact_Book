from import_file import *

class ViewContact(Toplevel):
	def __init__(self):
		Toplevel.__init__(self)
		self.title("Phone Book-View Contact")
		self.geometry("700x680+50+0")
		self.resizable(False,False)

		#frames 
		self.top = Frame(self, height=200,bg='#f0d986')
		self.top.pack(fill=X)
		self.bottom = Frame(self, height=480,bg='#ebc334')
		self.bottom.pack(fill=X)

		#top frame design
		self.topImg = PhotoImage(file="icons/myContact.png")
		self.topImgLabel = Label(self.top, image=self.topImg,bg='#f0d986')
		self.topImgLabel.place(x=120,y=30)

		#heading
		self.topHeading = Label(self.top, text='  My Contacts  ', font='arial 25 bold',fg='black',bg='#ebc334')
		self.topHeading.place(x=300,y=70)

		#searchbar
		self.search = PhotoImage(file="icons/search.png")
		self.searchImgLabel = Label(self.bottom, image=self.search, bg='white')
		self.searchImgLabel.place(x=10,y=7.5)
		self.search_entry = Entry(self.bottom, font='arial 12', width=30, bd=1)
		self.search_entry.place(x=32, y=7)

		#search button 
		searchBtn=Button(self.bottom, text=' SEARCH ', width=10, font='arial 10 bold', bg='#f0d986', command=self.search_Contact)
		searchBtn.place(x=320, y=7)


		#list
		self.list = Listbox(self.bottom, width=50, height=20, font='arial 13', selectbackground='#ebc334')
		self.list.grid(row=0, column=0, padx=(10,10),pady=(64),sticky=N)

		#verticalscroll
		self.scroll = Scrollbar(self.bottom, orient=VERTICAL)
		self.scroll.grid(row=0, column=1, sticky=N+S, pady=(64)) 
		self.scroll.config(command=self.list.yview)
		self.list.config(yscrollcommand=self.scroll.set)

		count=0
		#....display query.....
		for ch in range(65,91):
			persons = cur.execute("select * from directory where f_name like '{}%' order by f_name asc;".format(chr(ch))).fetchall()
			if persons==[]:
				continue
			
			self.list.insert(count, " "+chr(ch))
			self.list.itemconfig(count,fg='orange')
			count+=1
			self.list.insert(count, " ")

			count+=1
			for person in persons:				
				self.list.insert(count, " " + " " +person[1]+" "+person[2])
				count+=1
				self.list.insert(count, " ")
				count+=1


		#-----------------------BUTTONS----------------------

		#add button 
		addBtn=Button(self.bottom, text=' ADD ', width=10, font='arial 18 bold', bg='#f0d986', command=self.add_Contact)
		addBtn.grid(row=0, column=2, padx=10, pady=70, sticky=N)
		#update button 
		updateBtn=Button(self.bottom, text=' UPDATE ', width=10, font='arial 18 bold', bg='#f0d986',command=self.update_Contact)
		updateBtn.grid(row=0, column=2, padx=10, pady=130, sticky=N)

		#display button 
		dispBtn=Button(self.bottom, text=' DISPLAY ', width=10, font='arial 18 bold', bg='#f0d986',command=self.display_Contact)
		dispBtn.grid(row=0, column=2, padx=10, pady=190, sticky=N)

		#delete button 
		delBtn=Button(self.bottom, text=' DELETE ', width=10, font='arial 18 bold', bg='#f0d986', command=self.del_Contact)
		delBtn.grid(row=0, column=2, padx=10, pady=250, sticky=N)


	def add_Contact(self):
		add_contact=AddContact()
		self.destroy()

	def search_Contact(self):
		self.list.delete(0, END)
		searchEntry= self.search_entry.get()
		if searchEntry:
			persons = cur.execute('select * from directory where (f_name|| " "|| s_name) like "%{}%" or f_name like "%{}%" or s_name like "%{}%" or mobNo like "%{}%" ;'.format(searchEntry,searchEntry, searchEntry, searchEntry)).fetchall()
			persons.sort(key=lambda x:x[1])
			count=0
			i=1
			if persons == []:
				self.list.insert(0,"No Records found...")
			else:
				for person in persons:
					
					self.list.insert(count, " " + " " +person[1]+" "+person[2])
					count+=1
					i+=1

		else:
			_count=0
			#....display query.....
			for ch in range(65,91):
				persons = cur.execute("select * from directory where f_name like '{}%' order by f_name asc;".format(chr(ch))).fetchall()
				if persons==[]:
					continue
				
				self.list.insert(_count, chr(ch))
				_count+=1
				for person in persons:				
					self.list.insert(_count, " " + " " +person[1]+" "+person[2])
					_count+=1
        

	def update_Contact(self):
		selected_record = self.list.curselection()
		record = self.list.get(selected_record)
		record_entry = record.split(" ")
		update_contact=UpdateContact(record_entry)
		self.destroy()

	def display_Contact(self):
		selected_record = self.list.curselection()
		record = self.list.get(selected_record)
		record_entry = record.split(" ")
		display_contact=DisplayContact(record_entry)
		self.destroy()

	def del_Contact(self):
		selected_record = self.list.curselection()
		record = self.list.get(selected_record)
		record_entry = record.split(" ")
		answer = askyesno(title='confirmation', message='Are you sure that you want to delete the contact?')
		if answer:
			del_query = cur.execute('delete from directory where f_name="{}" and s_name="{}"'.format(record_entry[2], record_entry[3])).fetchone()
			con.commit()
			self.destroy()

