from user import UserClass

class Login:
    __db = []
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome User")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
    def create_user(self, name, email, password):
        new_user = UserClass(name, email, password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self, email, password):
        temp=self.__db.copy()
        for user_obj in temp:
            if email == user_obj.email:
                if password == user_obj.get_user_password():
                    return True
                else:
                    return False
            return False

obj = Login()
while True:
    option = input("Enter your choice: ")
    if option == '1':
        name = input("Enter your full name: ")
        valid=False
        while(valid==False):
            email = input("Enter Email: ")
            if(email[0].isalpha()):
                if(email[-10:]=="@gmail.com" or email[-10:]=="@yahoo.com"):
                    print("valid Email")
                    valid==True
                else:
                    print("invalid extension")
            else:
                print("user name must start with alphabet")

        password = input("create new password: ")
        res = obj.create_user(name,email, password)
        if res == True:
            print("User created successfully")
    elif option == '2':
        email=input("Enter email: ")
        password=input("Enter password: ")
        if obj.validate_user(email,password):
            print("Login sucess")
        else:
            print("Login failed")
    elif option == '3':
        break
    else:
        print("Invalid Input")

