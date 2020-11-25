from module.protocol.network.message import Message


class ChangeHavenBagRoomRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9569
        self.roomId = {"type": "uint", "value": ""}
