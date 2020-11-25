from module.protocol.network.message import Message


class NpcDialogQuestionMessage(Message):
    def __init__(self, buffer_reader):
        Message.__init__(buffer_reader)
        self.id = 5895
        self.messageId = {"type": "uint", "value": ""}
        self.dialogParams = {"type": "Vector.<String>", "value": ""}
        self.visibleReplies = {"type": "Vector.<uint>", "value": ""}
