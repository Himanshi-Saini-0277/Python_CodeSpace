class a :
  age = 0
  def __init__(self, name, num):
    self.name = name
    self.num = num

  def show(self):
    a.age += 1
    print(f"name is {self.name} and age is {self.age}")

  @classmethod
  def show1(cls, z):
    name, num = z.split(",")
    return cls(name, num)

a1 = a("Himanshi",19)
a1.show()
a2 = a("Parshav",18)
a2.show()
z = "Himanshi,19"
a3 = a.show1(z)
print(a3.name, a3.num)