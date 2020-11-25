from module.protocol.network.message import Message


class StartupActionFinishedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3256
        self.success = {"type": "Boolean", "value": ""}
        self.actionId = {"type": "uint", "value": ""}
        self.automaticAction = {"type": "Boolean", "value": ""}
