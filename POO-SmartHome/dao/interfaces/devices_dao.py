from abc import ABC,abstractmethod


class Devices_dao(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def get_by_id(self,id:int):
        pass

    @abstractmethod
    def delete_by_id(self,id:int):
        pass

    @abstractmethod
    def update(self,id:int,data:dict):
        pass