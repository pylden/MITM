from module.protocol.network.message import Message


class StartupActionsListMessage(Message):
    def __init__(self):
        self.id = 1192
