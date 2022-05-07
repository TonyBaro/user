class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, sep="\n")
    
    def enroll(self):
        if self.is_rewards_member == False:
            self.is_rewards_member = True
            self.gold_card_points = self.gold_card_points + 200
        else:
            print(f'{self.first_name} is already a user')

    def spend_points(self, points):
        if points <= self.gold_card_points:
            self.gold_card_points -= points
            print(f'{self.first_name}s current point balance is {self.gold_card_points}')
        else:
            print("You dont have enough points for that")




tony = User("Tony", "Baro", "tonybaromagic@gmail.com", 32)
ben = User("Ben", "Reyes", "breyes@hotmail.com", 25)
cheebo = User("Cheebo", "Beebo", "cheebohatesbadcode@gmail.com", 1)

print (tony.first_name)
print (tony.age)
tony.display_info()
tony.enroll()
print(tony.is_rewards_member, tony.gold_card_points, sep="\n")
tony.spend_points(50)
ben.enroll()
ben.spend_points(80)
tony.display_info()
ben.display_info()
cheebo.display_info()
tony.enroll()
cheebo.spend_points(40)
