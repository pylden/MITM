from module.protocol.network.message import Message


class AllianceKickRequestMessage(Message):
    def __init__(self):
        self.id = 9735