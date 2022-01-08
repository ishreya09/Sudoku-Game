import sudoku
from tkinter import *
import random



def generate():
    grid=sudoku.main()
    #print(grid)
    return grid


def object(t,g,w,h,bg):
    r=Tk()
    r.title(t)
    r.geometry(g)
    r.minsize(w,h)
    r.maxsize(w,h)
    r.configure(background=bg)
    return r


def message(r):
    r.destroy()

    root=object("Solved Successfully","200x200",200,200,"black")

    Label(
        root,
        text= "Sudoku solved successfully",
        fg="white",
        bg="black",
        font="calibri 15",

    ).pack(side=TOP)

    Button(
        root,
        text="Ok",
        command=root.destroy,
        bg="#29293d",
        fg="white",

    ).pack(anchor=CENTER)

    Button(
        root,
        text="NEW Game",
        command=main,
        bg="#29293d",
        fg="white",
    ).pack(anchor=CENTER)


def tryagain(root):
    r=object("Sorry! It's not correct","200x200",200,200,"black")
    Label(
        r,
        text= "Sorry! It's not correct",
        fg="white",
        bg="black",
        font="calibri 15",

    ).pack(side=TOP)

    Button(
        r,
        text="Continue the Game",
        command=r.destroy,
        bg="#29293d",
        fg="white",

    ).pack(anchor=CENTER)

    Button(
        r,
        text="NEW Game",
        command=lambda:[r.destroy(),root.destroy(),main()],
        bg="#29293d",
        fg="white",
    ).pack(anchor=CENTER)



def main():
    root= object("SUDOKU GAME","200x400",200,400,"black")
    grid=generate()

    e=[[0,0,0,0,0,0,0,0,0] for i in range(9)]

    for i in range(len(e)):
        for k in range(len(e[1])):

            e[i][k]=IntVar(root)
        

    entry=[[0,0,0,0,0,0,0,0,0] for i in range(9)]

    
        
    def validate():
        

        solved=[[0,0,0,0,0,0,0,0,0] for i in range(9)]

        for i in range(len(e)):
            for j in range(len(e[1])):
                solved[i][j]=e[i][j].get()


        print (solved)
        print(grid==solved)
        if grid==solved:
            message(root)
        else:
            tryagain(root)

    def create():
        l=[[0,1,2,3,4,5,6,7,8] for i in range(9)]
        for i in range(len(l)):
            a=random.choices(l[i],k=4)
            for j in a:
                for k in range(len(grid)):
                    e[i][j].set(grid[i][j])
                    entry[i][j].configure(state="readonly",bd=0, bg="#29293d",fg="black")
    

    
    
    for i in range(len(entry)):
        for k in range(len(entry[1])):
            entry[i][k]=Entry(
                            root,
                            textvariable=e[i][k],
                            width=1,
                            font="calibri 20 bold",
                            bg="#29293d",
                            bd=0,
                            fg="white",
                        )
            entry[i][k].grid(row=i,column=k,padx=3,pady=3)



    create()

    k=1
    for i in "SUBMIT":
        Button(
            command=validate,
            text=i,
            font="calibri 10 bold",
            bg="black",
            bd=0,
            fg="white",
        ).grid(row=11,column=k)
        k=k+1
        
    
    
    
    
    

    root.mainloop()


if __name__=="__main__":
    main()

