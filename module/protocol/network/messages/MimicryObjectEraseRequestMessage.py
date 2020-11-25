from module.protocol.network.message import Message


class MimicryObjectEraseRequestMessage(Message):
    def __init__(self):
        self.id = 1801
