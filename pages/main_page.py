from .base_page import BasePage    #импорт класса из соседнего фала


class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)