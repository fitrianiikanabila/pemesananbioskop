class Film:
    def _init_(self, id_film, nama, harga):
        self.id_film = id_film
        self.nama = nama
        self.harga = harga

class Tiket:
    def _init_(self, id_tiket, nama_film, nama_pemesan, jumlah, total_harga):
        self.id_tiket = id_tiket
        self.nama_film = nama_film
        self.nama_pemesan = nama_pemesan
        self.jumlah = jumlah
        self.total_harga = total_harga

class Bioskop:
    def _init_(self):
        self.films = []
        self.tikets = []
        self.next_tiket_id = 1

    def tambah_film(self, id_film, nama, harga):
        film = Film(id_film, nama, harga)
        self.films.append(film)

    def tampilkan_daftar_film(self):
        if not self.films:
            print("Tidak ada film yang tersedia.")
            return
        print("Daftar Film:")
        for film in self.films:
            print(f"ID: {film.id_film}, Nama: {film.nama}, Harga: Rp{film.harga}")

    def pesan_tiket(self, nama_film, nama_pemesan, jumlah):
        for film in self.films:
            if film.nama.lower() == nama_film.lower():
                total_harga = film.harga * jumlah
                tiket = Tiket(self.next_tiket_id, nama_film, nama_pemesan, jumlah, total_harga)
                self.tikets.append(tiket)
                print(f"Tiket berhasil dipesan. ID Tiket: {self.next_tiket_id}, Total Harga: Rp{total_harga}")
                self.next_tiket_id += 1
                return
        print("Film tidak ditemukan.")

    def lihat_pesanan(self):
        if not self.tikets:
            print("Belum ada tiket yang dipesan.")
            return
        print("Daftar Pesanan Tiket:")
        for tiket in self.tikets:
            print(f"ID Tiket: {tiket.id_tiket}, Film: {tiket.nama_film}, Pemesan: {tiket.nama_pemesan}, Jumlah: {tiket.jumlah}, Total Harga: Rp{tiket.total_harga}")

    def hapus_pesanan(self, id_tiket):
        for tiket in self.tikets:
            if tiket.id_tiket == id_tiket:
                self.tikets.remove(tiket)
                print(f"Pesanan dengan ID Tiket {id_tiket} berhasil dihapus.")
                return
        print("Pesanan tidak ditemukan.")

# Program Utama
bioskop = Bioskop()

# Tambahkan beberapa film awal
bioskop.tambah_film(1, "Avatar: The Way of Water", 50000)
bioskop.tambah_film(2, "Spider-Man: No Way Home", 45000)
bioskop.tambah_film(3, "The Batman", 55000)

while True:
    print("\n--- Sistem Pemesanan Tiket Bioskop ---")
    print("1. Tampilkan Daftar Film")
    print("2. Pesan Tiket")
    print("3. Lihat Pesanan Tiket")
    print("4. Hapus Pesanan Tiket")
    print("5. Keluar")
    
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        bioskop.tampilkan_daftar_film()
    elif pilihan == "2":
        nama_film = input("Masukkan nama film: ")
        nama_pemesan = input("Masukkan nama pemesan: ")
        jumlah = int(input("Masukkan jumlah tiket: "))
        bioskop.pesan_tiket(nama_film, nama_pemesan, jumlah)
    elif pilihan == "3":
        bioskop.lihat_pesanan()
    elif pilihan == "4":
        id_tiket = int(input("Masukkan ID tiket yang akan dihapus: "))
        bioskop.hapus_pesanan(id_tiket)
    elif pilihan == "5":
        print("Terima kasih telah menggunakan sistem pemesanan tiket bioskop.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")