#name = [1 , 4 , "TNT"]
#print (type(name))

#ter = "fHb"
#print (ter.upper())
#print (ter.lower())

#name = "Python"
#print(hasattr(name, "upper"))
#print(hasattr(name, "lower"))
#print(hasattr(name, "title"))

#method = getattr(name, "upper" )
#print(method())

class Cat :
    def __init__(self, sound, age):
        self.sound = sound
        self.age = age
cat = Cat
print(type(Cat))
print(dir(Cat))
print(hasattr(Cat, 'sound'))
print(hasattr(Cat, 'age'))
print(hasattr(Cat, 'sound'))

import sys
print(sys.version)
print(sys.platform)