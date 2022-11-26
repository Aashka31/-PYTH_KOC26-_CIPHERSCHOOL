n = int(input ("Enter the number of till which the user wants to print the multiplication table: "))

def table(n):
 def nj(numb=2):
    while numb<=n:
     for i in range (1, 11):
        print  (numb,'*', i ,'=', numb* i)
     numb=numb+1
table(n)
