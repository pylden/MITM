from module.protocol.network.message import Message


class NotificationUpdateFlagMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 6989
        self.index = {"type": "uint", "value": ""}
