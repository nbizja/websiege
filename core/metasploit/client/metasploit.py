import subprocess
import csv
import os

class Metasploit:
    """Wrapper around msfconsole command"""

    def cmd(self, command):
        #todo do not forget to switch workspaces
        try:
            shell_output = subprocess.check_output('msfconsole --quiet -x "%s;exit"' % command, shell=True)
            result = shell_output.decode("utf-8")
            print(result)

            return shell_output
        except subprocess.CalledProcessError:
            print('Something went wrong!')
            exit()
        except OSError:
            print('Executable not found')
            exit()

    def db_nmap(self, ip):
        self.cmd('db_nmap -v -sV %s' % ip)

    def nmap(self, ip):
        self.cmd('nmap -v --no-stylesheet -sV %s -oX /media/sf_websiege/core/metasploit/examples/nmap' % ip)

    def services(self):
        self.cmd('services -o /tmp/test.csv')

        with open('/tmp/test.csv') as csvfile:
            services_reader = csv.DictReader(csvfile, delimiter=',')

            services = list(services_reader)

        os.remove('/tmp/test.csv')

        return services

    def search(self, search_string, app_filter='server', type_filter='exploit'):
        app_query = ''
        if app_filter:
            app_query = 'app:%s' % app_filter

        type_query = ''
        if type_filter:
            type_query = 'type:%s' % type_filter

        self.cmd('search %s %s %s' % (app_query, type_query, search_string))

    def help(self):
        self.cmd('help')