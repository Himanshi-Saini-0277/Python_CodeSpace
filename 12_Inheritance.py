class c:
  def __init__(self, value):
    self.value = value

  def show(self):
    print(f"Value is {self.value}")

class d (c):
  def e(self):
    print("This is a child class")

a = d("Himanshi")
a.show()
a.e()