from module.protocol.network.message import Message


class AllianceJoinedMessage(Message):
    def __init__(self):
        self.id = 6500
