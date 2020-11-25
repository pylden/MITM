from module.protocol.network.message import Message


class IgnoredAddedMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 2861
        self.ignoreAdded = {"type": "IgnoredInformations", "value": ""}
        self.session = {"type": "Boolean", "value": ""}
