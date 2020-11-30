from module.protocol.network.messages.JobAllowMultiCraftRequestMessage import JobAllowMultiCraftRequestMessage


class JobMultiCraftAvailableSkillsMessage(JobAllowMultiCraftRequestMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        JobAllowMultiCraftRequestMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 834
        self.playerId = {"type": "Number", "value": ""}
        self.skills = {"type": "Vector.<uint>", "value": ""}
