from core.openvas.client.omp import Omp

config = {
    'host': '127.0.0.1',
    'port': '9390',
    'username': 'nejc',
    'password': '112358',
}

omp = Omp(config)

print(omp.get_targets())

#test = subprocess.check_call("""omp -h 127.0.0.1 -u nejc -w 112358 -p 9390 --xml='<help/>'""", shell=True)

#print(test)