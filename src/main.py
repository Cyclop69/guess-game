import random
s=0
while True:
  
  a=random.randint(1,10)
  b=input("\n\n\nenter a number betweeen 1-10:(if you want to quit type:q):\n")
  if b=="q":
    break
  elif a==int(b):
    print("congrts,you won!")
    s=s+10
    print("your new score: ",s)
  else:
    print("comp chose ",a,"\nyou lost")











