from abc import ABC,abstractmethod


class Devices_dao(ABC):

    @abstractmethod
    def get_all(self):
        # Retorna todo los dispositivos
        pass

    @abstractmethod
    def get_by_id(self,id:int):
        # Retorna un dispositivo
        pass

    @abstractmethod
    def delete_by_id(self,id:int):
        # Elimin un dispositivo
        pass

    @abstractmethod
    def update(self,id:int,data:dict):
        # Actualiza un dispositivo
        pass

    @abstractmethod
    def post(self,data:dict):
        # Crea un dispositivo
        pass

    @abstractmethod
    def get_status(self,id:int):
        # Devuelve el estado del dispositivo
        pass
    
    @abstractmethod
    def set_status(self,id:int):
        # Modifica el estado del dispositivo
        pass