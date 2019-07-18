# Here I will create and abstract my monster Class
# Add the attributes in the __init__ method
# add behaviours as individual methods


class Monster():

    home = 'the moon'

    def __init__(self,name, height,skills):
        self.name = name
        self.height
        self.skills

    def eat(self, food='Pizza'):
        return "I NOM NOM NOM " + food

    def sleep(self):
        return 'Zzz'

    def add_skill(self, skill_arg):
        self.skills.append(skill_arg)


    def shout_out_skills_in_interview(self):
        # i need to get the list of skills
# iterate and print out each skill with upper case

skills_list  = self.skills
for skill in skills_list:
    (print(monster1.skills))

monster1 = Monster()
monster1.add_skill('SQL')
monster1.add_skill('Scary Python')

print(monster1)




#
#
#
# # def __init__(self, monster_name, monster_age, monster_colour):
# #
# #       # method called whenever a class has to be initialised , - python calls itself
# #     self.name = monster_name
# #     self.age = monster_age
# #     self.colour = monster_colour
#
# # since the function is inside the class it is a method
#
#
#     def eat(self, food='Pizza'):
#          return "I NOM NOM NOM " + food
#
#     def
#
# monster1 = Monster()
# print(monster1)
# print(type(monster1))
#
#
# print(monster1.eat())
#
#
# monster2 = Monster('Markson')
#
# monster3 = Monster('Markson')
#
#
#
# print(monster2)
# print(monster2.eat("Chicken"))
#
# print(monster1.home)
#
# monster1.home = "Switzerland"
# print(monster1.home)
#
# Monster.home = "Russia"
#
# print(monster1.name)
# print(monster2.name)
# print(monster3.name)