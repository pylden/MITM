from module.protocol.network.messages.ObjectErrorMessage import ObjectErrorMessage


class SymbioticObjectErrorMessage(ObjectErrorMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        ObjectErrorMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 1383
        self.vars.append({"name": "errorCode", "type": "int", "value": ""})
