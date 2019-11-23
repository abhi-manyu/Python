import sys


print('**************welcome to SBI bank*****************')
print('sbi wish u happy banking\n')
opening_balance=int(input('please enter the opening account balance \n'))
print('ur account opened successfully')
secret_pin=input('lets secure ur account from rubbery, enter a security pin \n')
choice=int(input('''enter : 
                       1 : to diposite
                       2 : withdraw
                       3 : balance check \n'''))
if choice==1:
    choice2=True
    while(choice2):
        temp = input("enter ur secure pin \n ")
        if(temp==secret_pin):
           diposite_amount=int(input('enter amount u want to diposit \n'))
           opening_balance+=diposite_amount;
           print('congrats u have diposited {} money into ur account, ur current balance is : {}'
              .format(diposite_amount,opening_balance))
           choice2=False
        else:
           print('''we are sorry , but u have entered an incorrect pin.
please , try again with correct pin''')
elif choice==2:
    choice2=True
    while(choice2):
        temp=input("please enter ur security pin \n ")
        if(temp==secret_pin):
            witdrwal_balance=int(input('enter the amount u want to withdraw \n'))
            if opening_balance<witdrwal_balance:
                print('insufficient balance, plz try again with amount less than ur account balance')
                sys.exit()
            elif opening_balance>witdrwal_balance:
                opening_balance-=witdrwal_balance;
                print('thank you for using SBI ATM , ur current balance is {}'.format(opening_balance))
            else:
                print('warning : so u want to withdraw all the balance from ur account ? ')
                choice2 = input('''yes \t No \n''').lower()
                print(choice2)
                if choice2 == 'yes':
                   opening_balance -= witdrwal_balance
                   print('thanks for using Atm , ur account balance is : {} '.format(opening_balance))
                elif choice2 == 'no':
                   print('thanks u saved urself , plz always try to save something, nd that will save u one day ')
                else:
                   print('invalid choice......try again')
                   sys.exit()
            choice2=False
        print('''we are sorry , but u have entered an incorrect pin.
please , try again with correct pin''')
            
else:
    choice2=True
    while(choice2):
       accepted_security_pin=input('enter ur security pin \n')
       if secret_pin==accepted_security_pin:
          print('ur available account balance is : {} '.format(opening_balance))
          choice2=False
       else:
          print('u inserted a wrong pin ')

