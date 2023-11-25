<center><b>WalletThon</b></center>
<center>Unofficial library for managing your <a href="https://t.me/wallet">@wallet</a> account</center>

```
pip install walletthon
```

```
from walletthon import Wallet
from telethon.sync import TelegramClient

client = TelegramClient('session', api_id = 611335, api_hash = 'd524b414d21f4d37f08684c1df41ac9c')
client.start()

wallet = Wallet(client)

print(wallet.get_user_balance('USDT'))
```

<p>Contact</p>
<li><a href="https://salism3.dev">https://salism3.dev</a></li><br>

<p>Credits</p>
<li><a href="https://github.com/LonamiWebs/Telethon">Telethon</a></li>
<li><a href="https://github.com/no-name-user-name/pyTelegramWalletApi">pyTelegramWalletApi</a></li>