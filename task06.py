k = input()

car = [{
    "brand": "Chevrolet",
    "model": "Cobalt", 
    "color": "white"
}]

for i in car:
    if k in i:
        print(i[k])
    else:
        print("Topilmadi")
