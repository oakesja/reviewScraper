class GenericAttribute(object):
    def __init__(self, name, value, page, formatting_method):
        self._name = name
        self._value = value
        self._page = page
        self._formatting_method = formatting_method

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, x):
        self._name = x

    @name.deleter
    def name(self):
        del self._name

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, x):
        self._value = x

    @value.deleter
    def value(self):
        del self._value

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, x):
        self._page = x

    @page.deleter
    def page(self):
        del self._page

    @property
    def formatting_method(self):
        return self._formatting_method

    @formatting_method.setter
    def formatting_method(self, x):
        self._formatting_method = x

    @formatting_method.deleter
    def formatting_method(self):
        del self._formatting_method

    def format_value(self):
        self._value = self._formatting_method(self._value)