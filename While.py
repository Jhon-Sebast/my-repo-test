#ciclos while
value=1
while value <=4:
    print(value)
    value+=1
print('')
#romper la sentencia usando break
num=20
while num>=1:
    if num%3==0:
        print(num)
        break
    num-=1

num=21
while num>=1:
    num-=1
    if num%3==0:
        continue
    print(num,end=',')
num=1
while num<10:
    print(num)
    num+=2

#While True
while True:
    mark=float(input('Introduzca nueva nota'))
    if not(0<=mark<=10):
        print('nota fuera de rango')
        break
    print(mark)