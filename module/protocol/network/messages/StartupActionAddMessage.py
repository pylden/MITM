from module.protocol.network.message import Message


class StartupActionAddMessage(Message):
    def __init__(self):
        self.id = 9836
