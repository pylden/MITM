from module.protocol.network.message import Message


class MountInformationRequestMessage(Message):
    def __init__(self):
        self.id = 5729
