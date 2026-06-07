from models.book import Book
from models.magazine import Magazine
from models.member import Member
from models.loan import Loan

from services.library_service import LibraryService
from services.report_service import ReportService

from utils.helper import garis


library = LibraryService()
while True:

    garis()

    print("SISTEM PERPUSTAKAAN PROFESIONAL")

    garis()

    print("""
1. Transaksi Peminjaman
2. Manajemen Data
3. Keluar
""")

    menu = input("Pilih Menu : ")

    # ==========================
    # TRANSAKSI
    # ==========================

    if menu == "1":

        while True:

            print("""
===== TRANSAKSI =====

1. Pinjam Buku
2. Kembalikan Buku
3. Perpanjang Peminjaman
4. Lihat Peminjaman
5. Kembali
""")

            pilih = input("Pilih : ")

            if pilih == "1":

                member_id = input("ID Member : ")
                item_id = input("ID Buku : ")

                loan = Loan(
                    member_id,
                    item_id
                )

                library.borrow_item(
                    loan
                )

            elif pilih == "2":

                member_id = input("ID Member : ")
                item_id = input("ID Buku : ")

                library.return_item(
                    member_id,
                    item_id
                )

            elif pilih == "3":

                member_id = input("ID Member : ")
                item_id = input("ID Buku : ")

                days = int(
                    input(
                        "Tambah Hari : "
                    )
                )

                library.extend_loan(
                    member_id,
                    item_id,
                    days
                )

            elif pilih == "4":

                library.show_loans()

            elif pilih == "5":

                break

    # ==========================
    # MANAJEMEN DATA
    # ==========================

    elif menu == "2":

        while True:

            print("""
===== MANAJEMEN DATA =====

1. Tambah Buku
2. Tambah Majalah
3. Tambah Member
4. Tampilkan Koleksi
5. Tampilkan Member
6. Update Judul Item
7. Hapus Item
8. Hapus Member
9. Laporan
10. Kembali
""")

            pilih = input("Pilih : ")

            if pilih == "1":

                item_id = input("ID Buku : ")
                title = input("Judul : ")
                author = input("Penulis : ")
                stock = int(
                    input("Stok : ")
                )

                book = Book(
                    item_id,
                    title,
                    author,
                    stock
                )

                library.add_item(book)

            elif pilih == "2":

                item_id = input(
                    "ID Majalah : "
                )

                title = input("Judul : ")

                publisher = input(
                    "Penerbit : "
                )

                edition = input(
                    "Edisi : "
                )

                magazine = Magazine(
                    item_id,
                    title,
                    publisher,
                    edition
                )

                library.add_item(
                    magazine
                )

            elif pilih == "3":

                member_id = input(
                    "ID Member : "
                )

                name = input(
                    "Nama : "
                )

                member = Member(
                    member_id,
                    name
                )

                library.add_member(
                    member
                )

            elif pilih == "4":

                library.show_items()

            elif pilih == "5":

                library.show_members()

            elif pilih == "6":

                item_id = input(
                    "ID Item : "
                )

                title = input(
                    "Judul Baru : "
                )

                library.update_title(
                    item_id,
                    title
                )

            elif pilih == "7":

                item_id = input(
                    "ID Item : "
                )

                library.remove_item(
                    item_id
                )

            elif pilih == "8":

                member_id = input(
                    "ID Member : "
                )

                library.remove_member(
                    member_id
                )

            elif pilih == "9":

                print(
                    "\n=== LAPORAN ==="
                )

                ReportService.total_items(
                    library.get_items()
                )

                ReportService.total_members(
                    library.get_members()
                )

            elif pilih == "10":

                break

    elif menu == "3":

        print(
            "Program selesai"
        )

        break