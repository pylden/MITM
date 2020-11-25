from module.protocol.network.message import Message


class SymbioticObjectAssociateRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5840
        self.symbioteUID = {"type": "uint", "value": ""}
        self.symbiotePos = {"type": "uint", "value": ""}
        self.hostUID = {"type": "uint", "value": ""}
        self.hostPos = {"type": "uint", "value": ""}
