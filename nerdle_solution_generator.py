"""
generates all the valid solutions for nerdle, to use in a solver

finds solutions of the form
a x b y c = d, where a,b,c,d are numbers and x,y are operators
or
a x b = d 

assumtions:

- a is positive. e.g. -5+4+3=2 is not allowed

- none of the components a,b,c is zero

- multiplication by 1 is not allowed

- division by 1 is not allowed

- d is >= 0)

"""
from itertools import product

def generate_solutions():


  for a,b,c in product(range(1,100),repeat=3):
    if len(str(a)+str(b)+str(c)) > 4 :
      continue

    for x,y in product('+-*', repeat=2):
        #if not( x=='*' and (a==1 or b==1)) and not(y=='*' and (b==1 or c==1)):
        expression = str(a)+x+str(b)+y+str(c)
        d = eval(expression)
        if d >= 0:
          equation = expression+'='+str(d)
          if len(equation)==8:
            yield equation
            #print(equation)
      
   
    # handle division with several separate cases
    x= '/'
    y= '*'
    if b!=0   and (a*c)%b == 0  :

      d = (a*c)//b
      expression = str(a)+x+str(b)+y+str(c)
      equation = expression+'='+str(d)
      if len(equation)==8:
        yield equation
        #print(equation)

    x= '*'
    y= '/'
    if c!=0   and (a*b)%c == 0  :

      d = (a*b)//c
      expression = str(a)+x+str(b)+y+str(c)
      equation = expression+'='+str(d)
      if len(equation)==8:
        yield equation
        #print(equation)

    x='/'
    if b!=0 and (a)%b == 0  :

      for y in '+-':
        d= a//b + c if y=='+' else a//b - c
        if d >= 0:
          expression = str(a)+x+str(b)+y+str(c)
          equation = expression+'='+str(d)
          if len(equation)==8:
            yield equation
            #print(equation)
          
    x='/'
    y='/'
    if b*c != 0 and a%(b*c)==0:
      d = a//(b*c)
      expression = str(a)+x+str(b)+y+str(c)
      equation = expression+'='+str(d)
      if len(equation)==8:
        yield equation
        #print(equation)
    
    y='/'
    if c!=0  and b%c == 0  :

      for x in '+-':
        d= a+b//c if x=='+' else a-b//c
        if d >= 0:
          expression = str(a)+x+str(b)+y+str(c)
          equation = expression+'='+str(d)
          if len(equation)==8:
            yield equation
            #print(equation)

  # now deal with single expressions  a x b = d          
  for a,b in product(range(1,1000),repeat=2):
    if len(str(a)+str(b)) > 5 :
      continue

    for x in '+-*':
        expression = str(a)+x+str(b)
        d = eval( expression )
        if d >= 0 :
          equation = expression+'='+str(d)
          if len(equation)==8:
            yield equation
            #print(equation)
      
    x='/'
    if b>0 and a%b==0:
      d= a//b
      equation = str(a)+x+str(b)+'='+str(d)
      if len(equation)==8:
        yield equation
        #print(equation)
    
    
#-----------------------------------------------------------------------------
def bitmap(word):
  return sum( 2**(ord(c)) for c in set(word) )

for x in '+-*/=0123456789':
  print(x, ord(x) )

from time import perf_counter

print ( "nerdleDict = {" )
starttime= perf_counter()
count=0
for x in generate_solutions():
  count+=1
  print ( '"'+ x + '" :' + str(bitmap(x))+',' )
endtime= perf_counter()
print('}')

print ("total expressions: ", count, ", ", endtime-starttime,"sec")
