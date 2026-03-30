User_FirstName = input("Enter First Name ").strip().lower()
User_LastName = input("Enter Last Name ").strip().lower()
Names_Buckets = [
    ["kelly", "eyole"],
    ["derick", "kimea"],
    ["john", "doe"],
    ["jane", "smith"],
    ["michael", "johnson"]
]

if [User_FirstName, User_LastName] in Names_Buckets:
    print(f'''
          Welcome Admin 
          {User_FirstName.title()} {User_LastName.title()}''')
else:
    print(f"Sorry, {User_FirstName.title()} {User_LastName.title()}, you are not authorized to access this course.")