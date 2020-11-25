from module.protocol.network.message import Message


class IgnoredAddedMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 2861
        self.ignoreAdded = {"type": "IgnoredInformations", "value": ""}
        self.session = {"type": "Boolean", "value": ""}
