print('welcome to SBI bank')
opening_balance=int(input('please enter the initial account balance \n'))
print('ur account opened successfully')
secret_pin=input('lets secure ur account from rubbery, enter a security pin \n')
choice=int(input('''enter : 
                       1 : to diposite
                       2 : withdraw
                       3 : balance check \n'''))
if choice==1:
    diposite_amount=int(input('enter amount u want to diposit \n'))
    opening_balance+=diposite_amount;
    print('congrats u have diposited {} money into ur account, ur current balance is : {}'
          .format(diposite_amount,opening_balance))
elif choice==2:
    witdrwal_balance=int(input('enter the amount u want to withdraw \n'))
    if opening_balance<witdrwal_balance:
        print('insufficient balance, plz try again with amount less than ur account balance')
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
            print('invalid choice')
else:
    accepted_security_pin=input('enter ur security pin \n')
    if secret_pin==accepted_security_pin:
        print('ur available account balance is : {} '.format(opening_balance))
    else:
        print('u inserted a wrong pin ')
