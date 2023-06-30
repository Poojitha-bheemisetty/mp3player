from pygame import mixer
from tkinter import *
import tkinter.font as font
from tkinter import filedialog
def addsongs():
    tempsong=filedialog.askopenfilenames(initialdir="Music/",title="Choose a song", filetypes=(("mp3 Files","*.mp3"),))
    for s in tempsong:
        s=s.replace("","")
        slist.insert(END,s)            
def deletesong():
    csong=slist.curselection()
    slist.delete(csong[0]) 
def Play():
    song=slist.get(ACTIVE)
    song=f'{song}'
    mixer.music.load(song)
    mixer.music.play()
def Pause():
    mixer.music.pause()
def Stop():
    mixer.music.stop()
    slist.selection_clear(ACTIVE)
def Resume():
    mixer.music.unpause()
def Previous():
    prev=slist.curselection()
    prev=prev[0]-1
    temp2=slist.get(prev)
    temp2=f'{temp2}'
    mixer.music.load(temp2)
    mixer.music.play()
    slist.selection_clear(0,END)
    slist.activate(prev)
    slist.selection_set(prev)
def Next():
    next=slist.curselection()
    next=next[0]+1
    temp=slist.get(next)
    temp=f'{temp}'
    mixer.music.load(temp)
    mixer.music.play()
    slist.selection_clear(0,END)
    slist.activate(next)
    slist.selection_set(next)
root=Tk()
root.title('Phonograh mp3 Player ')
mixer.init()
slist=Listbox(root,selectmode=SINGLE,bg="crimson",fg="white",font=('arial',15),height=12,width=47,selectbackground="coral",selectforeground="red")
slist.grid(columnspan=9)
deffont = font.Font(family='Helvetica')
playb=Button(root,text="Play",width =7,command=Play)
playb['font']=deffont
playb.grid(row=1,column=0)
pauseb=Button(root,text="Pause",width =7,command=Pause)
pauseb['font']=deffont
pauseb.grid(row=1,column=1)
stopb=Button(root,text="Stop",width =7,command=Stop)
stopb['font']=deffont
stopb.grid(row=1,column=2)
resb=Button(root,text="Resume",width =7,command=Resume)
resb['font']=deffont
resb.grid(row=1,column=3)
prevb=Button(root,text="Prev",width =7,command=Previous)
prevb['font']=deffont
prevb.grid(row=1,column=4)
nextb=Button(root,text="Next",width =7,command=Next)
nextb['font']=deffont
nextb.grid(row=1,column=5)
my_menu=Menu(root)
root.config(menu=my_menu)
add_song_menu=Menu(my_menu)
my_menu.add_cascade(label="Menu",menu=add_song_menu)
add_song_menu.add_command(label="Add songs",command=addsongs)
add_song_menu.add_command(label="Delete song",command=deletesong)
mainloop()