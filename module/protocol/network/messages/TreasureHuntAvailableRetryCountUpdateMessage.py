from module.protocol.network.message import Message


class TreasureHuntAvailableRetryCountUpdateMessage(Message):
    def __init__(self):
        self.id = 4986
