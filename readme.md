# 🏛️ Gestion Association - MVC Architecture

Système de gestion d'association utilisant l'architecture MVC (Model-View-Controller) avec FastAPI et interface web moderne.

## 📋 Description

Application complète de gestion d'association permettant de gérer:
- 👥 **Membres** - Inscription et gestion des membres
- 👨‍🏫 **Instructeurs** - Gestion des instructeurs et leurs spécialités
- 🎯 **Activités** - Création et suivi des activités
- 📝 **Abonnements** - Gestion des abonnements membres-activités

## 🏗️ Architecture

Le projet suit l'architecture **MVC (Model-View-Controller)**:

```
mvc/
├── data/                   # Données (CSV)
│   ├── members.csv
│   ├── instructors.csv
│   ├── activities.csv
│   └── subscriptions.csv
├── models/                 # Modèles de données
│   ├── base_model.py
│   ├── member.py
│   ├── instructor.py
│   ├── activity.py
│   └── subscription.py
├── controllers/            # Logique métier
│   ├── member_controller.py
│   ├── instructor_controller.py
│   ├── activity_controller.py
│   └── subscription_controller.py
├── views/                  # Vues
│   ├── api.py             # API REST
│   └── web/
│       └── index.html     # Interface web
├── utils/                  # Utilitaires
│   └── csv_loader.py
└── main.py                # Point d'entrée
```

## 🚀 Installation

### Prérequis
- Python 3.8+
- pip

### Étapes

1. **Cloner le repository**
```bash
git clone https://github.com/hoxine11/gestion-association-mvc.git
cd gestion-association-mvc
```

2. **Créer un environnement virtuel (optionnel mais recommandé)**
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

## ▶️ Utilisation

### Lancer le serveur

```bash
uvicorn main:app --reload
```

### Accéder à l'application

- **Interface Web**: http://127.0.0.1:8000
- **Documentation API (Swagger)**: http://127.0.0.1:8000/docs
- **API Alternative (ReDoc)**: http://127.0.0.1:8000/redoc

## 📡 API Endpoints

### Membres
- `GET /api/members` - Récupérer tous les membres
- `POST /api/members` - Ajouter un membre
- `DELETE /api/members/{id}` - Supprimer un membre

### Instructeurs
- `GET /api/instructors` - Récupérer tous les instructeurs
- `POST /api/instructors` - Ajouter un instructeur
- `DELETE /api/instructors/{id}` - Supprimer un instructeur

### Activités
- `GET /api/activities` - Récupérer toutes les activités
- `POST /api/activities` - Ajouter une activité
- `DELETE /api/activities/{id}` - Supprimer une activité

### Abonnements
- `GET /api/subscriptions` - Récupérer tous les abonnements
- `GET /api/subscriptions/member/{id}` - Abonnements d'un membre
- `POST /api/subscriptions` - Ajouter un abonnement
- `DELETE /api/subscriptions/{id}` - Supprimer un abonnement

## 💻 Technologies Utilisées

- **Backend**: FastAPI (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Stockage**: CSV
- **Architecture**: MVC (Model-View-Controller)

## ✨ Fonctionnalités

- ✅ Interface web moderne et responsive
- ✅ API REST complète
- ✅ Opérations CRUD sur toutes les entités
- ✅ Validation des données
- ✅ Notifications en temps réel
- ✅ Confirmation avant suppression
- ✅ Design moderne avec animations

## 📸 Screenshots

### Interface principale
![Dashboard](screenshots/dashboard.png)

### Gestion des membres
![Membres](screenshots/members.png)

## 🤝 Contribution

Les contributions sont les bienvenues! N'hésitez pas à:
1. Fork le projet
2. Créer une branche (`git checkout -b feature/amelioration`)
3. Commit vos changements (`git commit -m 'Ajout fonctionnalité'`)
4. Push vers la branche (`git push origin feature/amelioration`)
5. Ouvrir une Pull Request

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👤 Auteur

**Hoxine11**
- GitHub: [@hoxine11](https://github.com/hoxine11)

## 🙏 Remerciements

Projet réalisé dans le cadre du TP "Implementation Methods and Technology" - Architecture MVC.

---

⭐ N'oubliez pas de mettre une étoile si ce projet vous a été utile!