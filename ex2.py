# Faulty Calculator
# 45*3=555, 56+9=77, 56/6=4

print('Welcome to the faulty calculator. It is developed by Agniva Chakraborty. ')
print('Your choice of operations are :')
print('+ for addition')
print('- for subtraction')
print('* for multiplication')
print('/ for division')
print('** for power')
print('% for modulo')

operation = input('Choose your operation: \n')

num1 = int(input('Enter first number: \n'))

num2 = int(input('Enter second number: \n'))

if operation == '+' and num1 == 56 and num2 == 9:
    print(77)
elif operation == '*' and num1 == 45 and num2 == 3:
    print(555)
elif operation == '/' and num1 == 56 and num2 == 6:
    print(4)
elif operation == '+':
    print('Your result is : ', num1+num2)
elif operation == '*':
    print('Your result is : ', num1*num2)
elif operation == '-':
    print('Your result is : ', num1-num2)
elif operation == '/':
    print('Your result is : ', num1/num2)
elif operation == '**':
    print('Your result is : ', num1**num2)
elif operation == '%':
    print('Your result is : ', num1 % num2)

print('Thanks for using the faluty calculator :)')
