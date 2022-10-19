from import_file import *

class App(object):
	def __init__(self,master):
		self.master=master

		#frames 
		self.top=Frame(master, height=200,bg='#f0d986')
		self.top.pack(fill=X)
		self.bottom=Frame(master, height=350,bg='#ebc334')
		self.bottom.pack(fill=X)

		#top frame design
		self.topImg=PhotoImage(file="icons/phonebook.png")
		self.topImgLabel=Label(self.top, image=self.topImg, bg='#f0d986')
		self.topImgLabel.place(x=100,y=50)

		self.topHeading=Label(self.top, text='  Phone Book  ', font='arial 25 bold',fg='black',bg='#ebc334')
		self.topHeading.place(x=300,y=70)

		self.date=Label(self.top, text=date, font='arial 12  bold italic',fg='black',bg='#f0d986')
		self.date.place(x=595,y=0)

		#bottom frame design

        #button1:View Contact
		self.viewBtn=Button(self.bottom, text=' VIEW CONTACTS ', width=17, font='arial 18 bold', bg='#f0d986', command=self.view_Contact)
		self.viewBtn.place(x=232,y=80)

        #button2:Add Contact
		self.addBtn=Button(self.bottom, text=' ADD CONTACT ', width=17, font='arial 18 bold', bg='#f0d986', command=self.add_Contact)
		self.addBtn.place(x=232,y=170)

	def view_Contact(self):
		view_contact=ViewContact()

	def add_Contact(self):
	    add_contact=AddContact()

def main():
	root = Tk()
	app = App(root)
	root.title("Phone Book")
	root.geometry("700x550+50+0")
	root.resizable(False,False)
	root.mainloop()
if __name__=='__main__':
	main()