is_hungry = False
burger_lover = True
pizza_lover = True

if (is_hungry and (burger_lover or pizza_lover)):
    print("lets order the food")

elif (is_hungry):
    print("lets go to sleep")

else:
    print("not hungry")