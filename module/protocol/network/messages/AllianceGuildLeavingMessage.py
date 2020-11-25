from module.protocol.network.message import Message


class AllianceGuildLeavingMessage(Message):
    def __init__(self):
        self.id = 2611
