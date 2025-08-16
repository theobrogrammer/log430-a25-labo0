# Labo 00 – Infrastructure (Git, Docker, CI/CD)
<img src="https://upload.wikimedia.org/wikipedia/commons/2/2a/Ets_quebec_logo.png" width="250">    
ÉTS - LOG430 - Architecture logicielle - Chargé de laboratoire: Gabriel C. Ullmann, Automne 2025.    

## 🎯 Objectifs d’apprentissage
- Comprendre comment utiliser des conteneurs avec **Docker**.
- Apprendre à écrire et exécuter des tests automatisés avec **pytest**.
- Mettre en place un pipeline **CI/CD** avec **GitLab** et **Docker**.
- Accéder à un serveur via SSH et vérifier la disponibilité des ressources computationnelles (CPU, RAM, espace disque)
- Savoir combiner les outils de développement modernes (VS Code, **Git**, **Docker**) pour lancer un cycle de développement logiciel.

---

## ⚙️ Setup
Dans ce laboratoire, vous travaillerez sur une application calculatrice de base. Elle est implémentée dans un seul script Python, sans connexion à une base de données ni API pour communiquer avec d’autres applications. 

Cette calculatrice est volontairement très simple afin que nous puissions nous concentrer sur la création et la maintenance d’un pipeline CI/CD. Dans les prochains laboratoires, l’architecture logicielle évoluera progressivement et deviendra plus complexe afin que nous puissions explorer d'autres sujets.

### 1. Faites un fork et clonez le dépôt GitLab

```bash
git clone https://github.com/guteacher/log430-a25-labo0
cd log430-a25-labo0
```

### 2. Lancez le conteneur Docker

```bash
docker compose up -d
```

Vérifie que le conteneur est bien lancé :

```bash
docker ps
```

Pour accéder au conteneur de manière interactive :
```bash
docker exec -it <nom_conteneur> /bin/bash
```

### 3. Créez un environnement virtuel Python sur votre ordinateur

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

### 4. Installez les dépendances Python

```bash
pip install -r requirements.txt
```

### 5. Lancez l’application

```bash
cd src
python calculator.py
```

---

## 🧪 Activités

### 1. Écrivez les tests

Dans le fichier `test_calculator.py`, écrivez des tests pour les fonctions définies dans `calculator.py`.

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

> 💡 Question 1 : Si l’un des tests échoue à cause d’un bug, comment pytest signale-t-il l’erreur et aide-t-il à la localiser ? Rédigez un test qui provoque volontairement une erreur, puis montrez la sortie du terminal obtenue.

### 2. Ajoutez une étape à la pipeline CI (intégration continue)

Ajoutez une étape (step) dans `.github/workflows/.gitlab-ci.yml` pour que GitLab exécute les tests automatiquement à chaque push. 

### 3. Versionnez votre code

Si tous les tests passent :

```bash
git add .
git commit -m "Tests pour calculator.py"
git push
```

Gitlab éxecutera les tests dans son serveur, et ils devront passer également si ils sont corrects.

> 💡 Question 2 :  Que fait GitLab pendant les étapes de « setup » et « checkout » ? Veuillez inclure la sortie du terminal Gitlab CI dans votre réponse.

### 4. Automatiser déploiement continu (CD)
Après l’exécution des tests, déployez l’application dans le conteneur via SSH :

```bash
ssh username@192.168.0.1
git clone https://github.com/guteacher/log430-a25-labo0
cd log430-a25-labo0
```

Rédigez ensuite un script pour automatiser le déploiement continu (CD) dans la machine virtuelle.

> 💡 Question 3 : Quelles commandes avez-vous exécutées pour automatiser le déploiement continu de l'application dans la machine virtuelle ? Veuillez inclure la sortie du terminal dans votre réponse.

Quelques commandes utiles pour vérifier l’état des ressources :
```bash
free -h   # Vérifier l’utilisation de la RAM
top       # Vérifier l’utilisation du CPU et les processus en cours
df -h     # Vérifier l’espace disque disponible
```

> 💡 Question 4 : Quel type d'informations pouvez-vous obtenir via la commande « top » ? Veuillez inclure la sortie du terminal dans votre réponse.
---

## 📦 Livrables

- Code compressé en `.zip` contenant **l'ensemble du code source** du projet Labo 00.
- Rapport `.pdf` répondant aux 4 questions presentées dans ce fichier. Il est **obligatoire** d'ajouter du code ou des sorties de terminal pour illustrer chacune de vos réponses.