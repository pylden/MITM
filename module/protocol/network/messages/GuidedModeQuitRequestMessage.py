from module.protocol.network.message import Message


class GuidedModeQuitRequestMessage(Message):
    def __init__(self):
        self.id = 2026
