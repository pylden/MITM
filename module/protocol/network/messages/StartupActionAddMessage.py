from module.protocol.network.message import Message


class StartupActionAddMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9836
        self.newAction = {"type": "StartupActionAddObject", "value": ""}
