## 端口映射
```bash
iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
```

操作表名nat，添加规则名PREROUTING,协议名tcp，转发端口80，动作REDIRECT,到目标端口8080


此时，访问http://ip 和http://ip:8080是一样的。
