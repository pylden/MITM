from module.protocol.network.message import Message


class PrismFightDefenderLeaveMessage(Message):
    def __init__(self):
        self.id = 9060
