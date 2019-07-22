from guizero import App, PushButton, info, Text, MenuBar
from os import path
import configparser
from tkinter.filedialog import askdirectory
if(path.exists("autorealm.cfg")):
    config = configparser.ConfigParser()
    config.read("autorealm.cfg")
    WowPath = config.get("myvars", "WowPath")
else:
    WowPath = askdirectory()
    f = open("autorealm.cfg","w+")
    f.write("[myvars]\n")
    f.write("WowPath: " + WowPath)
    f.close()
RealmPath = WowPath + "/Data/enUS/realmlist.wtf"

def change_path():
    WowPath = askdirectory()
    f = open("autorealm.cfg","w+")
    f.write("[myvars]\n")
    f.write("WowPath: " + WowPath)
    f.close()
def menu_close():
    app.destroy()
def about_window():
    app.info("About this app", "This app was made by Fatality on 7/21/2019\nIt was made because manually changing realms can get annoying,\nand this simplifies it.\n\nThank you for using AutoRealm v1.0")
def warmane():
    f = open(RealmPath,"w+")
    f.write("set realmlist logon.warmane.com")
    f.close()
    app.info("Success!", "Realmlist Changed To Warmane!")
def wotg():
    f = open(RealmPath,"w+")
    f.write("set realmlist logon.worldofthegods.com")
    f.close()
    app.info("Success!", "Realmlist Changed To World of the Gods!")
def xwow():
    f = open(RealmPath,"w+")
    f.write("set realmlist logon.xwow.eu")
    f.close()
    app.info("Success!", "Realmlist Changed To xWoW!")
    


app = App(title="AutoRealm v1.0", bg="#000000")
message = Text(app, color="aqua", text="Welcome to v1.0 of AutoRealm!\nYou are currently set to edit: " + RealmPath)
button1 = PushButton(app, text="Warmane", command=warmane)
button1.text_color = "aqua"
button1.bg = "#323232"
button2 = PushButton(app, text="World of the Gods", command=wotg)
button2.text_color = "aqua"
button2.bg = "#323232"
button3 = PushButton(app, text="xWoW", command=xwow)
button3.text_color = "aqua"
button3.bg = "#323232"

menubar = MenuBar(app,
                  toplevel=["File", "About"],
                  options=[
                      [ ["Change WoW Path...", change_path], ["Close", menu_close] ],
                      [ ["About This App", about_window] ]
                      ])
app.display()
