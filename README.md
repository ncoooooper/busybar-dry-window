# Dry Window

Find a continuous dry slot long enough for your run, walk or outdoor errand.

A dry hour on a weather chart may have only ten usable minutes left. This app looks for an unbroken interval long enough for the whole errand, including the part that falls in the next forecast hour.

On the window page each block is one forecast hour, starting with the current hour. Blue means the hour fails the rain limits, teal means it qualifies, and taller pale-green blocks mark the chosen outing. Gray means missing data. The rain-limit page places the configured threshold on a 0–100% scale.

## Screen transitions

Move from the length of the dry window to its start time.

![Dry Window front display. Move from the length of the dry window to its start time.](media/guide/screen-transitions.gif)

<details>

<summary>Watch the rear display</summary>

![Dry Window rear display during the recorded controls](media/guide/screen-transitions-rear.gif)

</details>

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

The test forecast included a rainy hour between two dry periods. A 45-minute outing had to fit entirely within a qualifying period. Zero forecast precipitation and the configured probability ceiling apply throughout. The recording used five hours of test data in the Open-Meteo response format.

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

The GIFs are excerpts from the emulator recording. Each LED occupies a 16 × 16 cell with a black border. The end frames pause for reading.

[Full recording](media/controls.mp4) · [Rear display](screenshots/back-1.png) · [Firmware test](EMULATOR-QA.md) · [MIT license](LICENSE)
