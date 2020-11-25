from module.protocol.network.message import Message


class GameActionAcknowledgementMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7836
        self.valid = {"type": "Boolean", "value": ""}
        self.actionId = {"type": "int", "value": ""}
