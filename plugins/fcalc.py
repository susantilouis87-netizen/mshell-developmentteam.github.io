# Fungsi untuk operasi dasar
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error! Pembagian dengan nol."
    return x / y

# Tampilkan menu operasi ke pengguna
print("Pilih Operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

while True:
    pilihan = input("\nMasukkan pilihan (1/2/3/4) atau ketik 'q' untuk keluar: ")

    # Cek apakah pengguna ingin keluar
    if pilihan.lower() == 'q':
        print("Keluar dari program. Terima kasih!")
        break

    # Cek apakah pilihan valid
    if pilihan in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka!")
            continue

        if pilihan == '1':
            print(f"Hasil: {num1} + {num2} = {tambah(num1, num2)}")
        elif pilihan == '2':
            print(f"Hasil: {num1} - {num2} = {kurang(num1, num2)}")
        elif pilihan == '3':
            print(f"Hasil: {num1} * {num2} = {kali(num1, num2)}")
        elif pilihan == '4':
            print(f"Hasil: {num1} / {num2} = {bagi(num1, num2)}")
    else:
        print("Pilihan tidak valid. Silakan pilih nomor yang benar.")
