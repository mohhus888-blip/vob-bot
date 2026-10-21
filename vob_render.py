
import requests, time, os

TELEGRAM_TOKEN = "8069393836:AAFf5rI7L8v7sQ2dJ7lM8n9o0p1q2r3s4t"
CHAT_ID = "7739212650"

if os.getenv("BOT_TOKEN"):
    TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")
if os.getenv("CHAT_ID"):
    CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg}, timeout=15)
        print(f"Telegram: {msg}")
    except Exception as e:
        print(f"Telegram error: {e}")

def get_price(symbol):
    try:
        # جرب Binance الاول، لو فشل جرب Bybit
        try:
            url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}"
            r = requests.get(url, timeout=10).json()
            return float(r['price'])
        except:
            url = f"https://api.bybit.com/v5/market/tickers?category=spot&symbol={symbol}"
            r = requests.get(url, timeout=10).json()
            return float(r['result']['list'][0]['lastPrice'])
    except Exception as e:
        print(f"Price error {symbol}: {e}")
        return None

send_telegram("✅ بوت VOB اشتغل على Render - بيراقب BTC + ETH (1m + 3m) - شغال 24/7")

symbols = ["BTCUSDT", "ETHUSDT"]
timeframes = ["1m", "3m"]

while True:
    for sym in symbols:
        price = get_price(sym)
        for tf in timeframes:
            if price:
                print(f"{sym} {tf} - {price} - OK")
            else:
                print(f"{sym} {tf} - FAILED")
    print("--- نايم 60 ثانية ---")
    time.sleep(60)
