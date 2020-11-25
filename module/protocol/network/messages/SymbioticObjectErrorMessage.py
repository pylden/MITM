from module.protocol.network.message import Message


class SymbioticObjectErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1383
        self.errorCode = {"type": "int", "value": ""}
