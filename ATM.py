security_key = input('Please enter your security key')
account_balance = 500

if security_key == '1234':
    print('Your security key is correct!')
    print('1. Account balance \n')
    print('2. Money transfer \n')
    print('3. Money withdraw \n')
    print('4. Money insertion \n')
    print('5. Change security key \n')
    choice = input('Imput chosen operation number\n')
    

    if choice == '1':
        print('Account balance is {}$'. format(float(account_balance)))
    elif choice == '2':
        transfer_amount = abs(float(input('Input how much money do you want to transfer\n')))#no need negative numbers
        if  transfer_amount <= account_balance:
            account_balance = account_balance - transfer_amount
            print("You transaction is sucessfuly completed! \n")
            print('Yuor new accoun balance is {}$'.format(account_balance))
        else:
            print('Sorry, you not have enough money!')
    elif choice == '3':
        withdraw = abs(float(input('Enter how much money you want to withdraw\n')))
        if withdraw <= account_balance:
            account_balance = account_balance - withdraw
            print('Withdraw was successful! \n')
            print('Your account balance is {}$'.format(account_balance))
        else:
            print('Not enough funds!')
    elif choice == '4':
        insert_amount = abs(float(input('Please type how much money do you want to insert\n')))
        if insert_amount <= 5000:
            print('Your insertion was successufl!\n')
            account_balance = account_balance + insert_amount
            print('Your account balance is {}$'. format(account_balance))
        else:
            print('Chosen amount is not awailable!')
    elif choice == '5':
        old_pass = input('Enter your old password.\n')
        if old_pass == security_key:
            new_pass1 = input('Enter your new password\n')
            new_pass2 = input('Enter your new password again\n')
            if new_pass1 == new_pass2:
                security_key = new_pass1
                print('Password was changed!')
            else:
                print('your new passwords did not  match!')
        else:
            print('You netered wrond password!')
else:
    print('You entered incorrect password!')