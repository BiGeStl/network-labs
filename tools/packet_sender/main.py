from scapy.all import IP, TCP, send, Raw

payload = "Dear Steel Cat! This is no attack, it's my humster Pinkie you should track"

ip = IP(dst="127.0.0.1")
tcp = TCP(sport=1234, dport=12345, flags="PA", seq=1000)

packet = ip / tcp / Raw(load=payload)

send(packet, verbose=False)
