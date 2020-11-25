from module.protocol.network.message import Message


class InteractiveUseErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9202
        self.elemId = {"type": "uint", "value": ""}
        self.skillInstanceUid = {"type": "uint", "value": ""}
