


# Space Weather Window  
# John Clavin - August 2018
  
  




### IMPORT MODULES AND INITIALISE VARIABLES

from tkinter import *
import urllib.request
import webbrowser

na1=0
na2=0
Alerts=0
ki=0
ai=0
sfi=0
network=0


### Define callback function
def callback():
    webbrowser.open_new(r"http://www.spaceweather.com/")

###  Normal close
def close():
    swframe.destroy()



### If network available, grab and save wwv.txt
try:
    wwv_txt = urllib.request.urlopen("http://services.swpc.noaa.gov/text/wwv.txt").read(2000)
    file = open( '/home/john/Dev/Projects/Spaceweather/noaa_data.txt', 'wb' )
    file.write(wwv_txt)
    file.close()
    network=1

except :
    network=0



### Text parsing Kp, Ap and sfi values from noaa_data
for line in open('/home/john/Dev/Projects/Spaceweather/noaa_data.txt') :
    if ":Issued:" in line:
        date_time= line[14:29]

for line in open('/home/john/Dev/Projects/Spaceweather/noaa_data.txt') :
    if "K-index" in line:
        k=line.split()
        j=(k.index("was"))
        ki=(int(float(k[j+1])))

for line in open('/home/john/Dev/Projects/Spaceweather/noaa_data.txt') :
    if "A-index" in line:
        a=line.split()
        j=(a.index("A-index"))
        ai=(int(float(a[j+1])))

for line in open('/home/john/Dev/Projects/Spaceweather/noaa_data.txt') :
    if "Solar flux" in line:
        s=line.split()
        j=(s.index("flux"))
        sfi=(int(float(s[j+1])))



### Reporting if Solar Alert exists, output as 'alerts' ###
for line in open('/home/john/Dev/Projects/Spaceweather/noaa_data.txt') :
    if "No space weather storms were observed" in line:
        na1=1

for line in open('/home/john/Dev/Projects/Spaceweather/noaa_data.txt') :
    if "No space weather storms are predicted" in line:
        na2=1

alerts=na1+na2



### Space Weather Frame
swframe=Tk()
swframe.bind('<Control-x>', close)
swframe.attributes("-topmost", True)


def space_weather_frame():

    swframe.configure(bg='#000000')
    swframe.geometry("430x240+780+403")
    swframe.overrideredirect(False)
    swframe.title("     EI5JS")
    var = StringVar()

    la=Label(swframe, text="   ", bg=("#000000"), fg=("#000000"), font=("verdana", 10))
    la.pack()

    la1=Label(swframe, text="NOAA Space Weather Data", font=("verdana", 14), bg=("#000000"), fg=("#55ff55"))
    la1.pack(pady=3)

    la6=Label(swframe, text="   ", bg=("#000000"), fg=("#000000"), font=("verdana", 1))
    la6.pack()

    var.set(date_time)
    la2=Label(swframe, text= str(date_time), font=("verdana", 12), bg=("#000000"), fg=("white"))
    la2.pack()

    var.set(ki)
    la3=Label(swframe, text="Kp index = " + str(ki), font=("verdana", 12), bg=("#000000"), fg=("white"))
    la3.pack()

    var.set(ai)
    la4=Label(swframe, text="Ap index = " + str(ai), font=("verdana", 12), bg=("#000000"), fg=("white"))
    la4.pack()

    var.set(sfi)
    la5=Label(swframe, text="SFI = " + str(sfi), font=("verdana", 12), bg=("#000000"), fg=("white"))
    la5.pack()

    la7=Label(swframe, text="   ", bg=("#000000"), fg=("#000000"), font=("verdana", 13))
    la7.pack()

    if alerts == 2:
        var.set("text")
        button=Button(swframe, text="  No Solar Storm Alerts ", font=("verdana", 12), bg=("#000000"), fg=("#b0b0b0"), height=("1"), borderwidth="0", command=callback)
        button.pack()


    if alerts != 2:
        var.set("text")
        button=Button(swframe, text="  SOLAR STORM ALERT  ", font=("verdana", 12), bg=("#000000"), fg=("#ff6666"), height=("1"), borderwidth="0", command=callback)
        button.pack()


### No Network Available Frame
def no_network_frame():

    swframe.configure(bg='#000000')
    swframe.geometry("410x210+600+300")
    swframe.title("Space Weather")
    swframe.overrideredirect(False)
    la1=Label(swframe, text="   ", bg=("#000000"), fg=("#000000"), font=("verdana", 28))
    la1.pack()
    la2=Label(swframe, text=" NOAA Website unreachable ", font=("verdana", 14), bg=("#000000"), fg=("white"))
    la2.pack()
    la3=Label(swframe, text="   ", bg=("#000000"), fg=("#000000"),font=("verdana", 14))
    la3.pack()
    la4=Label(swframe, text="  Check Network Connection  ", font=("verdana", 12), bg=("#000000"), fg=("#ff6666"))
    la4.pack()


### frame choice
if network==1:
    space_weather_frame()
if network==0:
    no_network_frame()



swframe.mainloop()
