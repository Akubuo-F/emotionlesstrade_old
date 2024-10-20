from abc import ABC, abstractmethod


class AbstractDirectoryHelper(ABC):

    @staticmethod
    @abstractmethod
    def root_dir() -> str:
        ...