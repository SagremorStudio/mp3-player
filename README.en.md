# 🎵 Neon MP3 Player

A browser-based, retro-neon MP3 player with folder-based navigation, spectrum visualization, and a Python backend server.

![version](https://img.shields.io/badge/version-0.07--FIXED-00bfff)
![license](https://img.shields.io/badge/license-personal%20use-lightgrey)

## ✨ Features

- **Folder-based browsing** – a collapsible file browser grouped by the subfolders of the `mp3/` directory
- **Playback controls** – play/pause, previous/next track, ±10/20/30 second skip
- **Autoplay** – automatically continues to the next track when one ends (toggleable)
- **Live spectrum analyzer** – Web Audio API–powered VU-meter bars and a pulsing "music note" animation
- **State restoration** – remembers the last played track and which folders were open, even after a page reload (`localStorage`)
- **Memory management** – automatic and manual memory cleanup for long-running (e.g. kiosk-mode) use
- **Live status bar** – real-time memory usage, playback state, and cleanup status
- **Automatic list refresh** – re-fetches the folder structure from the server every 30 seconds

## 📁 Project Structure

```
.
├── index.html          # The player's user interface (this repo's content)
├── server.py           # Python backend server (static file serving + /list endpoint)
└── mp3/                # Folders containing the playable MP3 files
    ├── Album 1/
    │   ├── 01 - track.mp3
    │   └── 02 - track.mp3
    └── Album 2/
        └── ...
```

## ⚙️ How It Works

The frontend is a single static `index.html` file that relies on the server for two things:

1. **`GET /list`** – expected to return a JSON response mapping folder names to the list of files inside them:

   ```json
   {
     "Album 1": ["01 - track.mp3", "02 - track.mp3"],
     "Album 2": ["intro.mp3"],
     "": ["root_track.mp3"]
   }
   ```

2. **Static file serving** from the `mp3/` directory, since tracks are referenced via relative URLs like `mp3/<folder>/<filename>`.

So the backend server's job is simply this: a lightweight HTTP server that serves `index.html`, serves the static `mp3/` directory, and exposes a `/list` endpoint that walks the `mp3/` folder and returns the JSON structure above.

## 🚀 Setup & Running

### Prerequisites

- Python 3.8+
- A modern browser (Chrome, Firefox, Edge – with Web Audio API support)

### Steps

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>
   ```

2. Copy your MP3 files into the `mp3/` directory, organized by folder.

3. Start the server:
   ```bash
   python server.py
   ```

4. Open it in your browser:
   ```
   http://localhost:8000
   ```

> 💡 The exact startup command and port may differ depending on what `server.py` is built with (e.g. `http.server`, Flask) – adjust the steps above to match your actual server implementation if needed.

## 🎛️ Usage

| Control | Function |
|---|---|
| ▶ / ⏸ | Play / pause |
| ⏮ / ⏭ | Previous / next track |
| 🔙 / 🔜 | Skip -30/-20/-10s or +10/+20/+30s |
| 🔊 slider | Volume |
| 🔁 Autoplay | Toggle automatic continuation |
| 🗑️ Memory cleanup | Click: normal cleanup • Double-click: aggressive cleanup (restarts the `AudioContext`) |

Clicking a folder header expands/collapses its contents; the open/closed state is persisted in the browser's `localStorage`.

## 🧠 Memory Management

Since the player is designed for sustained use (e.g. running on a school display), it includes built-in memory management:

- **Automatic cleanup** on track change, and every 3 minutes while playback is paused
- **Manual cleanup** via the 🗑️ button, with a double-click triggering aggressive mode (fully restarting the `AudioContext`)
- **Live memory display** in the footer status bar (via the `performance.memory` API, where supported by the browser)

## 🛠️ Customization

The color palette can be adjusted via the CSS variables in `:root`:

```css
:root {
  --bg: #0a0f16;
  --panel: #1c2a3a;
  --accent: #00bfff;
  --accent2: #63f588;
  --accent3: #c2f563;
  --text: #e3f2ff;
}
```

## 📄 License

Built for personal / internal use.

---

*2025 | Dajka Lajos | Version: 0.07-FIXED*
