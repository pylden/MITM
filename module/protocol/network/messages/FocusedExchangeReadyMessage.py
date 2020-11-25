from module.protocol.network.message import Message


class FocusedExchangeReadyMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 9510
        self.focusActionId = {"type": "uint", "value": ""}
