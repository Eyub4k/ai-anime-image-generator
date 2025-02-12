# AI Anime Image Generator

## Description
Ce projet est une application web permettant de générer des images d'anime à l'aide du modèle **hakurei/waifu-diffusion**. L'application utilise **Flask** en backend pour servir l'API de génération et **HTML, CSS, et JavaScript** en frontend pour offrir une interface utilisateur simple et intuitive.

## Fonctionnalités
- Génération d'images d'anime à partir de prompts textuels.
- Interface utilisateur épurée et responsive.
- Indicateur de progression lors de la génération.
- Possibilité de télécharger l'image générée.

## Technologies utilisées
- **Backend :** Flask, PyTorch, Diffusers
- **Frontend :** HTML, CSS, JavaScript
- **Modèle :** hakurei/waifu-diffusion

## Installation et exécution
### Prérequis
- Python 3.8+
- pip
- Une carte graphique NVIDIA compatible CUDA (recommandé pour de meilleures performances)

### Étapes d'installation
1. **Cloner le dépôt**
```sh
git clone https://github.com/ton-repo/ai-anime-image-generator.git
cd ai-anime-image-generator
```

2. **Créer un environnement virtuel (optionnel mais recommandé)**
```sh
python -m venv venv
source venv/bin/activate  # Sur Linux/macOS
venv\Scripts\activate  # Sur Windows
```

3. **Installer les dépendances**
```sh
pip install -r requirements.txt
```

4. **Lancer l'application**
```sh
python app.py
```
L'application sera accessible sur `http://127.0.0.1:5000/`.

## Utilisation
1. Ouvrir l'application web dans un navigateur.
2. Entrer un prompt décrivant l'image souhaitée (ex: *a chibi girl with blue hair and cat ears*).
3. Cliquer sur **Generate Image** et attendre la fin du processus.
4. Télécharger l'image générée si elle vous convient.

## Déploiement
L'application peut être déployée sur un serveur avec **Gunicorn** et **NGINX** ou via des services comme **Heroku, AWS, ou Hugging Face Spaces**.

## Remarque
Ce projet utilise le modèle `hakurei/waifu-diffusion` pour la génération d'images. Ce modèle est conçu pour produire des images d'anime de haute qualité.

## Auteur
- [Ton GitHub](https://github.com/Eyub4k)

## Contributions
Les contributions sont les bienvenues ! N'hésite pas à ouvrir une issue ou à proposer une pull request.

---

🚀 **Amuse-toi bien en générant des images d'anime !**

