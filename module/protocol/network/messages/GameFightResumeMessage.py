from module.protocol.network.messages.GameFightSpectateMessage import GameFightSpectateMessage


class GameFightResumeMessage(GameFightSpectateMessage):
    def __init__(self, buffer_reader, len_type, length, count=None):
        GameFightSpectateMessage.__init__(self, buffer_reader, len_type, length, count)
        self.id = 7999
        self.vars.append({"name": "spellCooldowns", "type": "Vector.<GameFightSpellCooldown>", "value": ""})
        self.vars.append({"name": "summonCount", "type": "uint", "value": ""})
        self.vars.append({"name": "bombCount", "type": "uint", "value": ""})
