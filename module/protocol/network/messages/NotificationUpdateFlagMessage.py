from module.protocol.network.message import Message


class NotificationUpdateFlagMessage(Message):
    def __init__(self):
        self.id = 6989
