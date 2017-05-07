from cement.core.controller import CementBaseController


class AbstractBaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'My Application does amazing things!'
        arguments = [
            (['extra_arguments'],
             dict(action='store', nargs='*'))
            ]

    def assertRequiredArguments(self, expectedArguments, *args):
        if len(self.app.pargs.extra_arguments) != expectedArguments:
            requiredArgs = ''
            for arg in args:
                requiredArgs += arg + ' '
            raise Exception('Invalid number of required arguments. Required: %s' % requiredArgs)

        return True
