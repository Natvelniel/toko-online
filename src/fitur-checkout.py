# Program Sederhana Checkout Toko Online

# Daftar Produk
produk_toko = {
    "1": {"nama": "Kaos Polos", "harga": 50000},
    "2": {"nama": "Celana Jeans", "harga": 120000},
    "3": {"nama": "Jaket Hoodie", "harga": 150000},
    "4": {"nama": "Sepatu Sneakers", "harga": 250000}
}

keranjang = []

def tampilkan_menu():
    print("\n--- KATALOG PRODUK ---")
    for kode, data in produk_toko.items():
        print(f"[{kode}] {data['nama']} - Rp {data['harga']:,}")

def tambah_ke_keranjang():
    while True:
        tampilkan_menu()
        pilihan = input("\nMasukkan nomor produk yang ingin dibeli (ketik 'selesai' untuk checkout): ")
        
        if pilihan.lower() == 'selesai':
            break
            
        if pilihan in produk_toko:
            jumlah_str = input(f"Masukkan jumlah {produk_toko[pilihan]['nama']}: ")
            if jumlah_str.isdigit():
                jumlah = int(jumlah_str)
                nama = produk_toko[pilihan]['nama']
                harga = produk_toko[pilihan]['harga']
                subtotal = harga * jumlah
                
                keranjang.append({"nama": nama, "harga": harga, "jumlah": jumlah, "subtotal": subtotal})
                print(f"-> Berhasil menambahkan {jumlah} {nama} ke keranjang.")
            else:
                print("Jumlah harus berupa angka!")
        else:
            print("Pilihan tidak valid, coba lagi.")

def proses_checkout():
    if not keranjang:
        print("\nKeranjang belanjaan Anda masih kosong.")
        return False
        
    print("\n--- RINGkASAN BELANJA (CHECKOUT) ---")
    total_belanja = 0
    for item in keranjang:
        print(f"- {item['nama']} x{item['jumlah']} : Rp {item['subtotal']:,}")
        total_belanja += item['subtotal']
        
    print(f"\nTotal yang harus dibayar: Rp {total_belanja:,}")
    
    while True:
        uang_str = input("Masukkan jumlah uang pembeli (Rp): ")
        if uang_str.isdigit():
            uang_bayar = int(uang_str)
            if uang_bayar >= total_belanja:
                kembalian = uang_bayar - total_belanja
                print(f"Pembayaran berhasil! Uang kembalian: Rp {kembalian:,}")
                print("Terima kasih sudah berbelanja!")
                return True
            else:
                print("Uang Anda kurang! Silakan masukkan jumlah yang cukup.")
        else:
            print("Masukkan nominal angka yang valid!")

# Menjalankan Program
if __name__ == "__main__":
    print("Selamat Datang di Toko Online Sederhana!")
    tambah_ke_keranjang()
    proses_checkout()
