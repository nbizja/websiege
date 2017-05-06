from core.openvas.exceptions.bad_request import NonExistingPropertyException


class BaseOpenVAS():
    def __init__(self, attributes, data):
        for attr in attributes:
            if attr not in data:
                raise NonExistingPropertyException()
            self.attr = data[attr]