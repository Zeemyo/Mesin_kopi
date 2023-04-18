MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

keuntungan = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def get_harga(jenis_coffee):
    """Mengambil harga-harga kopi"""
    return MENU[jenis_coffee]["cost"]


def resources_sufficient(order_ingredients):
    """Mengembalikan true jika bahan bahannya cukup, dan false jika bahannya kurang"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Maaf bahan yang tersedia tidak cukup untuk kopi pesanan anda {item}")
            return False
        else:
            return True


def coins():
    """Mengembalikan total dari koin yang dimasukkan"""
    print(f"Masukkan koin. Tagihan: ${get_harga(pesanan)}")
    total = int(input("Berapa quarter? ")) * 0.25
    total += int(input("Berapa dimes? ")) * 0.1
    total += int(input("Berapa nickels? ")) * 0.05
    total += int(input("Berapa pennies? ")) * 0.01
    return total


def transaksi_berhasil(uang_terima, total_tagihan):
    """Mengembalikan true jika uang yang diterima cukup dari total tagian,
    dan mengembalikan false jika uang terima tidak cukup dari total tagihan"""
    if uang_terima >= total_tagihan:
        kembalian = round(uang_terima - total_tagihan, 2)
        print(f"Kembalian anda adalah {kembalian}.")
        global keuntungan
        keuntungan += total_tagihan
        return True
    else:
        print("Uang yang anda masukkan kurang, dan uang dikembalikan")
        return False


def buat_coffe(nama_minuman, order_ingredients):
    """Mengurangi resource berdasarkan ingredients yang dibutuhka"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Kopi {nama_minuman} anda selesai, silahkan dinikmati☕")


mesin_nyala = True


while mesin_nyala:
    pesanan = input("☕ Kopi apa yang anda mau? (Espresso/Latte/Cappuchino)"
                    "\nOptional"
                    "\n📴 Ketik 'Off untuk mematikan mesin'"
                    "\n💵 Ketik 'Report' untuk mengetahui keuntungan yang sudah di dapatkan"
                    "\n: ").lower()
    if pesanan == "off":
        mesin_nyala = False
    elif pesanan == "report":
        print("Sisah bahan yang tersedia:")
        print(f"Air: {resources['water']}ml")
        print(f"Susu: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Total pendapatan: {keuntungan}")
    else:
        minuman = MENU[pesanan]
        if resources_sufficient(minuman["ingredients"]):
            pembayaran = coins()
            if transaksi_berhasil(pembayaran, minuman["cost"]):
                buat_coffe(pesanan, minuman["ingredients"])

