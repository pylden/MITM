from module.protocol.network.message import Message


class ShortcutBarSwapErrorMessage(Message):
    def __init__(self):
        self.id = 8919
