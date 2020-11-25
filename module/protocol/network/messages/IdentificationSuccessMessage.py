from module.protocol.network.message import Message


class IdentificationSuccessMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 8394
        self.login = {"type": "String", "value": ""}
        self.nickname = {"type": "String", "value": ""}
        self.accountId = {"type": "uint", "value": ""}
        self.communityId = {"type": "uint", "value": ""}
        self.hasRights = {"type": "Boolean", "value": ""}
        self.hasConsoleRight = {"type": "Boolean", "value": ""}
        self.secretQuestion = {"type": "String", "value": ""}
        self.accountCreation = {"type": "Number", "value": ""}
        self.subscriptionElapsedDuration = {"type": "Number", "value": ""}
        self.subscriptionEndDate = {"type": "Number", "value": ""}
        self.wasAlreadyConnected = {"type": "Boolean", "value": ""}
        self.havenbagAvailableRoom = {"type": "uint", "value": ""}
