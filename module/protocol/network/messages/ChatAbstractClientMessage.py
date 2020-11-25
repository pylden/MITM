from module.protocol.network.message import Message


class ChatAbstractClientMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8438
        self.content = {"type": "String", "value": ""}
