from module.protocol.network.message import Message


class InventoryContentMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4140
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
        self.kamas = {"type": "Number", "value": ""}
