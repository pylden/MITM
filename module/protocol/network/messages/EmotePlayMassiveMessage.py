from module.protocol.network.message import Message


class EmotePlayMassiveMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9926
        self.actorIds = {"type": "Vector.<Number>", "value": ""}
