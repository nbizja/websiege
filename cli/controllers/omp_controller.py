from cement.core.controller import CementBaseController, expose

from core.openvas.client.omp import Omp


class OmpController(CementBaseController):
    class Meta:
        label = 'omp'
        stacked_on = 'base'
        stacked_type = 'embedded'

    def _setup(self, app):
        super(CementBaseController, self)._setup(app)

        # add a common object that will be used in any sub-class

        self.omp = Omp(app.config.get_section_dict('openvas'))

    @expose(help="Shows available commands ")
    def help(self):
        self.app.log.info("Inside MyBaseController.command1()")
        self.omp.help()

    @expose(aliases=['cmd2'], help="more of nothing")
    def get_configs(self):
        self.app.log.info("Inside MyBaseController.command2()")