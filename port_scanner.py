import socket
import threading
import argparse
from datetime import datetime

print("""
=======================================
  Advanced Port Scanner - A S Sumith
=======================================
""")

# Lock for thread-safe print and write
print_lock = threading.Lock()

# Open file to log results
log_file = None

def banner_grab(target, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        s.send(b'WhoAreYou\r\n')
        banner = s.recv(1024).decode().strip()
        s.close()
        return banner if banner else "No banner"
    except:
        return "Banner grab failed"

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    result = s.connect_ex((target, port))
    if result == 0:
        banner = banner_grab(target, port)
        output = f"[OPEN] Port {port}: {banner}"
        with print_lock:
            print(output)
            if log_file:
                log_file.write(output + "\n")
    s.close()

def main(target, start_port, end_port, output_file):
    global log_file

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    header = f"Scan Results for {target} | {timestamp}\n"
    header += "=" * 50 + "\n"

    if output_file:
        log_file = open(output_file, 'w')
        log_file.write(header)

    print(header)
    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\nScan complete.\n")
    if log_file:
        log_file.close()
        print(f"Results saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Port Scanner by A S Sumith")
    parser.add_argument("target", help="Target host to scan (e.g., 127.0.0.1)")
    parser.add_argument("start_port", type=int, help="Start port number")
    parser.add_argument("end_port", type=int, help="End port number")
    parser.add_argument("--output", help="Output file to save results (e.g., results.txt)")
    args = parser.parse_args()

    main(args.target, args.start_port, args.end_port, args.output)
