# Dry Window

Find a continuous dry slot long enough for your run, walk or outdoor errand.

Set latitude, longitude, your IANA time zone, required minutes and maximum hourly precipitation probability. A valid window has zero forecast precipitation and satisfies the probability limit for its entire duration. Data: Open-Meteo weather API under CC BY 4.0, https://open-meteo.com/. Use an appropriate plan for your use. Missing forecast hours break continuity.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
