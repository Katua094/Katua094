def greet(name):
    print(f"Hello {name}\n\n\n")
    print("hello welcome to my club peaple")
   

greet(input("whats your name? "))
print("we have premium, gold, silver, bronze\n\n\n")

choice=input("put down your choice?  ").lower()
if choice=="premium":
  print(f"you have chosen {choice} that will be £10 please")
elif choice=="gold":
  print(f"you have chosen {choice} that will be £5 please")
elif choice=="silver":
  print(f"you have chosen {choice} that will be £2 please")
elif choice=="bronze":
  print(f"you have chosen {choice} that will be £1 please")
else:
  print("sorry we dont have that choice")

