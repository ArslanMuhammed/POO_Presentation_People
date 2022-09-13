class Person:
    def __init__(self, name: str = "", age: int = 0):
        self.name = name
        self.age = age
        self.AskName()

    def ToIntroduce(self):
        info_person = "Hello my name is " + self.name
        if self.age != 0:
           info_person += f" I'm {self.age} years old"
        print(info_person)
        
        if self.age != 0:
            if self.IsMajor():
                print("I am of legal age")
            else:
                print("I'm a minor")
        print()
        
    def IsMajor(self):
        return self.age >= 18    
        
    def AskName(self):
        if self.name == "":
            self.name = input("What is your name ? ")
            print("The person:", self.name)
            print()



person1 = Person("Franck", 18)
person2 = Person("Jessica", 13)
person3 = Person()
person4 = Person(age=32)

person1.ToIntroduce()
person2.ToIntroduce()
person3.ToIntroduce()
person4.ToIntroduce()