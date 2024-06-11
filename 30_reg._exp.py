import re

see = r"[a-z]+er"
text = "The clever brown fox jumps over the lazy dog. The clever brown fox jumps over the lazy dog."

match = re.finditer(see, text)
for i in match:
  print(i.span(), text[i.span()[0]:i.span()[1]])