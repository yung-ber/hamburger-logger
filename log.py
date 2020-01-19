# hamburger logging program
# by KC3LVL (aka yung-ber)
import os
from time import asctime
from urllib.request import urlopen
from ssl import _create_unverified_context
from requests import*
from os import mkdir
from time import*
from tkinter import*
from random import shuffle
context = _create_unverified_context()
'''try:
    urlopen("https://hamcall.net/call?callsign="+input('your call sign> '), context=context)
except:
    print('OOF! call invalid or connection error')
    quit()'''
stop = ""
nun=''
root=Tk()
my=open('log/settings').read()
my=my.split('\n')
my=my[1].replace('call=','')
call=Entry(root)
freq=Entry(root)
if 'randomlayout=0' in open('log/settings').read():
    c=Label(root, text='call')
    c.pack(side='left')
    f=Label(root, text='freq')
    f.pack(side='right')
    call.pack(side='left')
    freq.pack(side='right')
    history=Text(root)
    history.pack()
    root.title(my+"'s hamburger log")
else:
    sides=['top', 'bottom', 'left', 'right']
    shuffle(sides)
    call.pack(side=sides[0])
    freq.pack(side=sides[1])
    history=Text(root)
    history.pack(side=sides[2])
    call.insert(0, 'call')
    freq.insert(0, 'frequency')
    root.title(my+"'s random hamburger log")
history.insert('1.0', open('log/contact.txt').read())
def log():
    if call.get() != '':
        lines = [line.rstrip('\n') for line in open('log/contact.txt')]
        file = open("log/contact.txt", 'w')
        clock = asctime( localtime(time()) )
        print("logging contact...")
        ln='\n'
        a=''
        out = [history.get('1.0','999.999'), "\n", call.get(), "  ", freq.get(), "  ", clock]
        out = a.join(str(s) for s in out)
        file.write(out.replace(" </body></html>\n", ''))
        print("the time is: "+clock)
        file.close()
        print("contact logged.")
        history.delete('1.0', '999.999')
        history.insert('1.0', open('log/contact.txt').read())
    else:
        file=open('log/contact.txt','w')
        file.write(history.get('1.0','999.999'))
        file.close()
butt=Button(root, text='log contact', command=log)
butt.pack()
root.mainloop()
