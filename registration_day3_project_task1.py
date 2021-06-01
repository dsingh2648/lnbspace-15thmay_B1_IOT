register=input('do you want to register(y/n):')
if(register=='y'):
    print(" You can register")
    user_name=input("Enter your username: ")
    full_name=input("Enter your Name: ")
    password=input("Enter your password: ")
    while(1):
        password_length=len(password)
        l,n,u=0,0,0
        for char in password:
             if char.islower():
                 l+=1
             elif char.isnumeric():
                 n+=1
             elif char.isupper():
                 u+=1
        if(l and n and u and password_length==8):
            print("Registration successful!!\n")
            break
        else:
            print("Error: Enter a valid Password!!")
            password=input("Enter your password again:")
while(1):
    Login=input("Do you want to login(y/n):")
    if Login=='y':
       username=input("Enter your username: \n")
       pswrd=input("Enter your password: \n")
       if username!=user_name or pswrd!=password:
           print("\n Enter valid username and password")
       else:
           print("you are successfully logged in!!\n")
           while(1):
                service=input(" do you want our service(y\n):")
                if service=='y':
                    print(" there are three service:\n")
                    print("1. Calculator(press 1)")
                    print("2. Table(press 2)")
                    print("3. Pattern(press 3)")
                    choice=input("Enter your choice: ")
                    if choice=='1':
                        while(1):
                            print("\n Calculator")
                            a = eval(input("Enter first number : \n"))
                            b = eval(input("Enter second number : "))
                            print("\nselect operation to perform")
                            print("1. Addition (press A)")
                            print("2. Substraction (press S)")
                            print("3. Multiplication (press M)")
                            print("4. Division (press D)")
                            operator = input("\nEnter your choice :")
                            if(operator == 'A'):
                                print("The addition of two number = ",a+b)
                            elif(operator == 'S'):
                                print("The substraction of two number =",a-b)                    
                            elif(operator == 'M'):
                                print("The multiplication of two number = ",a*b)                
                            elif(operator == 'D'):
                                print("The division of two number = ",a/b)
                            exit_choice = input("\nDo you want to exit calculator (y/n) :")
                            if(exit_choice == 'y'):
                                break      
                    if choice == '2':
                        while(1):
                            print("Table Generator\n")
                            n = eval(input("\nEnter the number : "))
                            for i in range(1,11):
                                print(n,' x ',i,' = ',n*i)
                            exit_choice = input("\nDo you want to exit table generator (y/n) : ")
                            if(exit_choice == 'y'):
                                break
                    if choice == '3':
                        while(1):
                            print("\nPattern Printing")
                            n = eval(input("\nEnter the number : "))
                            for i in range(1,n+1):
                                for j in range(1,i+1):
                                    print(j,end='')
                                print()
                            exit_choice = input("\nDo you want to exit pattern printing (y/n) : ")
                            if(exit_choice == 'y'):
                                break

                    else :
                        break
           else:
               break
    else:
        break

   
            
            
    
             
                 
    




       
                
                                        
                            
            
   


            
        
    
        
    

           
       
    

    
    
            


                
                
             
                                    
