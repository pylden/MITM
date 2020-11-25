from module.protocol.network.message import Message


class WatchInventoryContentMessage(Message):
    def __init__(self):
        self.id = 7807
