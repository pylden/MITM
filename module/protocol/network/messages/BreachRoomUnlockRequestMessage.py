from module.protocol.network.message import Message


class BreachRoomUnlockRequestMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2349
        self.roomId = {"type": "uint", "value": ""}
