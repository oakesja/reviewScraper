class GameDescription(object):
    def __init__(self, description=None, releaseDate=None, boxArtLink=None, esrb=None, genre=None, publisher=None, developer=None):
        self._description = description
        self._releaseDate = releaseDate
        self._boxArtLink = boxArtLink
        self._esrb = esrb
        self._genre = genre
        self._publisher = publisher
        self._developer = developer

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @description.deleter
    def description(self):
        del self._description

    @property
    def releaseDate(self):
        return self._releaseDate

    @releaseDate.setter
    def releaseDate(self, value):
        self._releaseDate = value

    @releaseDate.deleter
    def releaseDate(self):
        del self._releaseDate

    @property
    def boxArtLink(self):
        return self._boxArtLink

    @boxArtLink.setter
    def boxArtLink(self, value):
        self._boxArtLink = value

    @boxArtLink.deleter
    def boxArtLink(self):
        del self._boxArtLink

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        self._genre = value

    @genre.deleter
    def genre(self):
        del self._genre

    @property
    def publisher(self):
        return self._publisher

    @publisher.setter
    def publisher(self, value):
        self._publisher = value

    @publisher.deleter
    def publisher(self):
        del self._publisher

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, value):
        self._developer = value

    @developer.deleter
    def developer(self):
        del self._developer