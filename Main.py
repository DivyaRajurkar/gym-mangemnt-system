from gym_manager import gym_manager
from customer import customer

print("  ****WELLCOM TO GYM MANAGER PORTAL****")



def menu():
    print("1. Create Member")
    print("2. View Member")
    print("3. Delete Member")
    print("4. Update Member")
    print("5. Create Regimen")
    print("6. View Regimen")
    print("7. Delete Regimen")
    print("8. Update Regimen")
    print("0. Exit")
    print("\nEnter you chice: ")

menu()

While(True):
    option = int(input())
    if option == 1:
        Name = str(input("Enter Member's name - "))
        Age= str(input("Enter Member's Age - "))
        Gender = str(input("Enter Member's Gender - "))
        Phoenno = str(input("Enter Member's Phoenno - "))
        Email str(input("Enter Member's Email - "))
       Bmi = str(input("Enter Member's Bmi - "))
       if Bmi < '18.5':
           r = {'Mon': 'Chest,'Tue' : 'Biceps','Wed' : 'Rest','Thu' : 'Back','Fri' : 'Triceps','Sat' : 'Rest,'Sun' : 'Rest'}
       elif Bmi < '25':
           r = {'Mon': 'Chest,'Tue' : 'Biceps','Wed' : 'Cardio/Abs','Thu' : 'Back','Fri' : 'Triceps','Sat' : 'Legs,'Sun' : 'Rest'}
       elif Bmi < '30':
           r = {'Mon': 'Chest,'Tue' : 'Biceps','Wed' : 'Abs/Cardio','Thu' : 'Back','Fri' : 'Triceps','Sat' : 'Legs,'Sun' : 'Cardio'}
       elif Bmi >='30':
           r = {'Mon': 'Chest,'Tue' : 'Biceps','Wed' : 'Cardio','Thu' : 'Back','Fri' : 'Triceps','Sat' : 'Cardio,'Sun' : 'Cardio'}
        duration = str(input("Enter duration(in months)- ")
        customer = customer(Name,Age,Gender,Phoenno,Email,Bmi,duration)
        gym_manager.regimen[Phoenno] = r
        gym_manager.addCustomer(Customer)

    elif option == 2:
        check_ph_no = input("Enter phoen number of member:")
        print("Name\tAge\tGender\tPhoenno\tEmail\tBmi\tduration")
        for customer_Id in gym_manager.customer.keys():
            if customer_Id == check_ph_no:
                customer = gym_manager.customer[customer_Id] 
                Name = customer.getName()
                Age = customer.getAge() 
                Gender = customer.getGender()  
                Phoenno = customer.getPhoenno()
                Email= customer.getEmail()
                Bmi = customer.getBmi()
                dur = customer.getduration()
                print(Name + "\t" +Age+ "\t" +Gender+ "\t" +Phoenno+ "\t" +Email+ "\t" +Bmi+ "\t" +duration)
        print("\n")

    elif option == 3:
        check_ph_no = input("Enter phoen number of member you want to delete:")
        try:
            for customer_Id in gym_manager.customers.keys():
                if customer_Id == check_ph_no:
                    print("member Deleted")
            gym_manager.customers.pop(check_ph_no) 
        except:
            print(Number doesn't exist\n")
    elif option == 4:
        check = input("Enter phoen no:")
        exr = input("Enter if you want to extend or revoke:")
        if exr == 'extend':
            for customer_Id in gym_manager.customer.keys():
                customer = gymmanager.customers[customer_Id]
                if customer_Id == check:
                    dur = customer.getduration()
                    s = int(dur)+int(input("Enter how many months you want it to be extended for:"))
                    res = str(s)
                    customer.setduration(res)
        ellif exr == 'revoke':
            for customer_Id in gym_manager.customer.keys():
                customer = gymmanager.customers[customer_Id]
                if customer_Id == check:
                    customer.setduration('0')
                    print("membership revoked")
    elif option == 5:
        ph_no = input("Enter the phoen number of member you want to create regimen of:")
        for i in gym_manager.regimen:
            if i==ph_no:
                for j in gym_manager.Regimen[i]:
                    gym_manager.Regimen[i][j] = input(j+":")
                    
    elif option == 6:
        check_ph_no = input("Enter the phoen number of member:")
        for i in gym_manager.regimen:
            if i==check_ph_no:
                for key,val in gym_manager.Regimen[i].items():
                    print(key,":",val)
        print("\n")

    elif option == 7:
        check_ph_no = input("Enter the phoen number of member:")
        for i in gym_manager.regimen:
            if i==check_ph_no:
                print("workout regimen deleted!!!")
        gym_manager.regimen.pop(check_ph_no)
        print("\n")

    elif option == 8:
        check_ph_no = input("Enter the phoen number of member who's regimen you want to update:")
        for i in gym_manager.regimen:
            if i==check_ph_no:
                d = input("Enter the day which you want to update:")
                for j in gym_manager.regimen:
                    if j == d:
                        gym_manager.regimen[i][j] = input(Enter the workout:")
                        print("updated successfully!!!!")
        print("\n")
    elif option == 0:
        break

    else:
        print("pls enter valid option")
    member_menu()

    def menu():
        print("\n****wellcome to member portal****\n")
        print("1. My Regimen")
        print("2. My Profile")
        print(3. Exist)
        print("\nEnter your choice:")

    member_menu()
    while(True):
        option = int(input())
        if option == 1:
        p = input("enter your phoen number:")
        print("-- your regimen based on your BMI --")
        for i in gym_manager.regimen :
            if i == p:
                for key,val in gym_manager.regimen[i].items():
                    print(key,":",val)
                print("\n")

    elif if option == 2:
        p = input("enter your phoen number:")
        try:
            for customer_Id in gym_manager.customers.keys():
                if customer_Id == p:
                    customer gym_manager.customers[customer_Id]  
                    name = customer.getname()
                    Age =  customer.getAge()         
                    Gender =  customer.getGender()         
                    phoenno =  customer.getphoenno()
                    Email =  customer.getEmail()   
                    Bmi =  customer.getBmi()         
                    duration =  customer.getduration()     
                    print("****your profile****")    
                    print("Name:",name,"\nAge:",age,"\nGender:",gender,"\nphone:",phoenno,"\nEmail:",email,"\nBMI:","\nduration:")
        except:
            print("no user with this phoen no exist")
    elif option == 3:
        break
    else:
        print(please enter a valid number")
        membermenu        
         












                    

            

                    





    
        