# 端口映射
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
