from module.protocol.network.message import Message


class ObjectErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5736
        self.reason = {"type": "int", "value": ""}
