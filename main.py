from cement.core.foundation import CementApp
from cli.controllers.base_controller import BaseController
from cli.controllers.omp_controller import OmpController

class WebSiege(CementApp):
    class Meta:
        label = 'websiege'
        base_controller = 'base'
        handlers = [BaseController, OmpController]
        extensions = ['yaml']
        config_handler = 'yaml'
        config_files = [
            './config/openvas.yml'
        ]


def main():
    with WebSiege() as app:
        app.setup()
        app.run()

if __name__ == '__main__':
    main()