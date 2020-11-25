from module.protocol.network.message import Message


class StartupActionsListMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 1192
        self.actions = {"type": "Vector.<StartupActionAddObject>", "value": ""}
