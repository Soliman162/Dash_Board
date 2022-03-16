from tkinter import *
from tkinter import font
from PIL import ImageTk,Image

Speed_list =list()
Speed_Label_list = list() 

Battery_list = list()
Battery_Label_List =list()

KM_Value = 0.0000


#define Widget
Dash_Board = Tk()
Dash_Board.geometry("800x480")
#define Back_Ground_Image
#Back_Ground = PhotoImage(file="~/Embedded_linux/Neutrino/DashBoard/Variables/Asset 13.png")
Right_Sign_off = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Right_Sign/Turn_right_off.png"))
Right_Sign_on = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Right_Sign/Turn_right_on.png"))
Left_Sign_off = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Left_Sign/Turn_left_off.png"))
Left_Sign_on= ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Left_Sign/Turn_left_on.png"))
Neutrino = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Constant/Neutrino_logo.png"))
EVER = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Constant/EVER.png"))
Park = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Variables/Park.png"))
Horn = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Variables/Horn.png"))
Hight_LIght = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Variables/High_light.png"))
Running_Light = ImageTk.PhotoImage(Image.open("/home/soliman/Embedded_linux/Neutrino/DashBoard/Variables/Runing_light.png"))


for i in range(61):
    Speed_list.append(ImageTk.PhotoImage(Image.open(f"/home/soliman/Embedded_linux/Neutrino/DashBoard/speedometer/{i}.png")))
    Speed_Label_list.append(Label(image= Speed_list[i] ) )

for i in range(0,6):
    Battery_list.append(ImageTk.PhotoImage(Image.open(f"/home/soliman/Embedded_linux/Neutrino/DashBoard/Battery/{i}.png")))
    Battery_Label_List.append(Label(image= Battery_list[i] ) )


#Back_Ground_Label = Label(Dash_Board, image=Back_Ground)
Right_Sign_off_label = Label(image=Right_Sign_off)
Right_Sign_on_label = Label(image=Right_Sign_on)
Left_Sign_off_label = Label(image=Left_Sign_off)
Left_Sign_on_label = Label(image=Left_Sign_on)
Neutrino_Label = Label(image=Neutrino)
EVER_Label = Label(image=EVER)
KM_Label = Label(text=f"{KM_Value}km",font="Times 30",fg="red")
Park_Label = Label(image=Park) 
Horn_Label = Label(image=Horn)
Hight_LIght_Label = Label(image=Hight_LIght)
Running_Light_Label = Label(image=Running_Light)
#Back_Ground_Label.place(x=0,y=0,relwidth=1,relheight=1)
while True:
    ####
    Right_Sign_off_label.place(x=663,y=0)
    ####
    #Right_Sign_on_label.place(x=663,y=0)
    ###
    Left_Sign_off_label.place(x=0,y=0)
    ###
    #Left_Sign_on_label.place(x=0,y=0)
    ###
    Speed_Label_list[0].place(x=175,y=100)

    Neutrino_Label.place(x=645,y=320)

    KM_Label.place(x=350,y=400)
    Park_Label.place(x=350,y=0)
    Horn_Label.place(x=50,y=250)
    Hight_LIght_Label.place(x=50,y=200)
    Running_Light_Label.place(x=50,y=150)
    Battery_Label_List[0].place(x=660,y=150)
    flag_test = int(input("please enter number:"))

    if flag_test:
        EVER_Label.place(x=0,y=350)
    else:
       EVER_Label.place_forget()

    continue
    Dash_Board.mainloop()