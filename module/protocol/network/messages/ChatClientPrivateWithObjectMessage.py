from module.protocol.network.message import Message


class ChatClientPrivateWithObjectMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2672
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
