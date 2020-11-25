from module.protocol.network.message import Message


class CredentialsAcknowledgementMessage(Message):
    def __init__(self):
        self.id = 9930
