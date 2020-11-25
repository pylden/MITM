from module.protocol.network.message import Message


class ShortcutBarAddRequestMessage(Message):
    def __init__(self):
        self.id = 2373
