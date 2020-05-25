from dbhelper import DBHelper
def main():
    db=DBHelper()
    while True:
        print("*****welcome******")
        print()
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete user")
        print("Press 4 to update user")
        print("Press 5 to exit program")
        print()
        try:
            choice=int(input())
            if(choice==1):
                #insert user
                uid=int(input("Enter user id:"))
                username=input("Enter user name:")
                userphone=input("Enter user phone:")
                db.insert_user(uid,username,userphone)

                pass
            elif choice==2:
                #display user
                db.fetch_all()
                pass
            elif choice==3:
                #delete user
                userid=int(input("Enter user id which u want to delete:"))
                db.delete_user(userid)
                pass
            elif choice==4:
                #update user
                uid = int(input("Enter id of user:"))
                username=input("new name:")
                userphone=input("new phone:")
                db.update_user(uid,username,userphone)

                pass
            elif choice==5:
                break
            else:
                print("Invalid input ! Try again")
        except Exception as e:
            print(e)
            print("Invalid details ! Try again")

if __name__ == "__main__":
    main()

# helper=DBHelper()
# #helper.insert_user(1452,"dipu","8145596279")
# #helper.delete_user(1452)
# helper.fetch_all()
# helper.update_user(1452,'papay','79084678')
# helper.fetch_all()
