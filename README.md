# Linux Command Center

A lightweight, real-time system monitoring dashboard built with Python on Linux.

Linux Command Center displays CPU utilization, RAM usage, disk usage, swap usage, and current network throughput in a live terminal interface.

## Features

- **CPU monitoring** — real-time CPU utilization.
- **Memory monitoring** — RAM usage percentage.
- **Disk monitoring** — used and total disk space.
- **Swap monitoring** — swap space utilization.
- **Network monitoring** — current download and upload speeds in MiB/s.
- **Colored progress bars** — green below 60%, yellow from 60% to below 80%, and red at 80% or above.
- **Live terminal interface** — updates automatically using Rich.

## Requirements

- Linux
- Python 3
- `psutil`
- `rich`

## Installation

Clone the repository:

```bash
git clone https://github.com/AnastasisDrougas/linux-command-center.git
cd linux-command-center
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

## Usage

Run the dashboard:

```bash
python main.py
```

Press `Ctrl+C` to stop the program.

## Current Limitations

- Network speeds are measured across the network interfaces reported by `psutil`, rather than a single selected interface.
- Disk monitoring reports usage for the filesystem mounted at `/`.
- Network speeds represent current throughput, not maximum available internet speed.

## TODO

- [ ] More metrics: network, disk I/O, temperatures, battery
- [ ] Process insights: show what's using the most resources
- [ ] Multiple views: switch between table and progress bars
- [ ] Configuration: adjustable refresh rate and color thresholds
- [ ] Smoother rendering: reduce flicker on updates
- [ ] Project polish: screenshot, cleaner structure
- [ ] Testing: cover the core logic

## Technologies

- Python
- psutil
- Rich

