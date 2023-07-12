import hashlib

polluted_pw = '1111'
polluted_pw_hash = hashlib.sha256(polluted_pw.encode()).hexdigest()

print(polluted_pw_hash)