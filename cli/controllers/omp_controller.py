from cement.core.controller import CementBaseController, expose
from cli.controllers.abstract_base_controller import AbstractBaseController
from core.openvas.client.omp import Omp


class OmpController(AbstractBaseController):
    class Meta:
        label = 'omp'
        stacked_on = 'base'
        stacked_type = 'nested'

    def _setup(self, app):
        super(AbstractBaseController, self)._setup(app)

        self.omp = Omp(app.config.get_section_dict('openvas'))



#####################
# DIRECT OMP METHODS
#####################

    @expose()
    def start_task(self):
        AbstractBaseController.assertRequiredArguments(self, 1, 'TaskId')
        taskId = self.app.pargs.extra_arguments[0]
        self.omp.start_task(taskId)

    @expose(help="Get help text")
    def help(self):
        self.omp.help()

    @expose()
    def get_agents(self):
        response = self.omp.get_agents()
        
    @expose()
    def get_aggregates(self, type):
        response = self.omp.get_aggregates(type)

    @expose()
    def get_alerts(self):
        response = self.omp.get_alerts()

    @expose(help="Get all agents")
    def get_configs(self):
        self.omp.get_configs()

    @expose()
    def get_filters(self):
        response = self.omp.get_filters()

    @expose()
    def get_groups(self):
        response = self.omp.get_groups()

    @expose()
    def get_info(self):
        response = self.omp.get_info()

    @expose()
    def get_lsc_credentials(self):
        response = self.omp.get_lsc_credentials()

    @expose()
    def get_notes(self):
        response = self.omp.get_notes()

    @expose()
    def get_nvts(self):
        response = self.omp.get_nvts()

    @expose()
    def get_nvt_families(self):
        response = self.omp.get_nvt_families()

    @expose()
    def get_nvt_feed_version(self):
        response = self.omp.get_nvt_feed_version()

    @expose()
    def get_overrides(self):
        response = self.omp.get_overrides()
        
    @expose()
    def get_permissions(self):
        response = self.omp.get_permissions()
        
    @expose()
    def get_port_lists(self):
        response = self.omp.get_port_lists()
        
    @expose()
    def get_preferences(self):
        response = self.omp.get_preferences()
        
    @expose()
    def get_reports(self):
        response = self.omp.get_reports()
        
    @expose()
    def get_preport_formats(self):
        response = self.omp.get_report_formats()
        
    @expose()
    def get_results(self):
        response = self.omp.get_results()

    @expose()
    def get_roles(self):
        response = self.omp.get_roles()
        
    @expose()
    def get_scanners(self):
        response = self.omp.get_scanners()
        
    @expose()
    def get_schedules(self):
        response = self.omp.get_schedules()
        
    @expose()
    def get_settings(self):
        response = self.omp.get_settings()
        
    @expose()
    def get_slaves(self):
        response = self.omp.get_slaves()
        
    @expose()
    def get_system_reports(self):
        response = self.omp.get_system_reports()
        
    @expose()
    def get_tags(self):
        response = self.omp.get_tags()
        
    @expose()
    def get_targets(self):
        response = self.omp.get_targets()
        
    @expose()
    def get_tasks(self):
        response = self.omp.get_tasks()
        
    @expose()
    def get_users(self):
        response = self.omp.get_users()
        
    @expose()
    def get_versions(self):
        response = self.omp.get_versions()
        


