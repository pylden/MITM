from module.protocol.network.message import Message


class NpcDialogQuestionMessage(Message):
    def __init__(self, buffer_reader, len_type, length):
        Message.__init__(self, buffer_reader, len_type, length)
        self.id = 5895
        self.messageId = {"type": "uint", "value": ""}
        self.dialogParams = {"type": "Vector.<String>", "value": ""}
        self.visibleReplies = {"type": "Vector.<uint>", "value": ""}
