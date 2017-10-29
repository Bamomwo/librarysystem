from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import tkinter
import matplotlib.pyplot as plt


class library:
    conn = sqlite3.connect('udslibrary.db')
    c = conn.cursor()

    def __init__(self, master):
        self.m = master
        self.general_one = ttk.Frame(master)
        self.general_two = ttk.Frame(master)
        self.search_books = ttk.Frame(self.general_one,relief = SUNKEN)
        self.borrow_books = ttk.Frame(self.general_one)
        self.display_results = ttk.Frame(self.general_two)
        self.search_books.pack(anchor = 'nw',side = LEFT)
        self.borrow_books.pack( anchor = 'nw',side = LEFT)
        self.display_results.pack(side = BOTTOM)
        self.general_one.pack(anchor = 'nw')
        self.general_two.pack(anchor = 'nw')
       
        #### Menu items #####
        master.option_add("*tearOff",False)
        self.menu = Menu(master)
        master.config(menu = self.menu)
        
        self.submenu = Menu(self.menu)
        self.menu.add_cascade(label = "File", menu = self.submenu)
        self.submenu.add_command(label = "Quit", command = master.quit)

        self.analysis = Menu(self.menu)
        self.menu.add_cascade(label = "Analysis", menu = self.analysis)
        self.analysis.add_command(label ="Faculty Analysis", command = self.facultyanalysis)
        self.analysis.add_command(label = "Sectional Analysis", command = self.sectionanalysis)
        self.analysis.add_command(label ="Deptmental Analysis", command = self.courseanalysis)

        self.about = Menu(self.menu)
        self.menu.add_cascade(label = "About", menu =self.about)
        self.about.add_command(label = "Author", command = self.author)
        

        
        ####### search books sections #####
        ####### Widgets

        self.logo = PhotoImage(file = 'udslib.png')
        ttk.Label(self.search_books, image = self.logo).grid(row = 0, column = 0,rowspan = 3, columnspan = 10)

        self.var1 = StringVar(self.search_books)
        ttk.Label(self.search_books, text="Search by:", font = ('Courier', 18,'bold')).grid(row = 5, column = 0, pady = 20)
        
        ttk.Radiobutton(self.search_books, text="Author", variable = self.var1, value ="author").grid(row = 6, column = 1, sticky = 'w')
        ttk.Radiobutton(self.search_books, text="Title", variable = self.var1, value ="title").grid(row = 7, column = 1, sticky = 'w', pady = 10)
        self.large_font = ('Courier',15)
        self.searchentry = ttk.Entry(self.search_books, width = 50,font = self.large_font)
        self.searchentry.grid(row = 9, column = 0, columnspan = 5, sticky = 'w')
        
        self.ms = ttk.Button(self.search_books, text="Search",command = self.searchbook, width = 20)
        self.ms.grid(row = 9, column = 5, sticky = 'w',ipady = 3)
        ttk.Button(self.search_books, text="Clear Content", command = self.something, width = 30).grid(row = 10, column = 0, columnspan = 5, pady = 85)
        s = ttk.Separator(self.search_books, orient =VERTICAL)
        s.grid(row = 0,column = 11, rowspan = 10, sticky = 'ns')

        ###### Borrower's sections ########
        self.logo2 = PhotoImage(file = 'borrow.png')
        
        ttk.Label(self.borrow_books, image = self.logo2).grid(row = 0, column = 0, columnspan= 4, rowspan =2, \
                                                              padx = 20)

        ttk.Label(self.borrow_books, text = 'Register', font = ('Courier', 18, 'underline')).grid(row = 2, column=0)

        ttk.Label(self.borrow_books, text = "    ").grid(row = 3, column = 0)

        ttk.Label(self.borrow_books, text="Student ID").grid(row = 4, column = 0,sticky = 'w')
        ttk.Label(self.borrow_books, text="Programme of Study").grid(row = 4, column = 3,sticky = 'w')
        ttk.Label(self.borrow_books, text="Level").grid(row = 7, column =0,sticky = 'w')
        ttk.Label(self.borrow_books, text="Title of Book").grid(row = 7, column = 3,sticky = 'w')

        self.student_id = ttk.Entry(self.borrow_books)
        self.student_id.grid(row = 5, column = 0,sticky = 'w',pady = 4)
        self.programme = ttk.Entry(self.borrow_books)
        self.programme.grid(row = 5, column = 3,sticky = 'w',pady = 4)
        self.level = ttk.Entry(self.borrow_books)
        ttk.Label(self.borrow_books, text = "    ").grid(row = 6, column = 0)
        self.level.grid(row = 8, column = 0,sticky = 'w',pady = 4)
        self.title = ttk.Entry(self.borrow_books)
        self.title.grid(row = 8, column = 3,sticky = 'w',pady = 4)  

        ttk.Label(self.borrow_books, text = "    ").grid(row = 9, column = 0)
        
        self.registerbook = ttk.Button(self.borrow_books, text="Register Book",command = self.registerbook, width =20)
        self.registerbook.grid(row = 10,sticky = 'w', column = 0, columnspan = 4)
        
        self.clearcontent = ttk.Button(self.borrow_books, text="Clear content",command = self.clear, width =20)
        self.clearcontent.grid(row = 10, column = 3,sticky = 'w', columnspan = 4)
        ######## Find borrow's of books ####
        ttk.Label(self.borrow_books, text = "    ").grid(row = 11, column = 0)
        ttk.Label(self.borrow_books, text="Find a borrower",foreground = 'green', font= ('Lucida Calligraphy', 18, 'underline')).grid(row = 12, column = 0, columnspan = 2)

        self.second_font = ('Courier',12)
        
        ttk.Label(self.borrow_books, text="Search by Id").grid(row = 20, column = 0,sticky = 'w')
        self.findentry = ttk.Entry(self.borrow_books, width = 40, font = self.second_font)
        self.findentry.grid(row = 22, column = 0, columnspan = 4, sticky = 'w')
        self.idsearch = ttk.Button(self.borrow_books, text="Search",command = self.getborrower, width = 13)
        self.idsearch.grid(row = 22, column = 4,sticky = 'w',ipady = 1)

        ###### Find all borrower's ######3
        ttk.Label(self.borrow_books, text = "    ").grid(row = 24, column = 0)
        self.all = ttk.Button(self.borrow_books, text="All Borrower's",command = self.getallborrowers ,width = 20)
        self.all.grid(row = 25, column = 0,columnspan = 2)
        self.clearlistbox = ttk.Button(self.borrow_books, text="Clear", command = self.something, width = 20)
        self.clearlistbox.grid(row = 25, column =2,columnspan = 2)

        ####### Display Section ##########
        self.lb1 = Listbox(self.display_results,width = 1366,activestyle = None ,height = 13,bg = '#ffffff', selectbackground = '#1ec6c7')
        
        
     
        self.lb1.grid(row = 0, column = 0)
        
        self.clearlistbox.bind('<Return>',self.asomething)
        self.all.bind('<Return>',self.allb)
        self.idsearch.bind('<Return>', self.getbyid)
        self.registerbook.bind('<Return>',self.get)
        self.clearcontent.bind('<Return>',self.getclear)
        self.ms.bind('<Return>',self.mainsearch)


        ##### Funtionality of the software #######
    def something(self):
        self.lb1.delete(0, 'end')

    def asomething(self,event):
        self.lb1.delete(0, 'end')
    
    def registerbook(self):
        student_id = self.student_id.get().lower()
        programme = self.programme.get().lower()
        level = self.level.get().lower()
        title = self.title.get().lower()

        if student_id == '' or programme == '' or level == '' or title == '':
            messagebox.showwarning(title ="Warning", message = "All fields are requried")
        else:
            if library.c.execute("INSERT INTO borrow(student_id,programme, level, title)VALUES(?,?,?,?)",(student_id,programme, \
                                                                                                       level, title)):
                library.conn.commit()
                messagebox.showinfo(title ="Info", message ="You have be successfully registered as a borrower")

       
    def clear(self):
        self.student_id.delete(0, 'end')
        self.programme.delete(0, 'end')
        self.level.delete(0, 'end')
        self.title.delete(0, 'end')

    def get(self,event):
        student_id = self.student_id.get().lower()
        programme = self.programme.get().lower()
        level = self.level.get().lower()
        title = self.title.get().lower()

        if student_id == '' or programme == '' or level == '' or title == '':
            messagebox.showwarning(title ="Warning", message = "All fields are requried")
        else:
            if library.c.execute("INSERT INTO borrow(student_id,programme, level, title)VALUES(?,?,?,?)",(student_id,programme, \
                                                                                                       level, title)):
                library.conn.commit()
                messagebox.showinfo(title ="Info", message ="You have be successfully registered as a borrower")

        
    ###### search functionality for borrower's sections ##3

    def getborrower(self):
        if self.lb1.size() == 0:
            id_search = self.findentry.get()
            library.c.execute("SELECT student_id,programme,level, title FROM borrow WHERE student_id = ?",(id_search,))
            for row in library.c.fetchall():
                self.lb1.insert(1,"STUDENT ID "+ (" ")*60+ "PROGRAMME" + (" ")*60 + "               lEVEL" + (" ")*60 + "TITLE")
                self.lb1.insert(1,row[0].upper() + (" ")*60 + row[1].upper() +(" ")*60 + row[2].upper() + (" ")*60 + row[3].upper())
        

    def getbyid(self,event):
        if self.lb1.size() == 0:
            id_search = self.findentry.get()
            library.c.execute("SELECT student_id,programme,level, title FROM borrow WHERE student_id = ?",(id_search,))
            for row in library.c.fetchall():
                self.lb1.insert(1,"STUDENT ID"+ (" ")*60+ "PROGRAMME" + (" ")*60 + "               LEVEL" + (" ")*60 + "TITLE")
                self.lb1.insert(1,row[0].upper() + (" ")*60 + row[1].upper() +(" ")*60 + row[2].upper() + (" ")*60 + row[3].upper())
        
    def getclear(self,event):
        self.student_id.delete(0, 'end')
        self.programme.delete(0, 'end')
        self.level.delete(0, 'end')
        self.title.delete(0, 'end')

    def getallborrowers(self):
        if self.lb1.size() == 0:
            self.lb1.insert(1,"STUDENT ID "+ (" ")*60+ "PROGRAMME" + (" ")*60 + "               LEVEL" + (" ")*60 + "TITLE")
            library.c.execute("SELECT student_id,programme,level,title FROM borrow")
            
            for row in library.c.fetchall():
                self.lb1.insert(1,row[0].upper() + (" ")*60 + row[1].upper() +(" ")*60 + row[2].upper() + (" ")*60 + row[3].upper())
            
            
    def allb(self,event):
        if self.lb1.size() ==0:
            self.lb1.insert(1,"STUDENT ID "+ (" ")*60+ "PROGRAMME" + (" ")*60 + "               LEVEL" + (" ")*60 + "TITLE")
            library.c.execute("SELECT student_id,programme,level,title FROM borrow")
            for row in library.c.fetchall():
                self.lb1.insert(1,row[0].upper() + (" ")*60 + row[1].upper() +(" ")*60 + row[2].upper() + (" ")*60 + row[3].upper())
          
        
            
        
        
    ###### Search functionality ######

    def searchbook(self):
        if self.var1.get() == 'author':
            userinput = self.searchentry.get()
            one = userinput.split()
            two = [a for a in one if len(a) >= 4]
            three = ['%'+c+'%' for c in two]
            

            for i in three:
                library.c.execute("SELECT * FROM booklocation WHERE author LIKE ? ",(i,))
                
            if self.lb1.size() == 0:
                self.lb1.insert(1,"BOOK TITLE                              " +(" ")*40+ "BOOK AUTHOR"+(" ")*70  + "LIBRARY SECTION"+(" ")*70+ "SHELF NUMBER"+(" ")*70 + "ROW NUMBER")
                for row in library.c.fetchall():
                    self.lb1.insert(1, row[1].upper()+(" ")*70 + row[2].upper()+(" ")*70 + row[3].upper() +(" ")*70 + (' ')*2 +(' ')*30 + str(row[4])+(" ")*70+  str(row[5]))
                    
                    

                library.conn.commit()
            

            
        elif self.var1.get() == 'title':
            
            userinput = self.searchentry.get()
            one = userinput.split()
            two = [a for a in one if len(a) >= 4]
            three = ['%'+c+'%' for c in two]
            

            for i in three:
                library.c.execute("SELECT * FROM booklocation WHERE title LIKE ? ",(i,))
                
            if self.lb1.size() == 0:
                self.lb1.insert(1,"BOOK TITLE                              " +(" ")*40+ "BOOK AUTHOR"+(" ")*70  + "LIBRARY SECTION"+(" ")*70+ "SHELF NUMBER"+(" ")*70 + "ROW NUMBER")
                for row in library.c.fetchall():
                    self.lb1.insert(1, row[1].upper()+(" ")*70 + row[2].upper()+(" ")*70 + row[3].upper() +(" ")*70 + (' ')*2 +(' ')*30 + str(row[4])+(" ")*70+  str(row[5]))

        else:
            userinput = self.searchentry.get()
            one = userinput.split()
            two = [a for a in one if len(a) >= 4]
            three = ['%'+c+'%' for c in two]
            

            for i in three:
                library.c.execute("SELECT * FROM booklocation WHERE title LIKE ? ",(i,))
                
            if self.lb1.size() == 0:
                self.lb1.insert(1,"BOOK TITLE                              " +(" ")*40+ "BOOK AUTHOR"+(" ")*70  + "LIBRARY SECTION"+(" ")*70+ "SHELF NUMBER"+(" ")*70 + "ROW NUMBER")
                for row in library.c.fetchall():
                    self.lb1.insert(1, row[1].upper()+(" ")*70 + row[2].upper()+(" ")*70 + row[3].upper() +(" ")*70 + (' ')*2 +(' ')*30 + str(row[4])+(" ")*70+  str(row[5]))

            
    
                    
                    

                library.conn.commit()

    def mainsearch(self, event):
        if self.var1.get() == 'author':
            userinput = self.searchentry.get()
            one = userinput.split()
            two = [a for a in one if len(a) >= 4]
            three = ['%'+c+'%' for c in two]
            

            for i in three:
                library.c.execute("SELECT * FROM booklocation WHERE author LIKE ? ",(i,))
                
            if self.lb1.size() == 0:
                self.lb1.insert(1,"BOOK TITLE                              " +(" ")*40+ "BOOK AUTHOR"+(" ")*70  + "LIBRARY SECTION"+(" ")*70+ "SHELF NUMBER"+(" ")*70 + "ROW NUMBER")
                for row in library.c.fetchall():
                    self.lb1.insert(1, row[1].upper()+(" ")*70 + row[2].upper()+(" ")*70 + row[3].upper() +(" ")*70 + (' ')*2 +(' ')*30 + str(row[4])+(" ")*70+  str(row[5]))
                    
                    

                library.conn.commit()
            

            
        elif self.var1.get() == 'title':
            
            userinput = self.searchentry.get()
            one = userinput.split()
            two = [a for a in one if len(a) >= 4]
            three = ['%'+c+'%' for c in two]
            

            for i in three:
                library.c.execute("SELECT * FROM booklocation WHERE title LIKE ? ",(i,))
                
            if self.lb1.size() == 0:
                self.lb1.insert(1,"BOOK TITLE                              " +(" ")*40+ "BOOK AUTHOR"+(" ")*70  + "LIBRARY SECTION"+(" ")*70+ "SHELF NUMBER"+(" ")*70 + "ROW NUMBER")
                for row in library.c.fetchall():
                    self.lb1.insert(1, row[1].upper()+(" ")*70 + row[2].upper()+(" ")*70 + row[3].upper() +(" ")*70 + (' ')*2 +(' ')*30 + str(row[4])+(" ")*70+  str(row[5]))
                    
                    

                library.conn.commit()

    ######## Plot functionality ###############

    def facultyanalysis(self):
        a = 'fms%'
        b = 'fas%'
        library.c.execute("SELECT COUNT(*) FROM borrow WHERE student_id LIKE ?", (a,))
        for row in library.c.fetchall():
            fmsnumber = row[0]

        library.c.execute("SELECT COUNT(*) FROM borrow WHERE student_id Like ?",(b,))
        for row in library.c.fetchall():
            fasnumber = row[0]

        faculties = ['F M S', 'F A S']
        values = [fmsnumber, fasnumber]
        cols = ['C1', 'C2']

        plt.title('F.M.S  verses F.A.S')
        plt.pie(values, startangle = 90,shadow = True, colors = cols, explode = (0.3, 0), autopct = '%1.1f%%',labels = faculties)
        plt.show()

    def courseanalysis(self):
        computerscience = 'computer science'
        it = 'information technoloty'
        ca = 'computing with accounting'
        me = 'mathematics with economics'
        library.c.execute("SELECT COUNT(*) FROM borrow WHERE programme = ?",(computerscience,))
        for row in library.c.fetchall():
            computerscience = row[0]

        library.c.execute("SELECT COUNT(*) FROM borrow WHERE programme = ?",(it,))
        for row in library.c.fetchall():
            it = row[0]

        library.c.execute("SELECT COUNT(*) FROM borrow WHERE programme = ?",(ca,))
        for row in library.c.fetchall():
            ca = row[0]
            
        library.c.execute("SELECT COUNT(*) FROM borrow WHERE programme = ?",(me,))
        for row in library.c.fetchall():
            me = row[0]

        put = [ computerscience,it, ca, me ]
        cols = ['C2', 'C4', 'C6', 'C8']
        labs = ['Comp Science', 'I. T' , 'Comp & accouting', 'Maths with econs']
        plt.title("Courses Statistic")
        plt.pie(put, startangle = 90, shadow  = True, colors = cols, explode = (0,0.3,0, 0), autopct = '%1.1f%%', labels = labs)
        plt.show()

    def sectionanalysis(self):
        Tech = 'Technology'
        Chem = 'Chemistry'
        Stats = 'Statistics'
        Religion = 'Religion'
        Politics = 'Politics'
        Maths = 'Mathematics'

        library.c.execute("SELECT COUNT(*) FROM booklocation WHERE section  = ?",(Tech,))
        for row in library.c.fetchall():
            Tech = row[0]
        library.c.execute("SELECT COUNT(*) FROM booklocation WHERE section  = ?",(Chem,))
        for row in library.c.fetchall():
            Chem = row[0]
        library.c.execute("SELECT COUNT(*) FROM booklocation WHERE section  = ?",(Stats,))
        for row in library.c.fetchall():
            Stats = row[0]
        library.c.execute("SELECT COUNT(*) FROM booklocation WHERE section  = ?",(Religion,))
        for row in library.c.fetchall():
            Religion = row[0]
        library.c.execute("SELECT COUNT(*) FROM booklocation WHERE section  = ?",(Politics,))
        for row in library.c.fetchall():
            Politics = row[0]
        library.c.execute("SELECT COUNT(*) FROM booklocation WHERE section  = ?",(Maths,))
        for row in library.c.fetchall():
            Maths = row[0]

##        print(Tech, Chem, Stats, Religion, Politics, Maths)
        values = [Tech, Chem, Stats, Religion, Politics]
        labels = ['Tech', 'Chem', 'Stats', 'Religion','Politics']

        plt.bar(labels, values, label = "Sections", color = 'y')
        plt.legend()
        plt.xlabel("Library sections")
        plt.ylabel("No of books")
        plt.title("Sections with number of books")
        plt.show()

        
        
        











        

    def author(self):
        winnew = Toplevel(self.m)
        winnew.title("Author")
        winnew.geometry('800x400+100+100')
        winnew.resizable(False, False)
        winnew.iconbitmap('Oxygen-Icons.org-Oxygen-Actions-document-edit.ico')
        frame = ttk.Frame(winnew)
        frame.pack()

        picture = PhotoImage(file = 'victor.png')
        picture2 = picture.subsample(4, 4)

        ttk.Label(frame, text = "BASIC INFOMATION", font = ('Lucida Calligraphy', 16,'bold'),foreground = 'green') \
                         .grid(row = 0, column = 1, sticky = 'w')

        ttk.Label(frame, text = "Name :", font = ('Courier', 13)).grid(row = 2, column = 0, pady = 4,sticky = 'w')
        ttk.Label(frame, text = "School :", font = ('Courier', 13)).grid(row = 3, column = 0, pady = 4,sticky = 'w')
        ttk.Label(frame, text = "Course :", font = ('Courier', 13)).grid(row = 4, column = 0, pady = 4,sticky = 'w')
        ttk.Label(frame, text = "Expertise :", font = ('Courier', 13)).grid(row = 5, column = 0, pady = 4,sticky = 'w')
        ttk.Label(frame, text = "Contact :", font = ('Courier', 13)).grid(row = 6, column = 0, pady = 4,sticky = 'w')


        ttk.Label(frame, text="Suliah Victor Bamomwo ( Max7 )", font = ('Courier', 13)).grid(row = 2, column = 1, \
                                                                                             pady =4,sticky = 'w')
        ttk.Label(frame, text="University For Development Studies", font = ('Courier', 13)).grid(row = 3, column = 1, \
                                                                                             pady =4,sticky = 'w')
        ttk.Label(frame, text="Bsc. Computer Science", font = ('Courier', 13)).grid(row = 4, column = 1, \
                                                                                             pady =4,sticky = 'w')
        ttk.Label(frame, text="Web & Software development and cyber security", font = ('Courier', 13)).grid(row = 5, column = 1, \
                                                                                             pady =4,sticky = 'w')
        ttk.Label(frame, text="suliahvictor@gmail.com / 0554724010", font = ('Courier', 13)).grid(row = 6, column = 1, \
                                                                                             pady =4,sticky = 'w')

        ttk.Label(frame, image = picture2).grid(row = 7, column = 0)


        winnew.mainloop()
        
        







        





        
    
        
        

        



        

def main():
    root = Tk()
    root.title('UDS LIBRARY SOFTWARE')
    root.geometry('{0}x{1}+0+0'.format(root.winfo_screenwidth(),root.winfo_screenheight()))
    root.resizable(True, True)
    root.iconbitmap('Oxygen-Icons.org-Oxygen-Actions-document-edit.ico')
    one = library(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    
