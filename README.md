# 🎵 Billboard Hot 100 → Spotify Playlist Automation

An end-to-end Python automation project that scrapes **Billboard Hot 100 songs** for a given date and creates a **private Spotify playlist** with those tracks using the Spotify Web API.

This project demonstrates real-world skills such as **web scraping, API integration, OAuth authentication, data handling, and error resilience**.

---

## 🚀 Project Overview

The application:

1. Scrapes the Billboard Hot 100 chart from the official Billboard website.
2. Extracts the top 100 song titles.
3. Searches for each song on Spotify using the Spotify Web API.
4. Creates a **private Spotify playlist** for the selected date.
5. Adds all available songs to the playlist.

If a song is not found on Spotify, it is skipped gracefully without crashing the program.

---

## 🛠️ Tech Stack

* **Python 3**
* **Requests** – HTTP requests
* **BeautifulSoup4** – Web scraping
* **Spotipy** – Spotify Web API wrapper
* **Spotify OAuth 2.0** – Authentication
* **JSON** – Data storage

---

## 📂 Project Structure

```
Billboard-Spotify-Playlist/
│
├── main.py                  # Main application logic
├── song_list.json           # Scraped Billboard songs
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation
```

---

## 🔐 Spotify Setup (Required)

To run this project, you must create a Spotify Developer application.

### Steps:

1. Go to [https://developer.spotify.com/dashboard](https://developer.spotify.com/dashboard)
2. Create a new app
3. Copy your:

   * Client ID
   * Client Secret
4. Add the redirect URI:

   ```
   http://example.com
   ```
5. Save changes

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/billboard-spotify-playlist.git
cd billboard-spotify-playlist
```

### 2️⃣ Create a virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

```bash
python main.py
```

You will be prompted to enter a date in the format:

```
YYYY-MM-DD
```

Example:

```
2005-08-12
```

The program will:

* Scrape Billboard Hot 100
* Authenticate Spotify
* Create a playlist
* Add available songs

---

## ⚠️ Error Handling

* Songs missing on Spotify are skipped automatically
* OAuth tokens are cached locally
* Unicode characters are handled using UTF-8 encoding

---

## 📈 Key Learnings

* Web scraping with headers to avoid bot blocking
* Parsing complex HTML using CSS selectors
* Working with REST APIs
* OAuth authentication flow
* Defensive programming with `try-except`
* Handling real-world data inconsistencies

---

## 💼 Resume Description

> Built an automated Python application that scrapes Billboard Hot 100 charts and creates Spotify playlists using OAuth-authenticated API access. Implemented web scraping, API integration, JSON data handling, and robust error handling to manage missing or unavailable tracks.

---

## 🌱 Future Enhancements

* Support for international charts (India version)
* Public playlist option
* Flask-based web interface
* Database storage instead of JSON
* Email or WhatsApp notifications

---

## 📜 Disclaimer

This project is for **educational purposes only**. Billboard and Spotify data usage must comply with their respective terms of service.

---

## ⭐ Acknowledgements

* Billboard Hot 100
* Spotify Web API
* Spotipy Python Library

---

If you found this project helpful, feel free to ⭐ the repository!
