from module.protocol.network.message import Message


class StartupActionsExecuteMessage(Message):
    def __init__(self):
        self.id = 2943
