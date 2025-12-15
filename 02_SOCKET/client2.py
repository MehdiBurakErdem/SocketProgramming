#!/usr/bin/env python3
# client2.py -- Receiver + Parity checker
import argparse
import socket

def parity_bits_per_byte(data: bytes) -> str:
    bits = []
    for b in data:
        ones = bin(b).count("1")
        bit = '0' if ones % 2 == 0 else '1'  # even parity
        bits.append(bit)
    return "".join(bits)

def recompute_control(data: str) -> str:
    b = data.encode('utf-8')
    return parity_bits_per_byte(b)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--listen-host", default="0.0.0.0")
    parser.add_argument("--listen-port", type=int, default=6000)
    args = parser.parse_args()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((args.listen_host, args.listen_port))
    s.listen(1)
    print(f"[Client2] Dinleniyor {args.listen_host}:{args.listen_port}")
    try:
        while True:
            conn, addr = s.accept()
            with conn:
                raw = conn.recv(65535)
                if not raw:
                    continue
                packet = raw.decode('utf-8', errors='replace')
                print("[Client2] Alınan paket:", packet)
                parts = packet.split("|", 2)
                if len(parts) != 3:
                    print("[Client2] Geçersiz paket formatı.")
                    continue
                data_field, method, incoming_control = parts
                computed = recompute_control(data_field)
                print("Received Data :", data_field)
                print("Method :", method)
                print("Sent Check Bits :", incoming_control)
                print("Computed Check Bits :", computed)
                if computed == incoming_control:
                    print("Status : DATA CORRECT")
                else:
                    print("Status : DATA CORRUPTED")
                print("-"*40)
    except KeyboardInterrupt:
        print("\n[Client2] Kapanıyor (Ctrl+C alındı).")
    finally:
        s.close()

if __name__ == "__main__":
    main()
