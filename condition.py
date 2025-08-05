# if = faire quelque chose seulement c'est vrai
# sinon faire autre (else)

age = int(input("veuiller enter votre age: "))


if age >=100:
    print("you are too old sign up!")
elif age >=18:
    print("you are now signed up!")
elif age <0:
    print("you haven't been born yet!")
else:
     print("you must be 18+ to sign up!")    
    