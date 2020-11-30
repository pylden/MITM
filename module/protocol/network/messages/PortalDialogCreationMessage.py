from module.protocol.network.messages.NpcDialogCreationMessage import NpcDialogCreationMessage


class PortalDialogCreationMessage(NpcDialogCreationMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        NpcDialogCreationMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 4988
        self.type = {"type": "uint", "value": ""}
