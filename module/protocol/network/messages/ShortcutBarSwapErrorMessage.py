from module.protocol.network.message import Message


class ShortcutBarSwapErrorMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8919
        self.error = {"type": "uint", "value": ""}
