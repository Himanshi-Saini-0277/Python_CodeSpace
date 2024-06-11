import os 
j = 1

for i in os.listdir("photo"):
    os.rename(f"photo/{i}",f"photo/{j}.png")
    j += 1