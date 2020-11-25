from module.protocol.network.message import Message


class AllianceChangeGuildRightsMessage(Message):
    def __init__(self):
        self.id = 8726
