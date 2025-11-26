"""
given a filewall log with formate

<timestamp> ALLOW/DENY <src_ip> <dst_ip> <bytes>

return the total_allowed_bytes, number_of_denied_connections, top_source_ip_by_allowed_bytes
"""


from collections import defaultdict

# returns the total allowed byts, the # of denied connection and the top source ip by allowed bytes
def analyze_firewall(logs):

    total_allowed_bytes = 0
    denied_count = 0
    allowed_bytes_per_src = defaultdict(int)

    #iterate through the list of logs
    #split each log into its seciton.
    #timestamp  ALLOW/DENY  src_ip  dst_ip  bytes
    for line in logs:
        ports = line.split()
        status = ports[1]
        src_ip = ports[2]
        bytes_val = int(ports[4])

        #if allow update total allowed bytes update allowed bytes dict
        #else increment deny counter
        if status == "ALLOW":
            total_allowed_bytes += bytes_val
            allowed_bytes_per_src[src_ip] += bytes_val
        elif status == "DENY":
            denied_count += 1

    #find top src ip. if not found set it to none
    if allowed_bytes_per_src:
        top_src_ip = max(allowed_bytes_per_src, key=allowed_bytes_per_src.get)
    else:
        top_src_ip = None
    
    return total_allowed_bytes, denied_count, top_src_ip


#firewall log
logs = [
    "2025-01-01T10:00:00 ALLOW 10.0.0.1 10.0.0.2 400",
    "2025-01-01T10:00:01 DENY 10.0.0.3 10.0.0.2 0",
    "2025-01-01T10:00:02 ALLOW 10.0.0.1 10.0.0.3 200",
    "2025-01-01T10:00:00 ALLOW 10.0.0.2 10.0.0.2 400",
    "2025-01-01T10:00:01 DENY 10.0.0.3 10.0.0.2 0",
    "2025-01-01T10:00:02 ALLOW 10.0.0.2 10.0.0.3 200",
    "2025-01-01T10:00:00 ALLOW 10.0.0.2 10.0.0.2 400",
    "2025-01-01T10:00:01 DENY 10.0.0.3 10.0.0.2 0",
    "2025-01-01T10:00:02 ALLOW 10.0.0.1 10.0.0.3 200",
]


print(analyze_firewall(logs))
