import random

# This many entries for EACH combination
rows=1000
linecount=0

f=open("terminal input.txt","w")
for i in ["in range","out range"]:
  range_note=i
  for j in ["+"]:
    op_note=j
    f.write(";"+str(rows)+" rows, " + j + ", " +i+"\n")
    for m in range(rows):
      line=""
      exp_num=""
      for k in range(2):                           #Two numbers
        if random.randint(0,1)==0: line+="-"       #Number sign
        #First char should not be zero
        line+=chr(random.randint(ord("1"),ord("9")))
        digitcount=random.randint(1,31)
        if random.randint(0,1)==0:
          dec_point=random.randint(0,digitcount)
        else:
          dec_point=-1
        for l in range(digitcount):
          line+=chr(random.randint(ord("0"),ord("9")))
          if l==dec_point:
            line+='.'
        line+="e"
        if exp_num=="":
          exp_num=random.randint(-9999,9999)
        else:
          if i=="in range":
            exp_num+=random.randint(-32,32)
            if exp_num>9999: exp_num=9999
            elif exp_num<-9999: exp_num=-9999
          elif i=="out range":
            exp_num=random.randint(-9999,9999)
        line+=str(exp_num)
        line+=" "
      line+=j+"D\n"
      f.write(line)
      linecount+=1
    f.write("\n")
f.write("E")
f.close()

print(linecount,"lines written")