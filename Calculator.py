from tkinter import *
from tkinter import messagebox as ms
root=Tk()
root.geometry("500x500")
root.title("Simple Calculator ")
root.config(bg="#2C3F50")
root.iconbitmap("calculatoricon.ico")


def show(value):
    # entry.delete(0, tk.END)
    text=value.widget.cget("text")
    current = entry_result.get() #value of entry_result

    if text=="=":
        if current=="": #If entry is empty
            ms.showerror("Error","Write Some Expression")
        else: #Otherwisw calculate the expression
            try:
                result=eval(current)
                entry_result.delete(0,END)
                entry_result.insert(END,result)
                print(result)
            except:
                entry_result.delete(0,END)
                entry_result.insert(5,"Error")
                ms.showerror("Error","Type a Valid Expression.")
                entry_result.delete(0,END)
            

    elif text=="C":
        entry_result.delete(0,END)
    elif text=="⌫":
         current = entry_result.get()
         entry_result.delete(0,END)
         entry_result.insert(END, current[:-1])
         print(current)
    else:
      entry_result.delete(0,END)
      entry_result.insert(END,current+ str(text))
# --------------Logic for Menu-------------------------
def menu_message():
    ms.showinfo("Information","To find square or cude of a number press the multiply button 2 times and write 2 or 3 to get cube or square.Thanks")
def Introduction():
    ms.showinfo("About us","Python GUI development services are available. ")
main=Menu(root)
content=Menu(main,tearoff=0)
content.add_command(label="Square & Cube",command=menu_message)
main.add_cascade(menu=content,label="Square & Cube")
root.config(menu=main)

content2=Menu(main,tearoff=0)
content2.add_command(label="About us",command=Introduction)
content2.add_command(label="Exit",command=root.quit)
main.add_cascade(menu=content2,label="More")
root.config(menu=main)



    
        


x=25
y=120

entry_result=Entry(root,font="halvatica 20 bold",fg="white",background="#6d7e9c",bd=5,relief=SUNKEN)
entry_result.place(x=0,y=0,width=500,height=100)
for i in range(9,0,-1):
    button_1=Button(text=i,bg="#34495E",font="Merriweather 20 bold",cursor="hand2")
    button_1.place(x=x,y=y,width=100,height=50)
    button_1.bind("<Button-1>",show)
    x+=120 #this will increase value of x in every iteration in place method.
    if i==7 :
        x=25
        y=195
    if i==4:
        x=25
        y=272
# ------------------for loop for these buttons::["C","0","."]-------
final=["C",".","⌫"]
x2=25 #positon of first button.
for o in final:#this is final content:["C","0","."]
    button_o=Button(text=o,bg="#34495E",font="Merriweather 20 bold",cursor="hand2")
    button_o.place(x=x2,y=420,width=100,height=50)
    button_o.bind("<Button-1>",show)
    x2+=120
    if o=="C":
        button_o.config(background="#cc635c")
    if o=="⌫":
        button_o.config(background="#cc635c")
# ------------------for loop for :["+","-","x","÷","="]-----------------
sign=["+","-","*","/","="]
y3=120
for j in sign:
    button_j=Button(text=j,bg="#34495E",font="Merriweather 20 bold",cursor="hand2")
    button_j.place(x=380,y=y3,width=100,height=50) 
    button_j.bind("<Button-1>",show)
    y3+=75
    if j=="=":
        button_j.config(bg="#4fd179")
# --------------///---------------------

sign2=["(","0",")"]
x4=25
# y=
for k in sign2:
    button_k=Button(text=k,bg="#34495E",font="Merriweather 20 bold",cursor="hand2")
    button_k.place(x=x4,y=345,width=100,height=50) 
    button_k.bind("<Button-1>",show)
    x4+=120

root.mainloop()