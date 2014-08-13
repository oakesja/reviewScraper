class Review(object):
    def __init__(self, rating=None, ratingDescription=None, communityRating=None, communityDescripton=None, communityCount=None, reviewLink=None, videoReviewLink=None):
        self._rating = rating
        self._ratingDescription = ratingDescription
        self._communityRating = communityRating
        self._communityDescription = communityDescripton
        self._communityCount = communityCount
        self._reviewLink = reviewLink
        self._videoReviewLink = videoReviewLink

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value

    @rating.deleter
    def rating(self):
        del self._rating

    @property
    def ratingDescription(self):
        return self._ratingDescription

    @ratingDescription.setter
    def ratingDescription(self, value):
        self._ratingDescription = value

    @ratingDescription.deleter
    def ratingDescription(self):
        del self._ratingDescription

    @property
    def communityRating(self):
        return self._communityRating

    @communityRating.setter
    def communityRating(self, value):
        self._communityRating = value

    @communityRating.deleter
    def communityRating(self):
        del self._communityRating

    @property
    def communityDescription(self):
        return self._communityDescription

    @communityDescription.setter
    def communityDescription(self, value):
        self._communityDescription = value

    @communityDescription.deleter
    def communityDescription(self):
        del self._communityDescription

    @property
    def communityCount(self):
        return self._communityCount

    @communityCount.setter
    def communityCount(self, value):
        self._communityCount = value

    @communityCount.deleter
    def communityCount(self):
        del self._communityCount

    @property
    def reviewLink(self):
        return self._reviewLink

    @reviewLink.setter
    def reviewLink(self, value):
        self._reviewLink = value

    @reviewLink.deleter
    def reviewLink(self):
        del self._reviewLink

    @property
    def videoReviewLink(self):
        return self._videoReviewLink

    @videoReviewLink.setter
    def videoReviewLink(self, value):
        self._videoReviewLink = value

    @videoReviewLink.deleter
    def videoReviewLink(self):
        del self._videoReviewLink

