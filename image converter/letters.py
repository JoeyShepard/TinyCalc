from sys import exit
from graphics import *
import ctypes

win = GraphWin("converter",400,300)

mainImage=Image(Point(200,150), "letters.gif") 
mainImage.draw(win)

width=mainImage.getWidth()
height=mainImage.getHeight()

msg=''

for j in range(height):
    for i in range(width):
        x=mainImage.getPixel(i,j)
        if x==[0,0,0]:
            msg+='*'
        else:
            msg+=' '
    msg+='\n'

file=open("msg.txt","w")
file.write(msg)
file.close()


msg=""
msg_part=""
msg_len=0
for j in range(0,height,8):
    for i in range(width):
        byte=0
        if i%8>2:
            for k in range(8):
                x=mainImage.getPixel(i,j+k)
                if x==[0,0,0]:
                    byte|=2**(7-k)
            msg_part+=str(byte)+","
            if byte!=0:
                msg_len=i%5+1
            if i%8==7:
                #msg+=str(msg_len)+","+msg_part+" "
                msg+=","+msg_part+" "
                msg_part=""
                msg_len=0
            #ctypes.windll.user32.MessageBoxW(0, msg_part+"\n"+msg, "Your title", 1)            
    msg=msg[:-2]+"\n"
            
file=open("source.txt","w")
file.write(msg)
file.close()

win.mainloop()
sys.exit()
