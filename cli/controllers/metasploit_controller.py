from cement.core.controller import expose
from cli.controllers.abstract_base_controller import AbstractBaseController
from core.metasploit.client.metasploit import Metasploit

class MetasploitController(AbstractBaseController):
    class Meta:
        label = 'metasploit'
        stacked_on = 'base'
        stacked_type = 'nested'

    def _setup(self, app):
        super(AbstractBaseController, self)._setup(app)

        self.metasploit = Metasploit()

    @expose()
    def help(self):
        self.metasploit.help()

    @expose()
    def db_nmap(self):
        AbstractBaseController.assertRequiredArguments(self, 1, 'ip')
        ip = self.app.pargs.extra_arguments[0]

        self.metasploit.db_nmap(ip)

    @expose()
    def services(self):
        self.metasploit.services()

