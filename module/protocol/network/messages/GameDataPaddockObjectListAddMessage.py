from module.protocol.network.message import Message


class GameDataPaddockObjectListAddMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3488
        self.paddockItemDescription = {"type": "Vector.<PaddockItem>", "value": ""}
