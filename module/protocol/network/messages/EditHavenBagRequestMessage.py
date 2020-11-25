from module.protocol.network.message import Message


class EditHavenBagRequestMessage(Message):
    def __init__(self):
        self.id = 529
