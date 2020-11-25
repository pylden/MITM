from module.protocol.network.message import Message


class PrismFightJoinLeaveRequestMessage(Message):
    def __init__(self):
        self.id = 7685
