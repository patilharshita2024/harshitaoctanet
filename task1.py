import time
print("Please Enter your card")
time.sleep(5)
password = 1234

pin = int(input("please enter your pin:"))
balance = 100000
if pin == password:
 while True:
    print("""
          1 == balance query
          2 == cash withdraw
          3 == cash deposit
          4 == exit""")
    try:
        option = int(input("Please enter valid choice(1-4):"))
    except:
        print("Please enter valid option")

    if option == 1:
        print(f"your current balance is {balance}")

    if option == 2:

        withdraw_amount = int(input("Enter withdraw amount:"))

        balance = balance-withdraw_amount

        print(f"{withdraw_amount} is debited your account")

        print(f"your current balance is{balance}")

    if option == 3:

        deposit_amount = int(input("Enter deposit amount:"))

        balance = balance+deposit_amount

        print(f"{deposit_amount} is credited your account")

        print(f"your current balance is{balance}")
    if option == 4:
        break

else:
    print("you enter wrong pin please try again")