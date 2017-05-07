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

    def _get_command_string(self, xml_command):
        return "omp -h %s -p %s -u %s -w %s -i --xml='%s'" \
               % (self.config['host'], self.config['port'],
                  self.config['username'], self.config['password'], xml_command)

    def execute_xml_command(self, xml_command):
        try:
            shell_output = subprocess.check_output(self._get_command_string(xml_command), shell=True)
            raw_xml = shell_output.decode("utf-8")
            print(raw_xml)

            return ElementTree.fromstring(raw_xml)
        except subprocess.CalledProcessError:
            print('Something went wrong!')
            exit()
        except OSError:
            print('Executable not found')
            exit()

    def help(self):
        response = self.execute_xml_command('<help/>')

        print(response)

    def start_task(self, taskId):
        response = self.execute_xml_command('<start_task task_id="%s"/>' % taskId)
        print(response)

    def get_agents(self):
        response = self.execute_xml_command('<get_agents/>')
        print(response)

    def get_aggregates(self, type):
        response = self.execute_xml_command('<get_aggregates type="%s"/>' % type)
        print(response)

    def get_alerts(self):
        response = self.execute_xml_command('<get_alerts/>')
        print(response)

    def get_configs(self):
        response = self.execute_xml_command('<get_configs/>')
        print(response)

    def get_filters(self):
        response = self.execute_xml_command('<get_filters/>')
        print(response)

    def get_groups(self):
        response = self.execute_xml_command('<get_groups/>')
        print(response)

    def get_info(self):
        #todo needs type
        response = self.execute_xml_command('<get_info type=""/>')
        print(response)

    def get_lsc_credentials(self):
        response = self.execute_xml_command('<get_lsc_credentials/>')
        print(response)

    def get_notes(self):
        response = self.execute_xml_command('<get_notes/>')
        print(response)

    def get_nvts(self):
        response = self.execute_xml_command('<get_nvts/>')
        print(response)

    def get_nvt_families(self):
        response = self.execute_xml_command('<get_nvt_families/>')
        print(response)

    def get_nvt_feed_version(self):
        response = self.execute_xml_command('<get_nvt_feed_version/>')
        print(response)

    def get_overrides(self):
        response = self.execute_xml_command('<get_overrides/>')
        print(response)

    def get_permissions(self):
        response = self.execute_xml_command('<get_permissions/>')
        print(response)

    def get_port_lists(self):
        response = self.execute_xml_command('<get_port_lists/>')
        print(response)

    def get_preferences(self):
        response = self.execute_xml_command('<get_preferences/>')
        print(response)

    def get_reports(self):
        response = self.execute_xml_command('<get_reports/>')
        print(response)

    def get_report_formats(self):
        response = self.execute_xml_command('<get_report_formats/>')
        print(response)

    def get_results(self):
        response = self.execute_xml_command('<get_results/>')
        print(response)

    def get_roles(self):
        response = self.execute_xml_command('<get_roles/>')
        print(response)

    def get_scanners(self):
        response = self.execute_xml_command('<get_scanners/>')
        print(response)

    def get_schedules(self):
        response = self.execute_xml_command('<get_schedules/>')
        print(response)

    def get_settings(self):
        response = self.execute_xml_command('<get_settings/>')
        print(response)

    def get_slaves(self):
        response = self.execute_xml_command('<get_slaves/>')
        print(response)

    def get_system_reports(self):
        response = self.execute_xml_command('<get_system_reports/>')
        print(response)

    def get_tags(self):
        response = self.execute_xml_command('<get_tags/>')
        print(response)

    def get_targets(self):
        response = self.execute_xml_command('<get_targets/>')
        print(response)

    def get_tasks(self):
        response = self.execute_xml_command('<get_tasks/>')
        print(response)

    def get_users(self):
        response = self.execute_xml_command('<get_users/>')
        print(response)

    def get_versions(self):
        response = self.execute_xml_command('<get_versions/>')
        print(response)






