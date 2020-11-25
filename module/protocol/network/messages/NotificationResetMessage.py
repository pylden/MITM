from module.protocol.network.message import Message


class NotificationResetMessage(Message):
    def __init__(self):
        self.id = 2913
