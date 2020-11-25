from module.protocol.network.message import Message


class AllianceCreationStartedMessage(Message):
    def __init__(self):
        self.id = 5298
