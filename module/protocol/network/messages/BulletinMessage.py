from module.protocol.network.message import Message


class BulletinMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5698
        self.lastNotifiedTimestamp = {"type": "uint", "value": ""}
