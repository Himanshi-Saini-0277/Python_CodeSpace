a = input ("Enter message: ")
words = a.split(" ")

z = input ("Enter 1 for Coding and 0 for Decoding: ")
coding = (z == "1")

print(coding)

if (coding):
  nwords = []
  for word in words:
    if len(word)>=3:
      b = "abc"
      c = "xyz"
      d = b + word[1:] + word[0] + c
      nwords.append(d)

    else:
      nwords.append(word[::-1])

  print(" ".join (nwords))

else:
  nwords = []
  for word in words:
    if len(word)>=3:
      d = word[3:-3]
      d = d[-1] + d[:-1]
      nwords.append(d)

    else:
      nwords.append(word[::-1])

  print(" ".join (nwords))