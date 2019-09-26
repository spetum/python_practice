

import socket
import uuid

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
hexIP = socket.inet_aton(IPAddr).hex()
macAddr = ':'.join(['{02X}'.format(
					(uuid.getnode()>> elements) & 0xff)
					for elements in range(0,2*6,2)][::-1])
						
print ('Your Computer Name is ' + hostname)
print ('Your Computer IP Address is ' + IPAddr)
print ('Your Hex IP Address: ' + hexIP)
print ('Your Computer MAC Address is ' + macAddr)