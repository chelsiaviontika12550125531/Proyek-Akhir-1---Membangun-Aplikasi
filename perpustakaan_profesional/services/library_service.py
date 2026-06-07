class LibraryService:

    def __init__(self):
        self.__items = []
        self.__members = []
        self.__loans = []

    # ITEM

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, item_id):

        for item in self.__items:
            if item.get_item_id() == item_id:
                self.__items.remove(item)
                return

        print("Item tidak ditemukan")

    def update_title(self, item_id, new_title):

        for item in self.__items:

            if item.get_item_id() == item_id:
                item.set_title(new_title)
                return

    def show_items(self):

        if not self.__items:
            print("Belum ada koleksi")
            return

        for item in self.__items:
            item.display_info()

    def get_items(self):
        return self.__items

    # MEMBER

    def add_member(self, member):
        self.__members.append(member)

    def remove_member(self, member_id):

        for member in self.__members:

            if member.get_member_id() == member_id:
                self.__members.remove(member)
                return

        print("Member tidak ditemukan")

    def show_members(self):

        if not self.__members:
            print("Belum ada member")
            return

        for member in self.__members:
            member.display_member()

    def get_members(self):
        return self.__members
    
    # PEMINJAMAN

    def borrow_item(self, loan):

        self.__loans.append(loan)

        print("Peminjaman berhasil")


    def return_item(self, member_id, item_id):
        for loan in self.__loans:
            if (
                loan.get_member_id() == member_id
                and
                loan.get_item_id() == item_id
            ):
                
                self.__loans.remove(loan)
                print("Buku berhasil dikembalikan")
                return
            
        print("Data peminjaman tidak ditemukan")

    def extend_loan(self,member_id,item_id,days):
        for loan in self.__loans:
            if (
                loan.get_member_id() == member_id
                and
                loan.get_item_id() == item_id
            ):
        
                loan.extend_loan(days)
                print("Peminjaman berhasil diperpanjang")
                return
            
        print("Data tidak ditemukan")


    def show_loans(self):
        if not self.__loans:

            print("Tidak ada peminjaman aktif")
            return
        
        for loan in self.__loans:
            loan.display_loan()
