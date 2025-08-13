# Labo 00 – Infrastructure (Git, Docker, CI/CD)
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Ets_quebec_logo.png" width="250">    
ÉTS - LOG430 - Architecture logicielle - Chargé de laboratoire: Gabriel C. Ullmann, Automne 2025.    

## 🎯 Objectifs d’apprentissage

- Comprendre comment utiliser des conteneurs avec **Docker**.
- Apprendre à écrire et exécuter des tests automatisés avec **pytest**.
- Mettre en place un pipeline **CI/CD** avec **GitLab** et **Docker**.
- Savoir combiner les outils de développement modernes (VS Code, **Git**, **Docker**) pour lancer un cycle de développement logiciel.

---

## ⚙️ Setup

### 1. Faites un fork et clonez le dépôt GitLab

```bash
git clone https://github.com/guteacher/log430-a25-labo0
cd log430-a25-labo0
```

### 2. Lancez le conteneur Docker

```bash
docker compose up -d
```

Vérifiez que le conteneur est bien lancé :

```bash
docker ps
```

### 3. Créez un environnement virtuel Python sur votre ordinateur (pas dans Docker)

#### Sur Linux/Mac
```bash
python -m venv .venv/labo0
source .venv/labo0/bin/activate
```

#### Sur Windows
```bash
python -m venv .venv/labo0
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser # Si nécessaire
.venv\labo0\Scripts\activate.ps1
```

### 4. Créez un fichier .env
Ce fichier est dans .gitignore et ne sera donc pas envoyé au système de contrôle de version, afin de préserver la confidentialité de nos informations de connexion à la base de données.

```bash
DB_HOST=localhost
DB_NAME=mydb
DB_USERNAME=user
DB_PASSWORD=pass
```

### 5. Installez les dépendances Python

```bash
pip install -r requirements.txt
```

### 6. Lancez l’application

```bash
cd src
python main.py
```

### 7. Exposez la porte 3306 (MySQL) du conteneur à la machine hôte

```yaml
ports:
  - "3306:3306"  
```

### 8. Re-lancez le conteneur Docker

```bash
docker compose down
docker compose up -d
```
---

## 🧪 Activités

### 1. Écrivez les tests

Dans le fichier `test_main.py`, écrivez des tests pour les fonctions définies dans `main.py`.

```python
def test_addition():
    assert addition(2, 3) == 5
```
Pour lancer les tests localement:

```bash
pytest
```

Si cela ne marche pas dans votre environnement, vous pouvez essayer:
```bash
python3 -m pytest
```

### 2. Ajoutez une étape à la pipeline CI (intégration continue)

Ajoutez une étape (step) dans `.github/workflows/.gitlab-ci.yml` pour que GitLab exécute les tests automatiquement à chaque push. Utilisez la même commande de test de l'activité 1.

### 3. Versionnez votre code

Si tous les tests passent :

```bash
git add .
git commit -m "Ajout des tests pour main.py"
git push
```

Gitlab éxecutera les tests dans son serveur, et ils devront passer également si ils sont corrects.

> 💡 Réfléchissez : en plus des tests, quelles autres étapes sont nécessaires pour garantir qu’un logiciel sera correctement déployé et qu’il ne contiendra pas de bugs majeurs pouvant interrompre son fonctionnement ?

### 5. Extra: CD
Après l'execution de tests, déployez l'appli dans le conteneur via SSH.

---

## 📦 Livrables

- Code compressé en `.zip` contenant l'ensemble du code source du projet Labo 00
- Rapport **PDF** répondant aux questions suivantes :
  1. Quels sont les bénéfices de l’utilisation des conteneurs dans un environnement de production et de développement ?
  2. Vous avez écrit des tests unitaires pour des opérations très simples (addition, soustraction, etc.). Quelle est l’importance des tests à mesure que l’on développe des opérations plus complexes, et aussi lorsqu’on travaille en équipe ?
  3. Est-ce que ça vaut la peine de mettre en place un pipeline CI/CD dès le début du développement d’une application, ou vaut-il mieux attendre que l’application ait atteint une certaine maturité ?



