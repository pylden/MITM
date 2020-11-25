from module.protocol.network.message import Message


class DungeonKeyRingMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6151
        self.availables = {"type": "Vector.<uint>", "value": ""}
        self.unavailables = {"type": "Vector.<uint>", "value": ""}
