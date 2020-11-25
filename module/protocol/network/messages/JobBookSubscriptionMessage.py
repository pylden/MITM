from module.protocol.network.message import Message


class JobBookSubscriptionMessage(Message):
    def __init__(self):
        self.id = 9091
