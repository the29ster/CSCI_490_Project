import requests

def get_card_data(card_name):
    url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        card_data = response.json()
        return {
            'name': card_data.get('name'),
            'scryfall_id': card_data.get('id'),
            'usd_price': card_data.get('prices').get('usd'),
            'eur_price': card_data.get('prices').get('eur'),
            'tix_price': card_data.get('prices').get('tix'),
        }
    return None
