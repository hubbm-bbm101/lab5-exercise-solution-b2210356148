N=int(input("Enter a number: "))
odd=even=0
for i in range(1,N + 1):
   if i % 2 == 0:
    even +=i
   else:
    odd +=i
print("Sum of odd numbers is",odd)
print("The average of even numbers is",even/int(N/2))