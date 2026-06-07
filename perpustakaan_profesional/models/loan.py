class Loan:

    def __init__(self,member_id, item_id, due_days=7):
        self.__member_id = member_id
        self.__item_id = item_id
        self.__due_days = due_days

    def get_member_id(self):
        return self.__member_id

    def get_item_id(self):
        return self.__item_id

    def get_due_days(self):
        return self.__due_days

    def extend_loan(self, days):
        self.__due_days += days

    def display_loan(self):

        print(f"""
ID Member      : {self.__member_id}
ID Buku        : {self.__item_id}
Sisa Hari      : {self.__due_days}
""")