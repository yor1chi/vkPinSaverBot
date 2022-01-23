import vk_api
from vk_api.bot_longpoll import VkBotLongPoll
import os


class Connection:
    __server = os.environ['SERVER']
    __token = os.environ['TOKEN']
    __key = os.environ['KEY']
    __ts = os.environ['TS']
    __groupId = os.environ['GROUP_ID']

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
