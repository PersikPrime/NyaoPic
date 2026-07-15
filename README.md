<div align="center">
  <img src="https://www.dropbox.com/scl/fi/6aioog1mu17276k0zygsl/NyaoPic.png?rlkey=zas4y76g7z5dnry3oxdwebara&st=0do5jy7f&dl=1" alt="NyaoPic Logo" width="180" style="border-radius: 50%;">

  # NyaoLabs-Pic

  `A lightweight, modular, and fast Discord bot designed to bring cute anime illustrations right into your server!`
</div>

---

### 🐾 Features
* `Slash Commands` — Built using modern, fast Discord Slash Commands (`/neko`).
* `Modular Architecture (Cogs)` — Easy to scale, add new features, and manage commands.
* `Safe & Asynchronous` — Powered by `disnake` and `aiohttp` for non-blocking API requests.
* `Nekos.best Integration` — Fetches random, high-quality images of neko, waifu, kitsune, and more.

---

### 🧩 Main Requirements
* `disnake` - 2.12.0 or above
* `python-dotenv` - 1.2.2 or above
* `aiohttp` - 3.14.1 or above

Other requrements can be found in `requirements.txt`

---
### 🛠️ Installation & Setup
```text
1. Clone the repository:
   $ git clone [https://github.com/PersikPrime/NyaoPic.git](https://github.com/PersikPrime/NyaoPic.git)
   $ cd NyaoPic

2. Create a virtual environment & install dependencies:
   $ python3 -m venv .venv
   $ source .venv/bin/activate
   $ pip install -r requirements.txt

3. Configure Environment Variables in your .env file:
   BOT_TOKEN=your_secret_discord_bot_token_here

4. Run the Bot:
   $ python3 main.py
```

### 🌸 Project Structure
```text
NyaoPic/
├── cogs/                 # Modular command folders (Cogs)
│   ├── general.py        # Base commands
│   └── nekosend.py       # Neko-sending command integration
├── .env                  # Private bot tokens (git-ignored)
├── .env.example          # Environment template for others
├── .gitignore            # Tells git what to ignore
├── main.py               # Main bot entry point & cog loader
└── requirements.txt      # List of dependencies
```
