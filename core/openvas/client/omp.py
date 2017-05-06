import subprocess
import xml.etree.ElementTree as ElementTree

class Omp:
    """Wrapper around bash omp client."""

    config = {}

    def __init__(self, config):
        self.config['host'] = config['host']
        self.config['port'] = config['port']
        self.config['username'] = config['username']
        self.config['password'] = config['password']


    def help(self):
        response = self.execute_xml_command('<help/>')

        print(response)

    def get_configs(self):
        response = self.execute_xml_command('<get_configs/>')
        print(response)

    def get_targets(self):
        response = self.execute_xml_command('<get_targets/>')
        print(response)


    def get_command_string(self, xml_command):
        return "omp -h %s -p %s -u %s -w %s -i --xml='%s'" \
               % (self.config['host'], self.config['port'],
                  self.config['username'], self.config['password'], xml_command)

    def execute_xml_command(self, xml_command):
        try:
            shell_output = subprocess.check_output(self.get_command_string(xml_command), shell=True)
            raw_xml = shell_output.decode("utf-8")
            print(raw_xml)

            return ElementTree.fromstring(raw_xml)
        except subprocess.CalledProcessError:
            print('Something went wrong!')
            exit()
        except OSError:
            print('Executable not found')
            exit()






