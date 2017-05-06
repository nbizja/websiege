class MappingException(Exception):
    pass


class NonExistingPropertyException(MappingException):
    def __init__(self, attribute):
        self.message = 'Property %s does not exist in %s.' % (attribute, __class__.__name__)

