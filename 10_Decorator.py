def greet(fx):

  def mfx(*args, **kwargs):
    print("Hello")
    fx(*args, **kwargs)
    print("Thanks for using this function")

  return mfx


class m:

  def __init__(self, n, o):
    self.name = n
    self.occu = o

  @greet
  def z(self):
    print(f"{self.name} is a {self.occu}")


b = m("Himanshi", "Developer")
b.z()
