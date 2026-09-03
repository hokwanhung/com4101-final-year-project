# Hotel Customer Service Chatbot

A Traditional Chinese hotel guest chatbot built as a **COM4101 Final Year Project** at The Hang Seng University of Hong Kong (BA-AHCC). Guests can book a room, ask for nearby food, attractions, and shopping, and leave feedback — all in chat.

香港恒生大學 BA-AHCC 四年級專題：以繁體中文提供酒店客戶服務的聊天機器人。

---

## What it can do

| Feature | What the guest can ask |
| --- | --- |
| **Room booking** | Reserve a room by price, occupancy, room type, and harbour / mountain view |
| **Nearby food** | Chinese, Japanese, Korean, or Southeast Asian restaurants (from local CSV data + OpenRice links) |
| **Places to visit** | Museums, shopping, and outskirts / nature spots in Hong Kong |
| **Shopping** | Clothing and groceries nearby |
| **Feedback & sentiment** | Leave comments at the end of a chat; overall mood is scored and stored |

The bot greets the guest, remembers their name, and reacts to compliments or complaints during the conversation.

---

## How it works

```
Guest (chat)  →  Rasa NLU (Chinese)  →  Dialogue stories / rules
                                          ↓
                                   Custom actions
                                          ↓
                    MySQL rooms   CSV local tips   Firebase feedback
```

1. **NLU** — Jieba tokenises Chinese text. A custom NLTK sentiment component labels each message as positive, neutral, or negative. DIET classifies intents and extracts entities (name, room type, food category, and so on).
2. **Dialogue** — Stories in `data/stories.yml` teach typical flows (greet → book, ask for food, say goodbye). Rules cover fixed replies such as “who are you?”.
3. **Actions** — Python code in `actions/` looks up rooms in MySQL, picks two recommendations from CSV files, optionally opens Chrome to fetch a search result URL, and writes feedback plus a weighted sentiment score to Firebase.

---

## Tech stack

- **Rasa 2.8** / **Rasa SDK 2.8** — NLU and dialogue
- **Python 3.8**
- **Jieba** — Chinese word segmentation
- **NLTK Naive Bayes** — custom sentiment pipeline component
- **MySQL** — hotel rooms, users, and bookings (`sql/`)
- **Firebase Realtime Database** — conversation feedback and overall sentiment
- **Selenium + ChromeDriver** — optional live search links for recommendations
- **Telegram / REST / Socket.IO** — chat channels (see `credentials.example.yml`)

---

## Repository layout

```
├── actions/                 Custom actions + sentiment component
│   ├── actions.py
│   ├── sentiment.py
│   └── labels.txt           Training labels for sentiment
├── csv/                     Recommendation lists (food, visit, shopping)
├── data/
│   ├── nlu.yml              Training examples (intents & entities)
│   ├── stories.yml          Conversation flows
│   └── rules.yml            Must-follow mappings
├── scripts/                 Commit-message checker used by git hooks
├── sql/                     MySQL schema and sample room data
├── tests/                   Rasa story tests and pytest for the checker
├── config.yml               NLU pipeline and policies
├── domain.yml               Intents, slots, responses, actions
├── credentials.example.yml  Copy to credentials.yml (gitignored)
├── endpoints.example.yml    Copy to endpoints.yml
├── requirements.txt         Runtime packages (Rasa and the action server)
└── requirements-dev.txt     Ruff, pre-commit, and pytest
```

Secrets such as `credentials.yml` and Firebase admin keys are **not** in this repo. Copy the example files and keep real tokens on your machine only.

---

## Prerequisites

- Python **3.8** (Rasa 2.8 does not support newer Python versions)
- MySQL (local instance; default schema name `fyp_project_default`)
- Chrome + a matching `chromedriver.exe` in the project root (only if you want live search URLs)
- A Firebase project with Realtime Database (only if you want feedback storage)

---

## Setup

### 1. Clone and install

```bash
git clone https://github.com/<your-org>/com4101-final-year-project.git
cd com4101-final-year-project

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate

pip install --no-cache-dir -r requirements.txt
pip install --no-cache-dir -r requirements-dev.txt
python -m pre_commit install --hook-type pre-commit --hook-type commit-msg
```

Point `PYTHONPATH` at the `actions` folder so the custom sentiment component can be imported:

```powershell
# Windows PowerShell
$env:PYTHONPATH = "$PWD\actions;$env:PYTHONPATH"
```

```bash
# macOS / Linux
export PYTHONPATH="$(pwd)/actions:$PYTHONPATH"
```

### 2. Local config files

```bash
cp credentials.example.yml credentials.yml
cp endpoints.example.yml endpoints.yml
```

Fill in `credentials.yml` with your Telegram bot token (or leave Telegram blank and use the REST / shell channel). Do not commit this file.

### 3. MySQL

Create the database and tables:

```sql
SOURCE sql/fypprojectdefault.sql;
SOURCE sql/users.sql;
SOURCE sql/hotel_rooms.sql;
SOURCE sql/booking.sql;
```

Room lookup currently uses `mysql+pymysql://root:root@localhost:3306/fyp_project_default`. Change the connection string in `actions/actions.py` if your local MySQL user or password is different.

### 4. Firebase (feedback)

1. Place a gitignored service-account file at `actions/firebase-adminsdk.json`.
2. Set the Realtime Database URL:

```powershell
$env:FIREBASE_DATABASE_URL = "https://<your-project>.firebaseio.com"
# optional if the JSON is not at the default path:
$env:FIREBASE_CREDENTIALS_PATH = "path\to\firebase-adminsdk.json"
```

Without Firebase, greeting and recommendations still work; ending a conversation that saves feedback will fail until this is configured.

### 5. Train and run

Use **three terminals** (all with the venv activated and `PYTHONPATH` set):

```bash
# Terminal 1 — train the model (once, or after data changes)
rasa train

# Terminal 2 — custom action server
rasa run actions

# Terminal 3 — talk to the bot in the shell
rasa shell
```

To expose HTTP / Telegram / Socket.IO instead of the shell:

```bash
rasa run --enable-api --cors "*"
```

The action server must already be running on `http://localhost:5055/webhook` (see `endpoints.example.yml`).

---

## Checks

Format and lint with Ruff (line length 100). Commits fail if either check is dirty:

```powershell
python -m ruff format
python -m ruff check
python -m ruff format --check
```

Install the git hooks once (already shown in setup). After that, `git commit` runs Ruff on staged Python and rejects a commit whose **first line** is not formatted as required. If a commit is blocked, run `python -m ruff format` (and `python -m ruff check --fix` when the fix is safe), then commit again.

The first line of a commit message must be at most 100 characters and match
`feature|bugfix|docs|refactor: ` followed by a lowercase summary, for example
`feature: add hotel room search by occupancy`. A body after a blank line is allowed.

```text
feature: add harbour-view filter to room search
bugfix: skip firebase write when feedback is empty
docs: describe ruff format checks
refactor: extract sentiment weighting helper
```

Invalid: missing prefix, `Feature:`, `feature:Add`, no space after `:`, or a first line longer than 100 characters.

---

## Talking to the bot

The assistant expects **Traditional Chinese**. Example turns:

- `你好` → it asks how to address you
- `我姓陳` → greeting and a short list of services
- `我想預約酒店` → room search from MySQL
- `想吃東西` then `中菜` / `日本菜` / `韓式` / `東南亞` → two restaurant names and links
- `附近有什麼好玩` then museums / shopping / outskirts
- `再見` → optional feedback, then the session ends

---

## Training data and recommendations

| Path | Role |
| --- | --- |
| `data/nlu.yml` | Intent examples and entity annotations |
| `data/stories.yml` | Happy paths for booking, food, visit, shopping, feedback |
| `csv/ask_food_*.csv` | Restaurant names by cuisine |
| `csv/ask_visit_*.csv` | Museums, shopping, outskirts |
| `csv/ask_buy_*.csv` | Clothing and grocery spots |
| `actions/labels.txt` | `pos` / `neu` / `neg` labels for the sentiment classifier |

`gen.py` is a helper used to generate some of those lists; it is not required at runtime.

---

## Tests

Dialogue tests:

```bash
rasa test
```

Story tests live in `tests/test_stories.yml`. Update them if you change greet / goodbye flows in `domain.yml`.

Commit-message checker:

```bash
python -m pytest tests/test_check_commit_msg.py
```

---

## Notes for markers and collaborators

- Language of the **product** is Traditional Chinese; this README is in English so the GitHub page is easy to scan.
- Trained models under `models/` are gitignored — run `rasa train` locally.
- Channel tokens, Firebase keys, and `.env` files are gitignored on purpose.
- Selenium search is best-effort: if ChromeDriver or Google’s page layout fails, the bot still returns the two CSV names and apologises for missing URLs.

---

## Licence and authors

Final Year Project (COM4101), The Hang Seng University of Hong Kong, BA-AHCC Year 4.

This repository is submitted for academic assessment. Ask the project team before reusing the code or data outside that context.
