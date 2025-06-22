inventory = {
    "olma": 10,
    "banan": 5,
    "uzum": 12
}

mahsulot = input("Mahsulot nomini kiriting: ")

if mahsulot in inventory:
    print(f"{mahsulot} mavjud, miqdori: {inventory[mahsulot]}")
else:
    inventory[mahsulot] = 0
    print(f"{mahsulot} yoq edi, quantity = 0 qilib qoshildi.")

print("Yangi inventory:", inventory)
