ips = ['11.16.211.2','133.1.1.111','201.22.3.41','17.55.23.123','144.211.32.45']

for ip in ips:
  ip_nodes = ip.split(".")
  print(ip)
  if int(ip_nodes[0]) < 128:
    host = ".".join(ip_nodes[1:])
    print(f"Class A Host: {host}")
  elif int(ip_nodes[0]) < 192:
    host = ".".join(ip_nodes[2:])
    print(f"Class B Host: {host}")
  elif int(ip_nodes[0]) < 233:
    host = ip_nodes[3]
    print(f"Class C Host: {host}")
  else:
    print("Invalid class")
