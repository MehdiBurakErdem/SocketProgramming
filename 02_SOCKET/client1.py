#!/usr/bin/env python3
# client1.py -- Simple Parity (even) sender
import argparse
import socket

def parity_bits_per_byte(data: bytes) -> str:
    """Return a string of '0'/'1' parity bits (even parity) for each byte."""
    bits = []
    for b in data:
        ones = bin(b).count("1")
        bit = '0' if ones % 2 == 0 else '1'  # even parity: total ones must be even
        bits.append(bit)
    return "".join(bits)

def build_packet(data: str) -> str:
    b = data.encode('utf-8')
    control = parity_bits_per_byte(b)
    packet = f"{data}|PARITY|{control}"
    return packet

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--server-host", default="127.0.0.1")
    parser.add_argument("--server-port", type=int, default=5000)
    args = parser.parse_args()

    data = input("Göndermek istediğin mesajı yaz (| kullanma): ")
    packet = build_packet(data)
    print("[Client1] Gönderilen paket:", packet)
    with socket.create_connection((args.server_host, args.server_port)) as s:
        s.sendall(packet.encode('utf-8'))
    print("[Client1] Paket gönderildi.")

if __name__ == "__main__":
    main()
