from module.protocol.network.message import Message


class IgnoredListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8697
        self.ignoredList = {"type": "Vector.<IgnoredInformations>", "value": ""}
