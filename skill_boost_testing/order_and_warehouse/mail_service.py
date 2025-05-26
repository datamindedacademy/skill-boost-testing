from abc import ABC, abstractmethod


class MailService(ABC):
    @abstractmethod
    def send(self, message: str) -> None:
        pass
