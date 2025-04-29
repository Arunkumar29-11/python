from array import *
print("time pass quiz")

mark=0
x=[1,4,2,3]
y=array('i',[])

for i in range(4):
    ans=int(input('\t 1.what is new of the king \n\t a)raja \t b)king \n\t c)prision \t \n\n'))
    y.append(ans)
    if y[0]==x[0]:
        print('correct answer')
        mark+=1
    else:
        print('better luck next time ! ')
    ans=int(input('\t 1.what is fight? \n\t a)brave \t b)courage \n\t c)wrong \n\n'))
    y.append(ans)
    if y[1]==x[1]:
        print('correct answer')
        mark+=1
    else:
        print('better luck next time ! ')
    ans=int(input('\t 1.what is soil? \n\t a)nothing \t b)coal \n\t c)charcoal \t\n\n'))
    y.append(ans)
    if y[2]==x[2]:
        print('correct answer')
        mark+=1
    else:
        print('better luck next time ! ')
    ans=int(input('\t 1.what rain? \n\t a)noting \t b)water \n\t c)acid \t\n\n'))
    y.append(ans)
    if y[3]==x[3]:
        print('correct answer')
        mark+=1
    else:
        print('better luck next time ! ')
    break

print('total marks is :',mark)
				    
