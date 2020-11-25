from module.protocol.network.message import Message


class InteractiveUseErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9202
        self.elemId = {"type": "uint", "value": ""}
        self.skillInstanceUid = {"type": "uint", "value": ""}
