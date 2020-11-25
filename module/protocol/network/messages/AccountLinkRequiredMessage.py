from module.protocol.network.message import Message


class AccountLinkRequiredMessage(Message):
    def __init__(self):
        self.id = 5001
