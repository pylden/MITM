from module.protocol.network.message import Message


class BreachRoomUnlockRequestMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2349
        self.roomId = {"type": "uint", "value": ""}
