# Port-Scanner
A lightweight, multi-threaded port scanner written in Python. This tool identifies open TCP ports on a target host by leveraging the socket library and concurrent threading for efficient execution.

# Features
Multi-threaded: Uses Python's threading module to scan ports concurrently, drastically reducing wait times compared to serial scanning.

Service Mapping: Automatically identifies common services (e.g., HTTP, SSH, FTP) associated with discovered ports.

Thread-Safe: Implements threading.Lock() to ensure data integrity when updating the results list.

Configurable: Easily extendable to include more ports or custom service definitions.

# Usage
Ensure you have Python installed.

Clone this repository.

Run the script:
python scanner.py
Enter the IP address or hostname when prompted.

# How It Works
The script iterates through a specified range of ports (1-1000) and attempts a TCP connect scan for each. By spawning a new thread for every port, it performs the handshake process in parallel. If connect_ex returns 0, the port is flagged as open.

⚠️ Disclaimer
This tool is for educational purposes and authorized security testing only. Scanning networks or hosts you do not own or have explicit permission to test is illegal and unethical. Use responsibly.
