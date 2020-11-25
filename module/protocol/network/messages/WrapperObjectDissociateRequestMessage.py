from module.protocol.network.message import Message


class WrapperObjectDissociateRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9939
        self.hostUID = {"type": "uint", "value": ""}
        self.hostPos = {"type": "uint", "value": ""}
