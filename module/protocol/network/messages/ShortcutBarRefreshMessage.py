from module.protocol.network.message import Message


class ShortcutBarRefreshMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 9875
        self.barType = {"type": "uint", "value": ""}
        self.shortcut = {"type": "Shortcut", "value": ""}
