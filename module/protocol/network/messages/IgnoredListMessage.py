from module.protocol.network.message import Message


class IgnoredListMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 8697
        self.ignoredList = {"type": "Vector.<IgnoredInformations>", "value": ""}
