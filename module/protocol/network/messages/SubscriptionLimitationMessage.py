from module.protocol.network.message import Message


class SubscriptionLimitationMessage(Message):
    def __init__(self):
        self.id = 8198
