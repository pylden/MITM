from module.protocol.network.message import Message


class ShortcutBarAddErrorMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 788
        self.error = {"type": "uint", "value": ""}
