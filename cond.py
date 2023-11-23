# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output
user_age=int(input('Enter your age: '))               
drive_requir = int((18))
need_years = drive_requir - int(user_age)
if  user_age > 0 and int(user_age) >= drive_requir:
    print(" You are old enough to drive")
else :
    print(" You need", (need_years), "more years to learn drive")

your_age=int(input('Enter your age:'))              
if your_age > 0:
    if your_age >= 18:
         print(" You are old enough to drive")
    else  :
         print(f" You need {18-your_age} more years to learn drive")     
else:
    print("Age should be greater than zero")


# Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:
my_age=25                                                                   
your_age=input('Enter your age:')
if your_age > 0 :
    if my_age < your_age:
        print(f"You are {your_age - my_age} years older than me")
    else :
        print(f"I am {my_age - your_age} years older than you")
    # else:
    #     print(f"I am {my_age - your_age or your_age - my_age} year older than you")
else:
    print(f"We're the same age")
    
#Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:
a=int(input("Enter number one:"))
b=int(input("Enter number two:"))
if a > b:
    print(f"{a} is greater than {b}")
    
elif a < b:
    print(f"{ a }is smaller than { b}")
    
else:
    print(f" a is equal to b")
    

      

#Write a code which gives grade to students according to theirs score
grade=int(input("Enter grade to students :"))
if grade > 0 and grade < 49:
    print("It is F")
elif grade >50 and grade < 59:
    print("It is D")
elif grade >= 60 and grade < 69:
    print("It is C")
elif grade >= 70 and grade < 89:
    print("It is B")
elif grade >= 90 and grade < 100:
    print(f"It is A")
else:
    print("Invalid Input!")

#Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
user_input=input("Enter the mounths:")
if user_input in ('January', 'February', 'March'):
	season = 'winter'
elif user_input in ('April', 'May', 'June'):
	season = 'spring'
elif user_input in ('July', 'August', 'September'):
	season = 'summer'
else:
	season = 'autumn'

print(f" The mounths are {season}")

#If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
fruit_input=input('Enter the any fruits:')
if fruit_input in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(fruit_input)
    print(f"The new fruit add to list {fruits}")

* Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 * If the person is married and if he lives in Finland, print the information in the following format:

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
if person['skills'][2]:
    print(f"Yes, It exists in dictionary {person['skills'][2]}")
else:
    print(f"No, It doesn't exist in dictionary")



if 'Python' in person.get('skills'):
    print(f"Yes, It exists in dictionary {person['skills'][-1]}")
else:
    print(f"No, It doesn't exist in dictionary")



if len(person['skills']) == 2:
    if ('JavaScript' and 'React') in person.get('skills'):
        print('He is a front end developer')
elif ('Node' and 'Python 'and 'MongoDB')  in person.get('skills'):
    print('He is a backend developer') 
elif ('Node' and 'React' and ' MongoDB')  in person.get('skills'):
    print('He is a fullstack developer')
else:
    print('unknown title')

if ('Asabeneh' in person['first_name'] and 'Yetayeh' in person['last_name']) and ( 'Finland' in  person['country'] )and (person['is_marred']) :
    print(f" {person['first_name'][0:8]} {person['last_name'][0:7]} lives in {person['country'][0:7]}.He is married")
else:
    print("Error")


       









    





 
   