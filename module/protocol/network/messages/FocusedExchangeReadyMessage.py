from module.protocol.network.message import Message


class FocusedExchangeReadyMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9510
        self.focusActionId = {"type": "uint", "value": ""}
