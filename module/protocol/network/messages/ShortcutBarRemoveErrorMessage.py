from module.protocol.network.message import Message


class ShortcutBarRemoveErrorMessage(Message):
    def __init__(self):
        self.id = 5768
