print("ENTER 1st NUMBER:")
a = int(input())

print("ENTER 2nd NUMBER:")
b = int(input())

print("Choose Your Operator(+,-,*,%,/,**):\n + = sum\n - = subtract\n * = multiplication\n"
      " / = division\n % = module\n ** = power")
c=input()

if a == 45 and b == 3 and c == '*':
  print("THE VALUE IS 555")

elif a == 56 and b == 9 and c == '+':
  print("THE VALUE IS 77")


elif  a ==56 and b==6 and c=='/':
  print("THE VALUE IS 4")


elif c == '+':
  d=a+b
  print("The output is")
  print(d)


elif c == '-':
  d=a-b
  print("The output is")
  print(d)

elif c == '*':
  d=a*b
  print("The output is")
  print(d)

elif c == '/':
  d=a/b
  print("The output is")
  print(d)

elif c == '%':
  d=a%b
  print("The output is")
  print(d)

elif c == '**':
  d=a**b
  print("The output is")
  print(d)

else:
  print("You Enter An Invalid operator")



