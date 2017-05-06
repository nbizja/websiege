from cement.core.controller import CementBaseController, expose


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = "My Application does amazing things!"
        arguments = [
            (['-f', '--foo'],
              dict(action='store', help='the notorious foo option')),
            (['-C'],
              dict(action='store_true', help='the big C option')),
            ]

    @expose(hide=True)
    def default(self):
        self.app.log.info('Inside MyBaseController.default()')
        if self.app.pargs.foo:
            print("Recieved option: foo => %s" % self.app.pargs.foo)
