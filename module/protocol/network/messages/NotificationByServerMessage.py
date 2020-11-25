from module.protocol.network.message import Message


class NotificationByServerMessage(Message):
    def __init__(self):
        self.id = 312
