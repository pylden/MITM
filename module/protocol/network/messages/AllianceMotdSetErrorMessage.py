from module.protocol.network.message import Message


class AllianceMotdSetErrorMessage(Message):
    def __init__(self):
        self.id = 1499
