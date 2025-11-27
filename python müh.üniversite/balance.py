balance=500
print("Hi User!")# welcome message 
print("Your balance:",balance)# initial balance display
while True:# infnite loop
    print("\n1)Increase the balance","2)Cash out","3)Deposite","4)Exit", sep="\n") # menu 
    operation_number=int(input("Please choose an operation:"))# user input 
    match operation_number: # match case  (match yapısı, bir değeri farklı durumlarla karşılaştırmak ve her duruma karşılık gelen işlemleri gerçekleştirmek için kullanılır.)
        case 1: # increase the balancer 
            income=int(input(("enter the income:"))) # user input 
            print("\nAre you sure? Y/N",end=": ")# confirmation
            choice1=input().upper() # user input 
            match choice1: # tupler list 
                case "Y":# increase the balance 
                    print("\nWait a second...") # loodiing message 
                    balance+=income # balance increase
                    print("Added to your balace:",income) # added balance 
                    print("Total balance:",balance) # total balance 
                case "N": # cancel operation 
                    print("The operation was cancelled") # cancel message 
        case 2: # cash out 
            print("Please enter the amount of cash!")# user input 
            cash=int(input()) # user inpur 
            print("\nAre you sure? Y/N")# confirmation
            balance-=cash# balance decrease
            choice2=input().upper() # user input 
            match choice2:# tupler list 
                case "Y": # caash out 
                    print("\nWait a second...") # loading message 
                    print("Please take your money!")# cash out message 
                    print("Total balance:",balance)# total balance 
                case "N":# cancel operation 
                    print("The operation was cancelled")# cancel message
                    balance+=cash # balance return
        case 3:
            interest=0.12 # interest rate 
            balance+=balance*interest # balance increase 
            print("\nDeposite:",interest*balance) # depozite message 
            print("Do you want to add the deposite to your balance? Y/N") # confirmatin 
            choiceB=input().upper() # user input 
            match choiceB:# tupler lisst 
                case "Y":# add the deposite 
                    print("added",balance*interest,"Total Balance:",balance)# added message 
                case "N":# cancel operation 
                    balance-=balance*interest # balance return
                    continue
        case 4:
            print("\nAre you sure? Y/N",end=": ")# confirmation 
            choice3=input().upper() # user input 
            match choice3:# tupler list 
                case "Y":# exit 
                    print("\nGood Bye User!") # gooodbye message 
                    break# exit the loop
                case "N":
                    continue# cancel oparation 
