def printMainMenu() :
    inputUser = input("Main Menu : \n 1. Lihat Menu\n 2. Lihat Cart\n 3. Checkout\n 4. Keluar\n\n Pilih Menu : ")
    return inputUser

def printMenu(listMenu,listCart) :
    print("Pilihan Menu : ")
    for i in range(0, len(listMenu)) :
        print(str(i + 1) + ". " + listMenu[i])
    inputUser = input("Mau yang mana? : ")
    qty = int(input("Berapa banyak ? : "))
    cartList[listMenu[int(inputUser)-1]] = qty

def printCart(listMenu) :
    print("Isi Cart : ")
    for i, key in zip(range(len(listMenu.keys())), listMenu.keys()) : #mendapatkan semua keys dalam dict
        print(str(i + 1) + ". " + key + " " + str(listMenu[key]))

def checkout(cartList, hargaList) :
    # while True :
        totalHarga = 0
        print("Item yang dipilih : ")
        for i, key in zip(range(len(cartList.keys())), cartList.keys()) :
            print(str(i + 1) + ". " + key + " " + str(cartList[key]))
            totalHarga += hargaList[key] * cartList[key]
        inputDuit = input("Total Harga Rp. " + str(totalHarga) + "\n\n Duit Anda Berapa? : ")
        if(int(inputDuit) < totalHarga):
            print("Uang Anda Kurang!")
            checkout(cartList, hargaList)
        else :
            print("Kembaliannya : Rp. " + str(int(inputDuit) - totalHarga))
            # break;


listMenu = ["Film Avenger 25"]
listHarga = { "film Avenger": 25}
listCart = { }

while True :
    pilihanUser = printMainMenu()
    if(pilihanUser == "1") :
        printMenu(listMenu, listCart)
    elif(pilihanUser == "2") :
        printCart(listCart)
    elif(pilihanUser == "3") :
        checkout(listCart, listHarga)
        listCart = {}
    elif(pilihanUser == "4") :
        print("Terima Kasih, dan sampai jumpa lagi!!")
        break