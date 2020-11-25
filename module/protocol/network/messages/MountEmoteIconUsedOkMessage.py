from module.protocol.network.message import Message


class MountEmoteIconUsedOkMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4039
        self.mountId = {"type": "int", "value": ""}
        self.reactionType = {"type": "uint", "value": ""}
