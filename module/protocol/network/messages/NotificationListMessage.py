from module.protocol.network.message import Message


class NotificationListMessage(Message):
    def __init__(self):
        self.id = 3042
