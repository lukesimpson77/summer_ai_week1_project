#Various import Statements can go here
from  social_network_classes import SocialNetwork,Person
import social_network_ui


name = ""
age = ""
#Create instance of main social network object
ai_social_network = SocialNetwork()
ai_person = Person(name, age)

#The line below is a python keyword to specify which 
if __name__ == "__main__":
    print("########################################################")
    print("          Welcome to Summer AI Social Network")
    print("########################################################")
    last_menu = None
    choice = social_network_ui.mainMenu()

    while True: 
        if choice == "1":
            print("\nYou are now in the create account menu")
            ai_social_network.create_account()

        elif choice == "2":
            inner_menu_choice = social_network_ui.manageAccountMenu()
            #Handle inner menu here
            while True:
                #edit details
                if inner_menu_choice == "1":
                    ai_person.edit_details()

                #add friends
                elif inner_menu_choice == "2":
                    name = input("Enter your name: ")
                    friend_name = input("Enter your friend's name: ")
                    person, friend = None, None
                    for p in ai_social_network.list_of_people:
                        if p.id == name:
                            person = p
                        if p.id == friend_name:
                            friend = p

                    if person and friend:
                        person.add_friend(friend)
                        break
                    else:
                        print("Account not found.")
                        break

                #view all friends
                elif inner_menu_choice == "3":
                    name = input("Enter your name: ")
                    for person in ai_social_network.list_of_people:
                        if person.id == name:
                            ai_social_network.view_friends(person)
                            break
                        
                    else:
                            print("Account not found")
                            break
                    break

                # view messages
                elif inner_menu_choice == "4":
                    name = input("Enter your name: ")
                    for person in ai_social_network.list_of_people:
                        if person.id == name:
                            ai_social_network.view_messages(person)
                            break
                    else:
                            print("Account not found")
                            break
                    break

                # block friends
                elif inner_menu_choice == "5":
                    name = input("Enter your name: ")
                    friend_name = input("Who would you like to block? ")
                    person, friend = None, None
                    for p in ai_social_network.list_of_people:
                        if p.id == name:
                            person = p
                        if p.id == friend_name:
                            friend = p

                    if person and friend:
                        person.block_friend(friend)
                        break
                    else:
                        print("Account not found.")
                        break

                # send messages to friends
                elif inner_menu_choice == "6":
                    name = input("Enter your name: ")
                    friend_name = input("Enter your friend's name: ")
                    person, friend = None, None
                    for p in ai_social_network.list_of_people:
                        if p.id == name:
                            person = p
                        if p.id == friend_name:
                            friend = p

                    if person and friend:
                        person.send_message(friend)
                        break
                    else:
                        print("Account not found.")
                        break
                
                # go back to main menu
                elif inner_menu_choice == "7":
                    break
                else:
                    inner_menu_choice = social_network_ui.manageAccountMenu()

        elif choice == "3":
            print("Thank you for visiting. Goodbye3")
            break

        else:
            print("Your input is invalid. Try Again!")
        
        #restart menu
        choice = social_network_ui.mainMenu()



        
