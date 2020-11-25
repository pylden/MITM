from module.protocol.network.message import Message


class AbstractGameActionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3972
        self.actionId = {"type": "uint", "value": ""}
        self.sourceId = {"type": "Number", "value": ""}
