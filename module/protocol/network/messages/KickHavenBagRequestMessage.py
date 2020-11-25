from module.protocol.network.message import Message


class KickHavenBagRequestMessage(Message):
    def __init__(self):
        self.id = 711
