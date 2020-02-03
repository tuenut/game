from abc import ABCMeta, abstractmethod

from abstractions.data.bases import ABCDataMaterialEntity


class ABCDataCharacter(ABCDataMaterialEntity, metaclass=ABCMeta):
    @property
    def sirializing_fields(self):
        return ["name", "type", "location", "id"]
