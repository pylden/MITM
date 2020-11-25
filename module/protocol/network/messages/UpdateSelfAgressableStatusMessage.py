from module.protocol.network.message import Message


class UpdateSelfAgressableStatusMessage(Message):
    def __init__(self):
        self.id = 1451
