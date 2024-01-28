import tkinter as tk
MyWindow = tk.Tk()
# ------------------------------


def calc():
    r=EntCelsius.get()
    if r=='':
        EntResult["text"] = "Error!, write value"
    else:
        c=float(r)
        f=(c*1.8)+32
        EntResult["text"]=str(f)+"°F"
        print(f)


MyWindow.title("Celsius to Fahrenheit")
MyWindow.geometry("400x200")
MyWindow.attributes("-toolwindow",True)
# ------------------Frames1--------------------------
TopFrame=tk.Frame(MyWindow,width=100,height=40,padx=5,pady=5)
TopFrame.pack(side="top",fill="x")
# ------------------Frames2--------------------------
TopFrame2=tk.Frame(MyWindow,width=100,height=40,padx=5,pady=5)
TopFrame2.pack(side="top",fill="x")
# ------------------Frames3--------------------------
TopFrame3=tk.Frame(MyWindow,width=100,height=40)
TopFrame3.pack(side="top",fill="x")
# ------------------Widgets--------------------------
# ------------------Frames1--------------------------
# ------------------Label--------------------------
lblCelsius=tk.Label(TopFrame,text="Celsius:",width=15,anchor="w")
lblCelsius.pack(side="left")
# ------------------Entry--------------------------
EntCelsius=tk.Entry(TopFrame,width=24,)
EntCelsius.pack(side="left")

# ------------------Frames2--------------------------
# ------------------Label2--------------------------
lblFahrenheit=tk.Label(TopFrame2,text="Fahrenheit:",width=15,anchor="w")
lblFahrenheit.pack(side="left")
# ------------------LBL--------------------------
EntResult=tk.Label(TopFrame2,text="-",width=20)
EntResult.pack(side="left")

# ------------------Frames3--------------------------
# ------------------Button--------------------------
CoverBt=tk.Button(TopFrame3,text="Convert:",width=15,pady=5,command=calc)
CoverBt.pack()


MyWindow.mainloop()
