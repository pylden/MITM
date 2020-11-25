from module.protocol.network.message import Message


class NotificationListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 3042
        self.flags = {"type": "Vector.<int>", "value": ""}
