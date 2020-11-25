from module.protocol.network.message import Message


class MountEmoteIconUsedOkMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4039
        self.mountId = {"type": "int", "value": ""}
        self.reactionType = {"type": "uint", "value": ""}
