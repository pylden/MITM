from module.protocol.network.message import Message


class GameDataPaddockObjectAddMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 7563
        self.paddockItemDescription = {"type": "PaddockItem", "value": ""}
