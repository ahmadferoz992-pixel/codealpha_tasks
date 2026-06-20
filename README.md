Network Sniffer — CodeAlpha Cybersecurity Internship Task 1
Overview
This is a basic network packet sniffer built with Python as part of the CodeAlpha Cybersecurity Internship. The tool captures live network traffic and displays useful information about each packet in real time. It helps understand how data travels through a network and how different protocols work at a low level.
Features

Captures live packets from the network interface
Displays source and destination IP addresses for each packet
Identifies the protocol being used such as TCP, UDP, or ICMP
Shows source and destination port numbers
Displays TCP flags for connection tracking
Prints a readable preview of the packet payload when available

Technologies Used

Python 3
Scapy library for packet capturing and analysis

Installation
Before running the script, install the required library by running this command:
pip install scapy
How to Run
Run the following command with root privileges since packet capturing requires system-level access:
sudo python3 network_sniffer.py
On Windows, open your terminal as Administrator and run:
python network_sniffer.py
Project Structure
The repository contains one file which is network_sniffer.py and it handles all the capturing and displaying logic.
Use Case
This tool is useful for learning how network protocols work, understanding packet structure, and getting started with network-level security analysis.
Disclaimer
This tool is built for educational purposes only as part of an internship assignment. Always use network sniffing tools on networks you own or have explicit permission to monitor.
Internship
Built as part of the CodeAlpha Cybersecurity Internship Program.

Company Website: www.codealpha.tech
