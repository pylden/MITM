from module.protocol.network.message import Message


class MountToggleRidingRequestMessage(Message):
    def __init__(self):
        self.id = 9639
