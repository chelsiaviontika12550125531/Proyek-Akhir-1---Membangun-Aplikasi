from models.book import Book
from models.magazine import Magazine
from models.member import Member

from services.library_service import LibraryService
from services.report_service import ReportService

from utils.helper import garis


library = LibraryService()

while True:

    garis()

    print("SISTEM PERPUSTAKAAN PROFESIONAL")

    garis()

    print("""
1. Tambah Buku
2. Tambah Majalah
3. Tambah Member
4. Tampilkan Koleksi
5. Tampilkan Member
6. Update Judul Item
7. Hapus Item
8. Hapus Member
9. Laporan
10. Keluar
""")

    pilihan = input("Pilih Menu : ")

    if pilihan == "1":

        item_id = input("ID Buku : ")
        title = input("Judul : ")
        author = input("Penulis : ")
        stock = int(input("Stok : "))

        book = Book(item_id, title, author, stock)

        library.add_item(book)

    elif pilihan == "2":

        item_id = input("ID Majalah : ")
        title = input("Judul : ")
        publisher = input("Penerbit : ")
        edition = input("Edisi : ")

        magazine = Magazine(
            item_id,
            title,
            publisher,
            edition
        )

        library.add_item(magazine)

    elif pilihan == "3":

        member_id = input("ID Member : ")
        nama = input("Nama : ")

        member = Member(member_id, nama)

        library.add_member(member)

    elif pilihan == "4":

        library.show_items()

    elif pilihan == "5":

        library.show_members()

    elif pilihan == "6":

        item_id = input("ID Item : ")
        title = input("Judul Baru : ")

        library.update_title(item_id, title)

    elif pilihan == "7":

        item_id = input("ID Item : ")

        library.remove_item(item_id)

    elif pilihan == "8":

        member_id = input("ID Member : ")

        library.remove_member(member_id)

    elif pilihan == "9":

        print("\n=== LAPORAN ===")

        ReportService.total_items(
            library.get_items()
        )

        ReportService.total_members(
            library.get_members()
        )

    elif pilihan == "10":

        print("Program selesai")
        break

    else:

        print("Menu tidak tersedia")
