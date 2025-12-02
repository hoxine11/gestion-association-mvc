# 🕌 Gestion Association Coranique - Architecture MVC Professionnelle

Système complet de gestion d'association coranique utilisant l'architecture MVC (Model-View-Controller) avec **Design Patterns avancés**, FastAPI, et interface web moderne en arabe.

## 📋 Description

Application professionnelle de gestion d'association coranique permettant de gérer:
- 👥 **Membres** - Inscription et gestion des élèves
- 👨‍🏫 **Instructeurs** - Gestion des enseignants et leurs spécialités (Tajweed, Tahfidh, Tafsir)
- 🎯 **Activités/Dورات** - Création et suivi des cours coraniques
- 📝 **Abonnements** - Gestion des inscriptions
- 🕌 **Mواقيت الصلاة** - Horaires de prière en temps réel
- 📊 **Dashboard** - Tableau de bord avec statistiques

## 🏗️ Architecture & Design Patterns

Le projet implémente l'architecture **MVC** avec **2 Design Patterns professionnels**:

### 1️⃣ Repository Pattern
**Objectif**: Séparer la logique d'accès aux données de la logique métier.

**Bénéfices**:
- ✅ Centralisation de l'accès aux données
- ✅ Facilite le changement de source de données (CSV → MySQL)
- ✅ Code plus maintenable et testable
- ✅ Respect des principes SOLID

**Implémentation**:
