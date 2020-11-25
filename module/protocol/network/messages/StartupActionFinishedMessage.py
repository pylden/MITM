from module.protocol.network.message import Message


class StartupActionFinishedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3256
        self.success = {"type": "Boolean", "value": ""}
        self.actionId = {"type": "uint", "value": ""}
        self.automaticAction = {"type": "Boolean", "value": ""}
