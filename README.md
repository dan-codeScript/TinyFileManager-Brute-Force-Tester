# TinyFileManager-Brute-Force-Tester

TinyFileManager Brute Force Tester
Outil de test de résistance pour TinyFileManager

Ce script permet de tester la robustesse des configurations TinyFileManager contre les attaques par force brute. Il intègre des mécanismes de sécurité éthique et respectueux des systèmes testés.

Features clés :
- 🛡️ Gestion automatique des tokens CSRF
- 📁 Chargement dynamique des wordlists
- ⏱️ Contrôle du débit des requêtes
- 🔍 Détection des réponses ambiguës
- 🌍 User-Agent et headers localisés
- ⚠️ Alertes de sécurité explicites

Usage :
```bash
python3 tinyfm_tester.py http://votresite.com/fm.php -u users.txt -p passwords.txt -d 0.3
```

Paramètres :
- `url` : URL de la page de login
- `-u/--users` : Fichier des identifiants
- `-p/--passwords` : Fichier des mots de passe
- `-d/--delay` : Délai entre les requêtes (défaut: 0.5s)

Exigences :
- Python 3.6+
- Bibliothèques : `requests`

Avertissement légal
⚠️ Cet outil est fourni à des fins éducatives et de test autorisés uniquement. L'utilisation non autorisée sur des systèmes dont vous n'êtes pas propriétaire est strictement interdite par la loi. Le développeur décline toute responsabilité pour une utilisation abusive.

Best Practices :
- Toujours obtenir une autorisation écrite
- Tester uniquement vos propres systèmes
- Limiter le débit à <1 req/seconde
- Utiliser des wordlists appropriées
- Arrêter immédiatement en cas de succès
