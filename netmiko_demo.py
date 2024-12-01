from netmiko import (
        ConnectHandler,
)

cisco_router = {
  'device_type': 'cisco_ios',
  'host': 'sandbox-iosxr-1.cisco.com',
  'username': 'admin',
  'password': 'C1sco12345',
  'secret': 'enablepass',
  'port': 22,
}

conn = ConnectHandler(**cisco_router)
result = conn.send_command('sh ip int br')

print(result)

# ssh -l admin sandbox-iosxe-latest-1.cisco.com