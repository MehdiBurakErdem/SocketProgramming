#!/usr/bin/env python3
# server.py -- intermediate + corruptor (substitution OR deletion)
import argparse
import socket
import threading
import random
import string

def inject_character_substitution(data: str) -> str:
    if not data:
        return data
    i = random.randrange(len(data))
    pool = string.ascii_letters + string.digits  # basit, görünür karakterler
    new_char = random.choice(pool)
    return data[:i] + new_char + data[i+1:]

def inject_character_deletion(data: str) -> str:
    if not data:
        return data
    i = random.randrange(len(data))
    return data[:i] + data[i+1:]

def maybe_inject_error(data: str, inj_prob: float) -> (str, bool, str):
    """
    inj_prob: 0..100 percentage to apply an error.
    Returns (possibly_modified_data, did_inject_bool, method_name)
    method_name is 'substitution' or 'deletion' or 'none'
    """
    if random.random() > inj_prob / 100.0:
        return data, False, "none"
    # choose between substitution and deletion equally
    if random.random() < 0.5:
        return inject_character_substitution(data), True, "substitution"
    else:
        return inject_character_deletion(data), True, "deletion"

def handle_client(conn, forward_host, forward_port, inj_prob):
    try:
        raw = conn.recv(65535)
        if not raw:
            return
        packet = raw.decode('utf-8', errors='replace')
        print("[Server] Gelen paket:", packet)
        parts = packet.split("|", 2)
        if len(parts) != 3:
            print("[Server] Geçersiz paket formatı; olduğu gibi iletiliyor.")
            corrupted_packet = packet
        else:
            data_field, method, control = parts
            corrupted_data, injected, method_name = maybe_inject_error(data_field, inj_prob)
            if injected:
                print(f"[Server] Hata enjekte edildi: {method_name}. DATA -> {corrupted_data}")
            else:
                print("[Server] Hata enjekte edilmedi (probability check).")
            corrupted_packet = f"{corrupted_data}|{method}|{control}"
        # forward to client2
        with socket.create_connection((forward_host, forward_port)) as s2:
            s2.sendall(corrupted_packet.encode('utf-8'))
            print(f"[Server] İletildi -> {forward_host}:{forward_port}")
    except Exception as e:
        print("[Server] Hata:", e)
    finally:
        conn.close()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--listen-host", default="0.0.0.0")
    parser.add_argument("--listen-port", type=int, default=5000)
    parser.add_argument("--forward-host", default="127.0.0.1")
    parser.add_argument("--forward-port", type=int, default=6000)
    parser.add_argument("--inj-prob", type=float, default=100.0,
                        help="Hata enjeksiyon olasılığı yüzde (0-100).")
    parser.add_argument("--seed", type=int, default=None, help="Opsiyonel random seed")
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((args.listen_host, args.listen_port))
    s.listen(5)
    print(f"[Server] Dinleniyor {args.listen_host}:{args.listen_port} -> yönlendiriyor {args.forward_host}:{args.forward_port}")
    try:
        while True:
            conn, addr = s.accept()
            print("[Server] Bağlantı geldi:", addr)
            t = threading.Thread(target=handle_client, args=(conn, args.forward_host, args.forward_port, args.inj_prob))
            t.daemon = True
            t.start()
    except KeyboardInterrupt:
        print("\n[Server] Kapanıyor (Ctrl+C alındı).")
    finally:
        s.close()

if __name__ == "__main__":
    main()
