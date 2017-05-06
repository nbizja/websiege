from core.openvas.models.base_openvas import BaseOpenVAS

class Target(BaseOpenVAS):
    """OpenVAS target"""

    properties = ['id', 'owner', 'name', 'comment', 'creation_time', 'port_list', 'alive_tests',
                  'modification_time', 'writable', 'in_use', 'permissions', 'user_tags', 'hosts',
                 'exclude_hosts', 'max_hosts', 'port_list', 'ssh_lsc_credential', '﻿smb_lsc_credential',
                 'esxi_lsc_credential', 'reverse_lookup_only', 'reverse_lookup_unify', 'alive_tests']

    def __init__(self, data):
        super().__init__(Target.properties, data)
