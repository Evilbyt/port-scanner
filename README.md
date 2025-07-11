# Advanced Port Scanner

A Python tool that scans a target host for open TCP ports, grabs banners from open ports, and saves results to a file. Uses multi-threading for faster scans.

## ✨ Features

- Multi-threaded scanning for speed.
- Banner grabbing: tries to identify services.
- Saves results with timestamp to a file.
- Uses only built-in Python libraries.

## ⚙️ Usage

```bash
git clone https://github.com/Evilbyt/port-scanner.git
cd port-scanner

# Run scanner:
python port_scanner.py <target> <start_port> <end_port> [--output results.txt]

EXAMPLE:
        python port_scanner.py 127.0.0.1 20 100 --output results.txt

✅ Note: Always scan only hosts you own or have permission for!

