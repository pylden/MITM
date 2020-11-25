from module.protocol.network.message import Message


class CheckIntegrityMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8606
        self.data = {"type": "Vector.<int>", "value": ""}
