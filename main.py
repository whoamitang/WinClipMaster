import os
from contextlib import closing
from pathlib import Path
import sqlite3
import time

import pyperclip


def main():
    data_dir = Path(os.environ.get("LOCALAPPDATA", Path.home())) / "WinClipMaster"
    data_dir.mkdir(parents=True, exist_ok=True)
    with closing(sqlite3.connect(data_dir / "history.db")) as db:
        db.execute("CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY, content TEXT NOT NULL, copied_at TEXT DEFAULT CURRENT_TIMESTAMP)")
        previous = None
        print(f"Saving clipboard text to {data_dir / 'history.db'}. Press Ctrl+C to stop.")
        while True:
            text = pyperclip.paste()
            if text and text != previous:
                db.execute("INSERT INTO history (content) VALUES (?)", (text,))
                db.commit()
            previous = text
            time.sleep(0.5)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nStopped.")
