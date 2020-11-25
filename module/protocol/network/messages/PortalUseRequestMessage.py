from module.protocol.network.message import Message


class PortalUseRequestMessage(Message):
    def __init__(self):
        self.id = 9046
