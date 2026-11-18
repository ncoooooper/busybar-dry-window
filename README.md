# Dry Window

Find a continuous dry slot long enough for your run, walk or outdoor errand.

A dry hour on a weather chart may have only ten usable minutes left. This app looks for an unbroken interval long enough for the whole errand, including the part that falls in the next forecast hour.

## Find a slot for the whole trip

1. Enter your location, time zone, required minutes and rain-probability limit in the companion.
2. Read **DRY WINDOW** for the start time. Turn the bar to read the start and end together on the rear. **Now** means the current moment works.
3. Use the wheel to check **RAIN LIMIT**. The sample uses 25% and a 45-minute outing.

![The next window at 01:00 gives way to the 25% rain limit.](media/guide/inspect-rain-limit.gif)

## Use the start time on the front

1. Turn the wheel back to **DRY WINDOW** and press **Start** to pin it if desired.
2. Check the rear for the local end time before leaving. A missing forecast hour interrupts a candidate slot, just like an hour that exceeds the rain limit.
3. If the page says **No slot**, the current forecast does not contain a continuous interval matching the settings.

![The 25% limit returns to a forecast start time of 01:00.](media/guide/return-to-dry-slot.gif)

## Example from the emulator

The test forecast included a rainy hour between two dry periods. A 45-minute outing had to fit entirely within a qualifying period. Zero forecast precipitation and the configured probability ceiling apply throughout. Deterministic five-hour Open-Meteo-shaped forecast. No live forecast is implied.

## Set up the source

Set latitude, longitude, your IANA time zone, required minutes and maximum hourly precipitation probability. A valid window has zero forecast precipitation and satisfies the probability limit for its entire duration. Data: Open-Meteo weather API under CC BY 4.0, https://open-meteo.com/. Use an appropriate plan for your use. Missing forecast hours break continuity.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run in the emulator

Open BUSY Bar Emulator. From this repository, run:

```sh
~/.busy-emulator/bin/busy-emulator dev --once
```

Press **Back** to exit.

The GIFs are excerpts from the emulator recording. Each front-display pixel is shown at 9× its original width and height. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
