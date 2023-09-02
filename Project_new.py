import os.path
print("\t\t\t\tHello, Welcome to Diet and Exercise Management System.")
print("THIS PROGRAM WILL LET YOU KEEP AND ISSUE THE PRESCRIPTION OF YOUR RESPECTIVE CLIENTS.")
print("\t\t\t\tFollowing your diet plan you will remain happy and healthy.")

a = int(input("For Input data press : 1 \nTo retrieve data press : 0\n"))
def getdate():
    import datetime
    return datetime.datetime.now()
v = getdate()
def Food1(name, age, weight, contact):
    while True:
        try:
            b = int(input("Number of food items to be listed - "))
        except:
            print("Sorry invalid input! Please try again.")
            continue 
        else:
            break
    
    if os.path.exists(name+contact+"food.txt") == False:
        f = open(name+contact+"food.txt", "x")
        f = open(name+contact+"food.txt", "a")
        f.write(f"                               {name}'s FITTNESS PRESCRIPTION          \n"
                f"              Phone : +91 7988091986           Email : codingcomrade@gmail.com\n"
                f"              _____________________________________________________________________\n"
                f"                                    Client's Details             \n\n"
                f"                   Name : {name}      Age : {age}     Sex : {gender}    \n\n"         
                f"                      Weight : {weight} kg        Height : {height} m\n\n"
                f"                      Phone : {contact}          Date and Time : {v}\n\n"  
                f"                                      BMI : {bmi}     \n"
                f"              _____________________________________________________________________\n")
        f.close()
    
    for i in range(1, b+1):
        g = input(f"Enter food item no {i} in list: ")
        f = open(name+contact+"food.txt", "a")
        f.write(str(g)+"\n\n")
    f.close()

def Exercise1(name, age, weight, contact):
    while True:
        try:
            c = int(input("Number of Exercises to be listed - "))
        except:
            print("Sorry invalid input! Please try again.")
            continue 
        else:
            break
            
    
    if os.path.exists(name+contact+"ex.txt") == False:
        h = open(name+contact+"ex.txt", "x")
        h = open(name+contact+"ex.txt", "a")
        h.write(f"                               {name}'s' FITTNESS PRESCRIPTION          \n"
                f"              Phone : +91 7988091986           Email : codingcomrade@gmail.com\n"
                f"              ____________________________________________________________________\n"
                f"                                    Client's Details             \n\n"
                f"                   Name : {name}      Age : {age}     Sex : {gender}    \n\n"         
                f"                      Weight : {weight} kg        Height : {height} m\n\n"
                f"                      Phone : {contact}          Date and Time : {v}\n\n"  
                f"                                      BMI : {bmi}     \n"
                f"              _____________________________________________________________________\n")
        h.close()
    
    for j in range(1, c+1):
        d = input(f"Enter Exercise no {j} in list: ")
        h = open(name+contact+"ex.txt", "a")
        h.write(str(d)+"\n\n")
    h.close()

def Foodr(namer, contactr):
    
    if os.path.exists(namer+contactr+"ex.txt") == False:
        print("You haven't logged in Diet")
    else:
        t = open(namer+contactr+"food.txt", "r")
        print(t.read())
        t.close()

def Exerciser(namer, contactr):
    
    if os.path.exists(namer+contactr+"ex.txt") == False:
        print("You haven't logged in Exercises")
    else:
        y = open(namer+contactr+"ex.txt", "r")
        print(y.read())
        y.close()
        
def BMIdiet(bmi):
    food_for_less_bmi = ["Glass of milk with two boiled eggs", "Raisin bran cereals", "Bananas", "Avocados","Sweet potatoes", "Peas", "Yogurt", "Milk,salmon", "Tuna", "Tofu", "Beans", "Nuts", "Seeds"]
    food_for_more_bmi = ["Vegetables: Greens, cauliflower, herbs, carrots, peppers, garlic, eggplant", "Fruits: Apples, strawberries, mango, papaya, banana, grapes", 
                         "Grains: Oats, millet, quinoa, whole-grain breads, brown rice", "Legumes: Lentils, pulses, beans","Dairy: Cheese, yogurt, milk, kefir, ghee"]
    food_for_normal_bmi = []
    if bmi < 18.5:
        print("\nConsider the following food items also for client's diet :-\n")
        for i in food_for_less_bmi:
            print(i)
    elif bmi >= 18.5 and bmi <= 24.9:
        print("\nYour BMI is perfect. Follow you trainer's advise.\n")
    else:
        print("\nConsider the following food items also for client's diet :-\n")
        for i in food_for_more_bmi:
            print(i)
            
def BMIexercise(bmi):
    ex_for_less_bmi = ["Squats", "Push-ups", "Bench Dips", "Lunges", "Crunches", "Glute Kickback", "Pull-Ups", "Bench Press", "Deadlift", "Burpees"]
    ex_for_more_bmi = ["Walking", "Jogging/running", "Cycling", "Weight training", "Interval training", "Swimming", "Yoga", "Pilates"]
    ex_for_normal_bmi = ["Side Leg Lifts", "Bridges", "Knee Lifts With Ball", "Modified Squats", "Stationary Bike", "Water Aerobics","Yoga"]
    if bmi < 18.5:
        print("\nAlso consider the following exercises. These are according to the client's BMI.\n")
        for i in ex_for_less_bmi:
            print(i)
    elif bmi >= 18.5 and bmi <= 24.9:
        print("\nAlso consider the following exercises. These are according to the client's BMI.\n")
        for i in ex_for_normal_bmi:
            print(i)
    else:
        print("\nAlso consider the following exercises. These are according to the client's BMI.\n")
        for i in ex_for_more_bmi:
            print(i)
    Weight_training = ["Circuit Training", "Squat + Curl", "Push Ups", "Dumbbell Row + Fly", "Bench Step Ups", "Lunge + Front Raise", "Renegade Rows", "Incline Dumbbell Press"]
    print("For Weight Training these exercise must be prescribed: ", Weight_training)

        

if a == 1:
    wl = int(input("Log Diet : 1, Log Exercise : 0 - "))
    name = input("Enter Client's name - ")
    age = input("Enter Clients Age: ")
    weight = float(input("Please Enter Client's WEIGHT - "))
    height = float(input('Please enter your height input meters(decimals): '))
    bmi = weight/(height*height)
    gender = input("Gender: ")
    contact = input("Enter Client's Mobile number: ")
    
    if wl == 1:
        BMIdiet(bmi)
        Food1(name, age, weight, contact)
        dd = input("Do you want to log Exercise? (yes/no)")
        if dd == "yes":
            BMIexercise(bmi)
            Exercise1(name, age, weight, contact)      
    elif wl == 0:
        BMIexercise(bmi)
        Exercise1(name, age, weight, contact)
        de = input("Do you want to log Diet? (yes/no)")
        if de == "yes":
            BMIdiet(bmi)
            Food1(name, age, weight, contact) 

elif a == 0:
    wr = int(input("Retrieve Diet : 1, Retrieve Exercise : 0 - "))
    namer = input("Enter Client's name - ")
    contactr = (input("Please anter your Contact no. - "))
    
    if wr == 1:
        Foodr(namer, contactr)
        drd = input("Do you want to retrieve Exercise? (yes/no)")
        if drd == "yes":
            Exerciser(namer, contactr)
    elif wr == 0:
        Exerciser(namer, contactr)
        dre = input("Do you want to retrieve Diet? (yes/no)")
        if dre == "yes":
            Foodr(namer, contactr)

            
print("\t\t\t\t\tNOTE!!! To DELETE a logged data please open the prescription.\n")
print("\t\t\t\t\tThank You for making use of our Diet and Exercise Management System")