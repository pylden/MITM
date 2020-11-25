from module.protocol.network.message import Message


class ChatServerCopyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5867
        self.receiverId = {"type": "Number", "value": ""}
        self.receiverName = {"type": "String", "value": ""}
