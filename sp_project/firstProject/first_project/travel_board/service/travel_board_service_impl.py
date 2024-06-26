from travel_board.repository.travel_board_repository_impl import TravelBoardRepositoryImpl
from travel_board.service.travel_board_service import TravelBoardService
# 240621
class TravelBoardServiceImpl(TravelBoardService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.__travelBoardRepository = TravelBoardRepositoryImpl.getInstance()
            return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def list(self):
        return self.__travelBoardRepository.list()

    def createTravelBoard(self, title, point, writer, review, reviewimage):
        return self.__travelBoardRepository.create(
            title, point, writer, review, reviewimage)

    def readTravelBoard(self, travelBoardId):
        return self.__travelBoardRepository.findByTravelBoardId(travelBoardId)

    def removeTravelBoard(self, travelBoardId):
        return self.__travelBoardRepository.deleteByTravelBoardId(travelBoardId)

    def updateTravelBoard(self, travelBoardId, travelBoardData):
        travel_board = self.__travelBoardRepository.findByTravelBoardId(travelBoardId)
        updatedTravelBoard = self.__travelBoardRepository.update(travel_board, travelBoardData)
        return updatedTravelBoard
