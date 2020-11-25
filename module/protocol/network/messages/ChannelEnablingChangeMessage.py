from module.protocol.network.message import Message


class ChannelEnablingChangeMessage(Message):
    def __init__(self):
        self.id = 3541
