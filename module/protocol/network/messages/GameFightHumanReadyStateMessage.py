from module.protocol.network.message import Message


class GameFightHumanReadyStateMessage(Message):
    def __init__(self):
        self.id = 386
