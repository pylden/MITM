from module.protocol.network.message import Message


class LoginQueueStatusMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7010
        self.position = {"type": "uint", "value": ""}
        self.total = {"type": "uint", "value": ""}
