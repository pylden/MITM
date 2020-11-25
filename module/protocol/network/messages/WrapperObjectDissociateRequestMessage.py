from module.protocol.network.message import Message


class WrapperObjectDissociateRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9939
        self.hostUID = {"type": "uint", "value": ""}
        self.hostPos = {"type": "uint", "value": ""}
