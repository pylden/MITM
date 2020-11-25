from module.protocol.network.message import Message


class ChatServerWithObjectMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 4275
        self.objects = {"type": "Vector.<ObjectItem>", "value": ""}
