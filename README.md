This project is the project from Nicolas, Ilias,Remond and me...

This project has for goal to create an application to manage an Airline (or more if you want...  ;-))

we wanted to manage customers, pilots, flights in functions of realtime meteo, flights around(for now as a future update) and many more things...

For now, we're still working on it. If you don't see anything, It's normal...
Updates will come soon...
Have a Nice journey on the repo...

Projet Programmation Orienté Objet :

Markdown

Copier le code

FlightSim - Simulateur de Gestion de Vols

Description

FlightSim est une application de gestion de vols simulée, permettant aux administrateurs de gérer les utilisateurs, les vols, les véhicules aériens et les itinéraires. Les utilisateurs peuvent se connecter en tant qu'administrateurs, clients, employés ou pilotes pour accéder à des fonctionnalités spécifiques.

Prérequis

- Python 3.10 ou supérieur
- Pip (pour installer les dépendances)

Installation

1. Clonez ce dépôt de code sur votre machine locale :
    ```bash
    git clone <URL_DE_VOTRE_DEPOT>
    cd FlightSim
    ```

2. Créez un environnement virtuel et activez-le :
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows, utilisez `venv\Scripts\activate`
    ```

3. Installez les dépendances nécessaires :
    ```bash
    pip install -r requirements.txt
    ```

Configuration des fichiers
Assurez-vous que les fichiers suivants sont présents dans le dossier `data` :

`users.json`
```json
[
    {
        "user_id": "A2024",
        "first_name": "Remond",
        "last_name": "Kamsu",
        "email": "rkamsu@poo.be",
        "password": "Administrateur",
        "role": "administrateur",
        "nationality": "American",
        "passport_number": "123456789",
        "address": "123 Main St, Anytown, USA",
        "licence": null
    },
    {
        "user_id": "P0002",
        "first_name": "Maréchal",
        "last_name": "Benjamin",
        "email": "bm@poo.be",
        "password": "1234",
        "role": "pilote",
        "nationality": "",
        "passport_number": "",
        "address": "",
        "licence": "741753789"
    },
    {
        "user_id": "E0003",
        "first_name": "Gédéon",
        "last_name": "Owen",
        "email": "og@poo.be",
        "password": "1234",
        "role": "employé",
        "nationality": "",
        "passport_number": "",
        "address": "",
        "licence": null
    },
    {
        "user_id": "C0004",
        "first_name": "Lucraice",
        "last_name": "Foya",
        "email": "fl@poo.be",
        "password": "1234",
        "role": "client",
        "nationality": "Belge",
        "passport_number": "789654",
        "address": "rue de la broucheterre 135",
        "licence": null
    },
    {
        "user_id": "E0005",
        "first_name": "Premier",
        "last_name": "Nicola",
        "email": "np@poo.be",
        "password": "1234",
        "role": "employé",
        "nationality": "",
        "passport_number": "",
        "address": "",
        "licence": null
    }
]
flights.json
json
Copier le code
[
    {
        "flight_id": 1,
        "airline": "Air France",
        "departure_airport": "Charles de Gaulle",
        "arrival_airport": "Berlin Brandenburg",
        "departure_time": "08:00",
        "arrival_time": "10:00",
        "departure_date": "2024-06-15",
        "arrival_date": "2024-06-15",
        "duration": "2h",
        "price_economy": 100,
        "price_business": 300,
        "stopover": null
    },
    {
        "flight_id": 2,
        "airline": "Lufthansa",
        "departure_airport": "Berlin Brandenburg",
        "arrival_airport": "Charles de Gaulle",
        "departure_time": "12:00",
        "arrival_time": "14:00",
        "departure_date": "2024-06-15",
        "arrival_date": "2024-06-15",
        "duration": "2h",
        "price_economy": 120,
        "price_business": 350,
        "stopover": null
    }
]
aircrafts.json
json
Copier le code
[
    {
        "aircraft_id": "A0001",
        "type": "Boeing 747",
        "airline": "Air France",
        "pilot": "P0001",
        "business_class_seats": 20,
        "economy_class_seats": 300,
        "weight": 400000
    },
    {
        "aircraft_id": "A0002",
        "type": "Airbus A320",
        "airline": "Lufthansa",
        "pilot": "P0002",
        "business_class_seats": 10,
        "economy_class_seats": 150,
        "weight": 200000
    }
]
airlines.json
json
Copier le code
[
    {"id": "1", "name": "Air France"},
    {"id": "2", "name": "Lufthansa"},
    {"id": "3", "name": "British Airways"},
    {"id": "4", "name": "KLM"},
    {"id": "5", "name": "EasyJet"},
    {"id": "6", "name": "Ryanair"},
    {"id": "7", "name": "Iberia"},
    {"id": "8", "name": "Turkish Airlines"},
    {"id": "9", "name": "Alitalia"},
    {"id": "10", "name": "Scandinavian Airlines (SAS)"}
]
cities.json
json
Copier le code
[
    {"city_id": 1, "name": "Paris", "postal_code": "75000", "country": "France"},
    {"city_id": 2, "name": "Berlin", "postal_code": "10115", "country": "Allemagne"},
    {"city_id": 3, "name": "Lisbonne", "postal_code": "1100-001", "country": "Portugal"},
    {"city_id": 4, "name": "Budapest", "postal_code": "1011", "country": "Hongrie"},
    {"city_id": 5, "name": "Londres", "postal_code": "SW1A 1AA", "country": "Grande Bretagne"},
    {"city_id": 6, "name": "Prague", "postal_code": "110 00", "country": "Republique Tchèque"},
    {"city_id": 7, "name": "Rome", "postal_code": "00100", "country": "Italie"},
    {"city_id": 8, "name": "Barcelone", "postal_code": "08001", "country": "Espagne"},
    {"city_id": 9, "name": "Amsterdam", "postal_code": "1012 JS", "country": "Pays Bas"},
    {"city_id": 10, "name": "Dublin", "postal_code": "D02 YX28", "country": "Ireland"},
    {"city_id": 11, "name": "Vienne", "postal_code": "1010", "country": "Australie"},
    {"city_id": 12, "name": "Madrid", "postal_code": "28001", "country": "Espagne"},
    {"city_id": 13, "name": "Cracovie", "postal_code": "31-001", "country": "Pologne"},
    {"city_id": 14, "name": "Reykjavik", "postal_code": "101", "country": "Iceland"},
    {"city_id": 15, "name": "Istanbul", "postal_code": "34122", "country": "Turkey"},
    {"city_id": 16, "name": "Florence", "postal_code": "50123", "country": "Italie"},
    {"city_id": 17, "name": "Copenhague", "postal_code": "1050", "country": "Danemark"},
    {"city_id": 18, "name": "Zagreb", "postal_code": "10000", "country": "Croatie"},
    {"city_id": 19, "name": "Stockholm", "postal_code": "111 52", "country": "Suède"},
    {"city_id": 20, "name": "Thessalonique", "postal_code": "546 25", "country": "Grèce"}
]
Exécution de l'application
1.	Assurez-vous que vous êtes dans l'environnement virtuel et que toutes les dépendances sont installées.
2.	Lancez l'application :
bash
Copier le code
python main.py
Utilisation
Connexion
•	Utilisez les informations d'identification d'un utilisateur pour vous connecter (voir users.json).
Interface Administrateur
•	Créer des utilisateurs (pilote, employé, client) via les formulaires correspondants.
•	Créer des véhicules aériens, des vols et des itinéraires.
•	Voir la liste des pilotes, employés et clients.
Interface Client
•	Recherche des vols en utilisant les critères de recherche (ville de départ et ville d'arrivée).
Interface Employé
•	Voir les informations de l'employé connecté.
Interface Pilote
•	Voir les informations du pilote connecté.
Structure du projet
•	main.py: Point d'entrée de l'application.
•	controller/: Contient les contrôleurs pour gérer la logique de l'application.
•	view/: Contient les vues pour afficher l'interface utilisateur.
•	model/: Contient les modèles de données pour les utilisateurs, vols, véhicules aériens, etc.
•	data/: Contient les fichiers JSON avec les données de l'application.
•	assets/: Contient les images utilisées dans l'application.


