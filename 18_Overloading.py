class Solution:
  def __init__(self, i, j, k):
    self.i = i
    self.j = j
    self.k = k

  def __str__(self):
    return (f"{self.i}i + {self.j}j + {self.k}k")

  def __add__(self, x):
    return Solution(self.i + x.i, self.j + x.j, self.k + x.k)

v1 = Solution(3, 4, 5)
print(v1)
v2 = Solution(1, 2, 9)
print(v2)

print(v1 + v2)