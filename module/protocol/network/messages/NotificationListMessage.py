from module.protocol.network.message import Message


class NotificationListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 3042
        self.flags = {"type": "Vector.<int>", "value": ""}
