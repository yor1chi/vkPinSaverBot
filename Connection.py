import vk_api
from vk_api.bot_longpoll import VkBotLongPoll


class Connection:
    __server = 'your_server'
    __token = 'your token'
    __key = 'your key'
    __ts = 'your ts'
    __groupId = 'your group id'

    def getServer(self):
        return self.__server

    def getToken(self):
        return self.__token

    def getKey(self):
        return self.__key

    def getTs(self):
        return self.__ts

    def getGroupId(self):
        return self.__groupId

    def createSession(self):
        vk_session = vk_api.VkApi(token=self.__token)
        longpoll = VkBotLongPoll(vk_session, self.__groupId)
        vk = vk_session.get_api()
        return [longpoll, vk]
