# import nemiko
from netmiko import ConnectHandler

# 接続先ルータ情報
router_1 = {
    "device_type": "cisco_ios",
    "host": "50.50.50.1",  # なんかのIP
    "username": "Router1",  # ルータのHOST名
    "password": "M47ptlmi",
    "port": "22",  # わからない。デフォルトは[22]？
    "secret": "secret",  # わからない。デフォルトは無し？
}

net_connect = ConnectHandler(**router_1)

print(net_connect.send_command("ena"))
print(net_connect.send_command("show interface"))


net_connect.disconnect()
