class BaseAttributeModifier:
    """
    Модификатор используется для влияния на характеристики.
    value - числовое значение int или float
    source - источник модификатора(например, расовая особенность)
    description - описание
    id - уникальный идентификатор, передаваемый при инициализации
    """

    def __init__(self, value, increment_id, source=None, description=None):
        self.value = value
        self.source = source
        self.description = description
        self.id = increment_id

    def __radd__(self, other):
        """для работы sum() со списком модификаторов"""
        return self.value + other
