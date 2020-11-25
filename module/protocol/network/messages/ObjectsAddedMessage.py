from module.protocol.network.message import Message


class ObjectsAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 6913
        self.object = {"type": "Vector.<ObjectItem>", "value": ""}
