for i in range (1,101):
     m = ( "fizz buzz" if i%15 == 0 else ( "fizz" if i%3 == 0 else ( "buzz" if i%5 == 0 else str(i))))
     print (m)
"""
attempt to find a shorter solution...
def modn(i, w, n):
     return (w[0]+" " + w[1] if i%(n[1]*n[0])==0 else (w[1] if i%n[1]==0 else (w[0] if i%n[0]==0 else str(i))))
print("\n".join([modn(i,["fizz", "buzz"], [5,3])   for i in range(1,101)]))


div_by = { 5:"fizz" , 15:"fizzbuzz", 3: "buzz", }
def fizzbuzz():
     for i in range(1,101):
          if i in [3,5,15]:
               print (div_by[i] if i %n==0)
        """  
