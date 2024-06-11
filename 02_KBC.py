ques = ["What is my name?","What is my age?","What is my favourite color?"]
answer = ["Himanshi","19","Black"]
price = [1000,2000,3000]

for i in range (len(ques)):
  print(ques[i])
  ans = input ("Enter your answer: ")

  if ans == answer[i]:
    print ("Answer is correct! You won ", price[i])

  else :
    print("You lost! Game Over")
    break
