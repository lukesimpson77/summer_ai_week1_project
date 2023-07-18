# A class to hold general system wide social media data and functions. Eg Data objects of all people, Eg functions: Save social media to disk
class SocialNetwork:
    def __init__(self):
        self.list_of_people = [] # this instance variable is initialized to an empty list when social network is created, 
                                 # you can save objects of people on the network in this list
        
    ## For more challenge try this
    def save_social_media(self):
        # function to save social media to a file on disk 
        # hint: look up how to use python's inbuil json module to turn objects to json
        # you can write this json unto a file on disk
        pass 

    ## For more challenge try this
    def reload_social_media(self):
        # function to load saved social media from file on disk 
        # hint: load a the json file from disk and look up how to recreate the list of people objects.
        pass

    def  create_account(self):
        ##implement function that creates account here
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        person = Person(name, age)
        self.list_of_people.append(person)
        print("Creating ...")
        
    def view_friends(self, person):
        print("Friend list of", person.id)
        for friend in person.friendlist:
            print(friend.id)

    def view_messages(self, person):
        print("Messages:")
        for message in person.messages:
            print(message)
    

class Person:
    def __init__(self, name, age):
        self.id = name
        self.year = age
        self.friendlist = []
        self.blocked_friends = []
        self.messages = []



    def add_friend(self, person_object):
        if person_object not in self.friendlist:
            self.friendlist.append(person_object)
            print(person_object.id, "added as a friend.")
            
        else:
            print(person_object.id, "is already a friend.")

    def block_friend(self, person_object):
        if person_object in self.friendlist:
            self.friendlist.remove(person_object)
            self.blocked_friends.append(person_object)
            print(person_object.id, "is now blocked.")
        else:
            print(person_object.id, "is not your friend.")



    def send_message(self, person_object):
        message = input("What would you like to say? ")
        if person_object in self.friendlist:
            person_object.messages.append(message)
            print("Message sent to", person_object.id)
        else: 
            print(person_object.id, "is not your friend")

    #def view_messages(self):
        #print("Messages received from friends:")
        #for message in self.messages:
        #    print(message)


    def edit_details(self):
        #implement editing details here
        new_age = input("Enter new age: ")
        new_name = input("Enter new name: ")
        self.year = new_age
        self.id = new_name



