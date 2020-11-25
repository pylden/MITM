from module.protocol.network.message import Message


class ExitHavenBagRequestMessage(Message):
    def __init__(self):
        self.id = 8249
