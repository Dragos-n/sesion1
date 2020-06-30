#Ex.1
def string_split(input_string):
    a = len(input_string)
    if  a%2 != 0: input_string += "_"
    return ([input_string[i:i + 2] for i in range(0, len(input_string), 2)])

input_string="avion"
print(string_split(input_string))

#Ex.2

def reverse_string(input_string):
    result = ""
    for i in range(0,len(input_string.split())):
        result +=" " + "".join(reversed(input_string.split()[i]))
    return result

input_string = "ana are mere rosii!"
print(reverse_string(input_string))

#Ex.3
class Human:
    def create(self):
        print("Human created!")

class Men(Human):
    def Men_create(self):
        print("Men created!")
        super().create()

class Woman(Human):
    def Woman_create(self):
        print("Woman created!")
        super().create()

Adam = Men()
Eve = Woman()

Adam.Men_create()
Eve.Woman_create()