from module.protocol.network.message import Message


class ShortcutBarRefreshMessage(Message):
    def __init__(self):
        self.id = 9875
