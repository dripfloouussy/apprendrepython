# if = faire quelque chose seulement c'est vrai
# sinon faire autre (else)

age = int(input("veuiller enter votre age: "))


if age >= 18:
    print("you are now signed up!")
elif age <0:
        print("you haven't born yet!")
elif age  >100:
          print("you are to old to sign up!")
else:
     print("you must be 18+ to sign up!")    
    