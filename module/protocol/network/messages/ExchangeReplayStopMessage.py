from module.protocol.network.message import Message


class ExchangeReplayStopMessage(Message):
    def __init__(self):
        self.id = 2959
