



#UNNEEDED!




addresses={}
for i in range(-9999,9999):
  if i % 100==0:
    print(i,", dict size:",len(addresses))
  for j in range(-9999,9999):
    if i<0:
      newI=(0x8000+i)
    else:
      newI=i

    if j<0:
      newJ=(0x8000+j)
    else:
      newJ=j

    newtotal=(i+j)&0xFFFF

    if newtotal<=0x270F:
      calc=newtotal
    elif newtotal<=0x58F0:
      calc="positive overflow"
    elif newtotal<=0x8000:
      calc=0x8000-newtotal
    elif newtotal<=0xA70F:
      calc=(newtotal-0x8000)*-1
    elif newtotal<=0xD8F0:
      calc="negative underflow"
    else:
      calc=(0x8000-newtotal)*-1


    if newtotal not in addresses.keys():
      addresses.update({newtotal:calc})
    elif addresses[newtotal]!=calc:
      print(i,"+",j,"dict:",newtotal," but calc:",calc)
      exit(0)

print("\nDone\nDict size:",len(addresses))
