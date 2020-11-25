from module.protocol.network.message import Message


class AllianceFactsErrorMessage(Message):
    def __init__(self):
        self.id = 2007
