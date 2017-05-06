import subprocess
import xml.etree.ElementTree as ET


shellOutput = ''

try:
    shellOutput = subprocess.check_output("""omp -h 127.0.0.1 -u nejc -w 112358 -p 9390 --xml='<get_configs/>'""", shell=True)
except subprocess.CalledProcessError:
    print('Something went wrong!')
    exit()
except OSError:
    print('Executable not found')
    exit()


result = shellOutput.decode("utf-8")
tree = ET.fromstring(shellOutput)

for child in tree:
    print(child.tag, child.attrib)