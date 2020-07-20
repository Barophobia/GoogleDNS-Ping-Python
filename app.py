import subprocess

hostname = '8.8.8.8'

ping = subprocess.call(['ping','-c','1',hostname])

if ping == 0:
    print ('googleDNS is up')
else:
        print('googleDNS is down')