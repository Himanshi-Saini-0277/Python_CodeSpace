class parent :
  def __init__(self, name, age):
    self.name = name
    self.age = age

class child(parent):
  def __init__(self, name, age, lang):
    super().__init__(name,age)
    self.lang = lang

  def __len__(self):
    return len(self.name)

  def __str__(self):
    return f"name is {self.name} and age is {self.age} and language is {self.lang} str"

  def __repr__(self):
    return f"name is {self.name} and age is {self.age} and language is {self.lang} repr"

  def __call__(self):
    print("calling")

a = child("Himanshi", 19, "Python")
print(a.name)
print(a.age)
print(a.lang)
print(len(a))
print(str(a))
print(repr(a))
a()
print(dir(a))
print(a.__dict__)