from module.protocol.network.message import Message


class EnabledChannelsMessage(Message):
    def __init__(self):
        self.id = 2771
