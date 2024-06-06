import tkinter as tk
from tkinter import messagebox, ttk

class AdministratorView:
    def __init__(self, root):
        self.root = root
        self.root.title("Administration")
        self.root.geometry('600x600')
        self.root['bg'] = 'white'
        self.controller = None

        # Création des sections
        self.create_section("Pilotes", [
            ("Ajouter un pilote", lambda: self.controller.show_message("Ajouter un pilote")),
            ("Modifier pilote", lambda: self.controller.show_message("Modifier un pilote")),
            ("Supprimer pilote", lambda: self.controller.show_message("Supprimer un pilote")),
            ("Voir les pilotes", lambda: self.controller.show_message("Voir les pilotes"))
        ])
        self.create_section("Avions", [
            ("Ajouter un avion", lambda: self.controller.show_message("Ajouter un avion")),
            ("Modifier avion", lambda: self.controller.show_message("Modifier un avion")),
            ("Supprimer avion", lambda: self.controller.show_message("Supprimer un avion")),
            ("Voir les avions", lambda: self.controller.show_message("Voir les avions"))
        ])
        self.create_section("Aéroports", [
            ("Ajouter un aéroport", lambda: self.controller.show_message("Ajouter un aéroport")),
            ("Modifier aéroport", lambda: self.controller.show_message("Modifier un aéroport")),
            ("Supprimer aéroport", lambda: self.controller.show_message("Supprimer un aéroport")),
            ("Voir les aéroports", lambda: self.controller.show_message("Voir les aéroports"))
        ])
        self.create_section("Comptes", [
            ("Créer un compte", lambda: self.open_account_creation_window()),
            ("Modifier compte", lambda: self.modify_selected_account()),
            ("Supprimer compte", lambda: self.delete_selected_account()),
            ("Voir les comptes", lambda: self.controller.view_accounts())
        ])

    def set_controller(self, controller):
        self.controller = controller
    
    def create_section(self, title, buttons):
        frame = tk.Frame(self.root, bg='white')
        frame.pack(pady=10)

        tk.Label(frame, text=title, bg='white', font=("Helvetica", 12, "bold")).grid(row=0, columnspan=len(buttons), pady=5)

        for i, (text, command) in enumerate(buttons):
            tk.Button(frame, text=text, command=command).grid(row=1, column=i, padx=5, pady=5)

    def open_account_creation_window(self):
        window_creation = tk.Toplevel(self.root)
        window_creation.title("Créer un compte")
        window_creation.geometry('400x350')
        window_creation['bg'] = 'white'

        # Création des widgets de la fenêtre de création de compte
        labels_entries = [
            ("Nom:", tk.Entry(window_creation)),
            ("Prénom:", tk.Entry(window_creation)),
            ("Email:", tk.Entry(window_creation)),
            ("Mot de passe:", tk.Entry(window_creation, show='*')),
        ]

        for text, entry in labels_entries:
            tk.Label(window_creation, text=text, bg='white').pack(pady=5)
            entry.pack(pady=5)

        label_type = tk.Label(window_creation, text="Type de compte:", bg='white')
        label_type.pack(pady=5)
        combo_type = ttk.Combobox(window_creation, values=['client', 'pilote', 'admin'])
        combo_type.pack(pady=5)
        combo_type.current(0)

        button_create = tk.Button(window_creation, text="Créer", command=lambda: self.controller.creer_compte(
            labels_entries[0][1].get(),
            labels_entries[1][1].get(),
            labels_entries[2][1].get(),
            labels_entries[3][1].get(),
            combo_type.get()
        ))
        button_create.pack(pady=20)

    def view_accounts(self, accounts):
        self.account_window = tk.Toplevel(self.root)
        self.account_window.title("Liste des comptes")
        self.account_window.geometry('600x400')
        self.account_window['bg'] = 'white'
        
        self.tree = ttk.Treeview(self.account_window, columns=("Nom", "Prénom", "Email", "Type"))
        self.tree.heading("#0", text="ID")
        self.tree.heading("Nom", text="Nom")
        self.tree.heading("Prénom", text="Prénom")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Type", text="Type")
        
        self.tree.column("#0", width=50)
        self.tree.column("Nom", width=100)
        self.tree.column("Prénom", width=100)
        self.tree.column("Email", width=150)
        self.tree.column("Type", width=100)
        
        self.tree.pack(fill=tk.BOTH, expand=True)
        
        for i, account in enumerate(accounts):
            self.tree.insert("", tk.END, text=i+1, values=(account['nom'], account['prenom'], account['email'], account['type_compte']))
    
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
    
        self.selected_account_id = None

    def on_tree_select(self, event):
        selected_item = self.tree.selection()
        if selected_item:
            self.selected_account_id = self.tree.item(selected_item)["text"]

    def modify_selected_account(self):
        if self.selected_account_id is not None:
            account_details = {
                'nom': 'Nouveau Nom',
                'prenom': 'Nouveau Prénom',
                'email': 'nouveau@example.com',
                'type': 'client'
            }
            self.controller.modify_selected_account(self.selected_account_id, account_details)
        else:
            messagebox.showwarning("Attention", "Aucun compte sélectionné.")

    def delete_selected_account(self):
        if self.selected_account_id is not None:
            self.controller.delete_selected_account(self.selected_account_id)
        else:
            messagebox.showwarning("Attention", "Aucun compte sélectionné.")
