#class: UserEventPointsBoard

class UserEventPointsBoard:
    def __init__(self):
        pass

    def setUserId(self, userId):
        self.userId = userId

    def setEventId(self, eventId):
        self.eventId = eventId

    def setTotalPoints(self, totalPoints):
        self.totalPoints = totalPoints

    def setTotalDistanceCovered(self, totalDistanceCovered):
        self.totalDistanceCovered = totalDistanceCovered

    def setAveragePace(self, averagePace):
        self.averagePace = averagePace

    def setTotalElevationGain(self, totalElevationGain):
        self.totalElevationGain = totalElevationGain

    def setBestPace(self, bestPace):
        self.bestPace = bestPace

    def setHighestElevation(self, highestElevation):
        self.highestElevation = highestElevation

    def setLongestDistanceInSingleActivity(self, longestDistanceInSingleActivity):
        self.longestDistanceInSingleActivity = longestDistanceInSingleActivity

    def setLatestActivityId(self, latestActivityId):
        self.latestActivityId = latestActivityId