

kalit = input("Kalit nomini kiriting: ")

car = {
    "brand": "Chevrolet", 
    "model": "Cobalt", 
    "color": "white",
    "age": 19
}

if kalit in car:
    car.pop(kalit)
    print(car)
else:
    print("Bunday kalit yoq")
