class UndergroundSystem:

    def __init__(self):
        self.start_info = dict()
        self.time_table= dict()
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.start_info[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_time = self.start_info[id][1]
        idx_se = (self.start_info[id][0], stationName)
        rec = self.time_table.get(idx_se, (0,0))
        self.time_table[idx_se] = (rec[0]+t-start_time, rec[1]+1)
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        idx_se = (startStation, endStation)
        time_total, people= self.time_table[idx_se]
        return time_total/people
