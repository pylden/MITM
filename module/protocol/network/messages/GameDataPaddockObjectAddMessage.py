from module.protocol.network.message import Message


class GameDataPaddockObjectAddMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 7563
        self.paddockItemDescription = {"type": "PaddockItem", "value": ""}
