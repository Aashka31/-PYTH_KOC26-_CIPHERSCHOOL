numb = int(input ("Enter the number of till which the user wants to print the multiplication table: "))      
 
number=1
while number<=numb:
  print ("The Multiplication Table of: ", number)    
  for count in range(1, 11):      
    print (number, 'x', count, '=', number * count)   
  number=number+1