from tkinter import messagebox
from model.administrator_model import Administrator
import json

# Chemin du fichier JSON
json_file_path = 'Data/accounts.json'

class administrator_controller:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)
        self.administrator = Administrator(id=1, name='Admin', lastname='Admin', email='admin@example.com', password='admin', function='Administrator')
        self.file_path = {
            'customer': 'Data/accounts.json',
            'planes': 'Data/planes.json',
            'airports': 'Data/airports.json'
        }
        self.json_file_path = self.file_path['client']

    def create_object(self, object, object_type):
        self.administrator.create(object, self.file_path[object_type])

    def delete_object(self, object_id, object_type):
        self.administrator.delete(object_id, self.file_path[object_type])

    def edit_object(self, object_id, new_details, object_type):
        self.administrator.edit(object_id, new_details, self.file_path[object_type])

    def see_object(self, object_type):
        return self.administrator.see(self.file_path[object_type])

    def display_message(self, message):
        messagebox.showinfo("Information", message)
    
    # Charger les comptes clients depuis le fichier JSON
    
    def upload_accounts(self):
        try:
            with open(self.json_file_path, 'r') as file:
                accounts = json.load(file)
            print("Comptes chargés :", accounts)  # Ajouter cette ligne pour vérifier le contenu des comptes
            return accounts
        except FileNotFoundError:
            messagebox.showerror("Erreur", "Le fichier de comptes n'existe pas.")
            return []
        except json.JSONDecodeError:
            messagebox.showerror("Erreur", "Erreur de décodage JSON.")
        return []
    
    
    
    def see_accounts(self):
        accounts = self.upload_accounts()
        self.view.view_accounts(accounts)

    def edit_accounts(self, account_id, new_details):
        accounts = self.upload_accounts()
        for accounts in accounts:
            if accounts['id'] == account_id:
                accounts.update(new_details)
                break
        with open(json_file_path, 'w') as file:
            json.dump(accounts, file, indent=4)
        self.see_accounts()

    def delete_accounts(self, account_id):
        account = self.upload_accounts()
        account = [account for account in account if account['id'] != account_id]
        with open(json_file_path, 'w') as file:
            json.dump(account, file, indent=4)
        self.see_accounts()
        
    def create_account(self, name, lastname, email, password, function):
        try:
            accounts = self.upload_accounts()
            new_id = max(accounts['id'] for account in accounts) + 1 if accounts else 1
            new_account = {
                'id': new_id,
                'nom': name,
                'prenom': lastname,
                'email': email,
                'mdp': password,
                'type': function
            }
            accounts.append(new_account)
            with open(json_file_path, 'w') as file:
                json.dump(accounts, file, indent=4)
            self.see_accounts()
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création du compte : {e}")
