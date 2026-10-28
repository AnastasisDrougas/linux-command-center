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
git clone YOUR_REPOSITORY_URL
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

### Monitoring
- [ ] Display the active network interface.
- [ ] Allow monitoring a specific network interface.
- [ ] Display peak download and upload speeds.
- [ ] Add CPU temperature monitoring where supported.
- [ ] Display RAM and swap usage in GiB as well as percentages.
- [ ] Add system uptime.

### Interface
- [ ] Improve the dashboard layout and visual hierarchy.
- [ ] Add configurable refresh intervals.
- [ ] Add warnings when CPU, RAM, or disk usage exceeds configurable thresholds.

### Code Quality
- [ ] Add type hints to functions.
- [ ] Add error handling for unavailable system metrics.
- [ ] Add tests for usage-color selection and network-speed calculations.
- [ ] Separate monitoring logic from terminal presentation.

## Technologies

- Python
- psutil
- Rich

