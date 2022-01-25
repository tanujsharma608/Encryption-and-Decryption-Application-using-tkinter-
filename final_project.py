from tkinter import *
from tkinter import messagebox #message box used to display pop up messages
import base64 #base64 module provides a function to encode the binary data to ASCII characters)
 # base64 module provides a function to encode the binary data to ASCII characters and decode that ASCII characters back to binary data.
 # ASCII is a 7-bit character set containing 128 characters. It contains the numbers from 0-9, A to Z in the upper and lower case English letters 

def decrypt():
     password=code.get()# used to accept password from user
     
     if password == "1234":
        screen2=Toplevel(screen)#used to create pop ip
        screen2.title("decryption")#heading of pop up window
        screen2.geometry("400x200")#size of pop up window
        screen2.configure(bg="red")#background color of pop up window
        
        message=text1.get(1.0,END) #reading data of text box starting from first character til last character
        decode_message=message.encode("ascii") #
        base64_bytes=base64.b64decode(decode_message)
        decrypt=base64_bytes.decode("ascii")
        
        Label(screen2,text="Decrypt",font="arial",fg="black",bg="white").place(x=10,y=0)
        text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        
        text2.insert(END,decrypt)
        
     elif password=="":
         messagebox.showerror("encryption","INPUT PASSWORD")
     elif password !="1234":
         messagebox.showerror("encryption","INVALID PASSWORD")
    
def encrypt():
    password=code.get()
    if password =="1234":
        screen1=Toplevel(screen) #A Toplevel widget is used to create a window on top of all other windows.
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="red")
        
        message=text1.get(1.0,END) #reading data of text box starting from first character til last character
        encode_message=message.encode("ascii")
        base64_bytes=base64.b64encode(encode_message)
        encrypt=base64_bytes.decode("ascii")
        
        Label(screen1,text="Encrypt",font="arial",fg="black",bg="white").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)
        text2.insert(END,encrypt)
        
    elif password=="":
        messagebox.showerror("encryption","INPUT PASSWORD")
    elif password !="1234":
        messagebox.showerror("encryption","INVALID PASSWORD")
        
          
    
    
    
def main_screen():
    # Variables that are created outside of a function  are known as global variables.
    #Global variables can be used by everyone, both inside of functions and outside
    #In Python, global keyword allows you to modify the variable outside of the current scope.
    #It is used to create a global variable and make changes to the variable in a local context.
    
    global screen
    global code
    global text1
    
    screen=Tk()#used to create box
    screen.geometry("500x500")#used to create box
    #icon
    image_icon=PhotoImage(file="lock.png")#used to add small picture over box in bar 
    screen.iconphoto(False, image_icon)
    screen.title("ENCRYPTION&DECRYPTION_APPLICATION")#used to give heading over box
    
    def reset():
        code.set("")
        text1.delete(1.0,END)
    
    
    Label(text="enter text for encryption and decryption",bg="yellow" ,fg="black",font=("calbri",20)).place(x=10,y=10) #heading over the box
    text1=Text(font="Robote 20",bg="white",relief=GROOVE,wrap=WORD,bd=0)# text inside text box
    text1.place(x=10,y=50,width=355,height=100)#position of text box
    
    
    Label(text="Enter password",fg="black",bg="orange",font=("calbri",16)).place(x=10,y=170) #heading over password box
    
    code=StringVar()# password wala box
    Entry(textvariable=code,width=19,bd=0,font=("arial",25)).place(x=10,y=200) #characteristics of text inside password box
    
    Button(text="ENCRYPT",height="2",width=23,fg="black",bg="light blue",bd=0,command=encrypt).place(x=10,y=250) #encrypt button
    Button(text="DECRYPT",height="2",width=23,fg="black",bg="Magenta",bd=0,command=decrypt).place(x=200,y=250) # decryption button
    Button(text="RESET",height="2",width=50,fg="black",bg="pink",bd=0,command=reset).place(x=10,y=300) #reset Button
   
    screen.mainloop()
    
main_screen()
    
    
   
