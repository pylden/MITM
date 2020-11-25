from module.protocol.network.message import Message


class ChatServerCopyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5867
        self.receiverId = {"type": "Number", "value": ""}
        self.receiverName = {"type": "String", "value": ""}
