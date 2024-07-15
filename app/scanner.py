from scapy.all import sr1, IP, TCP
from six.moves import range


def scan(ip):
    ports = [443, 80, 22, 587, 3389, 500, 179, 123, 53]  
    results = []
    
    for port in ports:
        pkt = IP(dst=ip)/TCP(dport=port, flags="S")
        resp = sr1(pkt, timeout=1, verbose=0)
        
        if resp:
            if resp.haslayer(TCP) and resp.getlayer(TCP).flags == 0x12:  # SYN-ACK
                results.append((port, 'open'))
            else:
                results.append((port, 'closed'))
        
    
    return results
