port = 80
service = "http"

port = [21,22,80,443]

server = {
    "ip": "192.168.1.10",
    "status": "active"
}

blocked_ips = {"10.0.0.1", "10.0.0.2"}

print("Port:", port)
print("Service:", service)
print("Ports List:", port)
print("Server dictionary:", server)
print("Blocked IPs:", blocked_ips)