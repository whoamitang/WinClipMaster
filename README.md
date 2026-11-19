# WinClipMaster

A lightweight Windows utility that saves copied text to a local SQLite database.

## Download and run

Download the latest .exe from the Releases tab. Run it and keep its console window open; press Ctrl+C or close the window to stop recording. Clipboard text is stored in `%LOCALAPPDATA%\WinClipMaster\history.db`. The database contains plain text, including any sensitive text copied while the utility is running.

## Run from source

On Windows, install Python and run `pip install -r requirements.txt`, then `python main.py`. The program checks the clipboard every half second and saves changes to non-empty text; it does not record images or files. Open the database with an SQLite viewer to browse or delete history.

Licensed under the [MIT License](LICENSE).
