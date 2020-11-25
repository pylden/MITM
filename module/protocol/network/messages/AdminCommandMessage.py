from module.protocol.network.message import Message


class AdminCommandMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(self, buffer_reader)
        self.id = 5178
        self.content = {"type": "String", "value": ""}
