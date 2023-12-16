
from tkinter import *
from tkinter import ttk
from lib.db_conn import *


class Transactions:
    def __init__(self, account_id):
        print('hello')
        self.account_id = account_id
        self.draw_window()

    def draw_window(self):
        bg_color = '#272829'

        root = Tk()
        root.title("Transactions Records")
        root.geometry("850x450")
        style = ttk.Style()
        style.configure("Custom.Treeview",foreground='white')
        style.configure("Custom.Treeview.Heading", font=("Arial", 12, "bold"))

        tree = ttk.Treeview(root, style="Custom.Treeview", columns=("Transaction ID", "Account ID", "Receiver ID", "Amount", "Transaction Date"), show="headings")
        tree.pack(fill="both", expand=True)

        column_widths = [150, 150, 150, 150, 100, 150]

        for i, column in enumerate(("Transaction ID", "Account ID", "Receiver ID", "Amount", "Transaction Date")):
            tree.column(column, width=column_widths[i])
            tree.heading(column, text=column, anchor="w")


        vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=vsb.set)
        vsb.pack(side="right", fill="y")

        hsb = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
        tree.configure(xscrollcommand=hsb.set)
        hsb.pack(side="bottom", fill="x")

        self.populate_treeview(tree)
        root.mainloop()


    def populate_treeview(self,tree):
        cursor = db.cursor()
        cursor.execute(f'select * from transactions where account_id = "{self.account_id}"')
        tree.delete(*tree.get_children())
        for row in cursor:
            tree.insert("", "end", values=row)
        cursor.close()


#Transactions('KOKNUXFNYCRH')