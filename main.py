#Write your code below this row 👇
num = 0
for num in range(0,101):
  if num % 3 == 0  and num % 5 == 0:
   print("fizzbuzz")
  elif num % 3 == 0:
   print("fizz")
  elif num % 5 == 0:
   print("buzz")
  else:
   print(num)      
