from walletthon import Wallet
from telethon.sync import TelegramClient

def test():
    client = TelegramClient('session', api_id = 611335, api_hash = 'd524b414d21f4d37f08684c1df41ac9c')
    client.start()

    wallet = Wallet(client)

    wallet.get_user_balance('USDT')