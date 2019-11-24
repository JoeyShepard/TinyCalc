from sys import exit
from graphics import *
win = GraphWin("converter",400,300)

mainImage=Image(Point(200,150), "test.gif") 
mainImage.draw(win)

msg=''

for j in range(32):
    for i in range(128):
        x=mainImage.getPixel(i,j)
        if x==[255,255,255]:
            msg+=' '
        else:
            msg+='*'
    msg+='\n'

file=open("msg.txt","w")
file.write(msg)
file.close()


msg=""
for j in range(0,32,8):
    for i in range(128):
        byte=0
        for k in range(8):
            x=mainImage.getPixel(i,(24-j)+k)
            if x==[0,0,0]:
                byte|=2**(7-k)
        msg+=str(byte)+","
    msg+="\n"
            
file=open("source.txt","w")
file.write(msg)
file.close()

win.mainloop()
sys.exit()
