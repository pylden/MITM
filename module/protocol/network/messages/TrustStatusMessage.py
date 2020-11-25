from module.protocol.network.message import Message


class TrustStatusMessage(Message):
    def __init__(self):
        self.id = 2030
