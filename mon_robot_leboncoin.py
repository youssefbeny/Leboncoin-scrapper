import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from urllib.parse import quote
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Demande les infos une par une au lancement
print("Configuration du robot Leboncoin...")
EMAIL_RECEIVER = input("Quel est ton email pour recevoir les messages ? ")
QUERY = input("Quel est le titre ou les mots-clés de l'annonce ? (ex. 'voiture occasion') ")
MAX_PRICE = int(input("Quel est le prix maximum ? (ex. 5000) "))
CATEGORY_SLUG = input("Quelle est la catégorie ? (ex. 'voitures') ")
EMAIL_SENDER = input("Quel est ton email d'envoi ? (ex. tonemail@gmail.com) ")
EMAIL_PASSWORD = input("Quel est ton mot de passe d'application Gmail ? ")
MAX_PAGES = 5  # Fixe, mais tu peux le changer si besoin
INTERVAL = 600  # 10 minutes, fixe aussi

def parse_search(html_content: str) -> list:
    """Parse les annonces depuis le JSON dans le HTML"""
    soup = BeautifulSoup(html_content, 'html.parser')
    script = soup.find("script", id="__NEXT_DATA__")
    if not script:
        print("Script JSON non trouvé - Le site a changé ?")
        return []
    try:
        json_data = json.loads(script.text)
        ads_data = json_data["props"]["pageProps"].get("searchData", {}).get("ads", [])
        listings = []
        for ad in ads_data:
            title = ad.get("subject", "N/A")
            price = ad.get("price", ["N/A"])[0]
            list_id = ad.get("list_id", "N/A")
            link = f"https://www.leboncoin.fr/ad/{CATEGORY_SLUG}/{list_id}"
            listings.append({"Titre": title, "Prix": price, "Lien": link})
        return listings
    except Exception as e:
        print(f"Erreur JSON : {e}")
        return []

def scrape_search(max_pages: int) -> list:
    """Scrape la recherche Leboncoin avec pagination"""
    base_url = f"https://www.leboncoin.fr/recherche?category={CATEGORY_SLUG}&text={quote(QUERY)}&price=0-{MAX_PRICE}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
        "Referer": "https://www.leboncoin.fr/",
        "Connection": "keep-alive"
    }
    search_data = []
    
    for page in range(1, max_pages + 1):
        url = f"{base_url}&page={page}" if page > 1 else base_url
        print(f"Scraping page {page} : {url}")
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            search_data.extend(parse_search(response.text))
        else:
            print(f"Erreur {response.status_code} pour {url}")
            break
        time.sleep(2)  # Pause pour éviter les blocs
    
    return search_data

def send_email_alert(new_listings):
    """Envoie un email avec les nouvelles annonces"""
    if not new_listings:
        return
    msg = MIMEMultipart()
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER
    msg['Subject'] = "Nouvelles annonces Leboncoin !"
    
    body = "Nouvelles annonces trouvées :\n\n"
    for listing in new_listings:
        body += f"- {listing['Titre']} | {listing['Prix']} € | {listing['Lien']}\n"
    msg.attach(MIMEText(body, 'plain'))
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_SENDER, EMAIL_PASSWORD)
    server.send_message(msg)
    server.quit()
    print("Email d'alerte envoyé !")

# Charge les annonces vues
seen_links = set()
try:
    with open("seen_links.txt", "r") as f:
        seen_links = {line.strip() for line in f}
except FileNotFoundError:
    pass

# Boucle de monitoring avec gestion d'erreur
try:
    while True:
        print("Scan en cours...")
        listings = scrape_search(MAX_PAGES)
        
        if listings:
            df = pd.DataFrame(listings)
            df.to_excel("annonces_leboncoin.xlsx", index=False)
            print("Tableau mis à jour : annonces_leboncoin.xlsx")
            
            new_listings = [l for l in listings if l["Lien"] not in seen_links]
            if new_listings:
                print("\nNouvelles annonces trouvées !")
                for l in new_listings:
                    print(f"- {l['Titre']} | {l['Prix']} € | {l['Lien']}")
                    seen_links.add(l["Lien"])
                send_email_alert(new_listings)
            
            with open("seen_links.txt", "w") as f:
                for link in seen_links:
                    f.write(link + "\n")
        else:
            print("Aucune annonce trouvée - Vérifie tes critères ou le site.")
        
        time.sleep(INTERVAL)
except Exception as e:
    print(f"Erreur fatale : {e}")
    input("Appuie sur Entrée pour quitter...")  # Garde la fenêtre ouverte
