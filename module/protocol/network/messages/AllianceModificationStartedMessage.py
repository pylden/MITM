from module.protocol.network.message import Message


class AllianceModificationStartedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2652
        self.canChangeName = {"type": "Boolean", "value": ""}
        self.canChangeTag = {"type": "Boolean", "value": ""}
        self.canChangeEmblem = {"type": "Boolean", "value": ""}
