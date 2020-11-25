from module.protocol.network.message import Message


class BreachRoomUnlockResultMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7688
        self.roomId = {"type": "uint", "value": ""}
        self.result = {"type": "uint", "value": ""}
