from module.protocol.network.message import Message


class InventoryContentMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4140
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
        self.kamas = {"type": "Number", "value": ""}
