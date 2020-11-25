from module.protocol.network.message import Message


class ChatServerCopyWithObjectMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 4706
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
