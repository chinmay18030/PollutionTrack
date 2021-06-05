# importing the required modules
import json
import requests
import matplotlib.pyplot as plt


# Tracking pollution level
class TrackPollution:
    def __init__(self, city):
        self.city = city
        self.data = requests.get(
            'https://api.waqi.info/feed/' + self.city + '/?token=43cc1b7292dc59c1d09922d50a882c478d1717af')
        self.api = json.loads(self.data.content)
        self.x = []
        self.y = []

# write the date in the form of year-month-date
    def trackPm25(self, stats_type):
        # types here are avg, min, max
        pm25 = self.api['data']["forecast"]["daily"]["pm25"][2]
        avg = pm25["avg"]
        min = pm25["min"]
        max = pm25["max"]
        if stats_type == "avg":
            return avg
        elif stats_type == "min":
            return min
        elif stats_type == "max":
            return max
        else:
            raise NameError("No " + stats_type + " found in the types of stat")

    def trackPm10(self, stats_type):
        # types here are avg, min, max
        struc = self.api['data']["forecast"]["daily"]["pm10"][2]
        avg = struc["avg"]
        min = struc["min"]
        max = struc["max"]
        if stats_type == "avg":
            return avg
        elif stats_type == "min":
            return min
        elif stats_type == "max":
            return max
        else:
            raise NameError("No " + stats_type + " found in the types of stat")

    def track03(self, stats_type):
        # types here are avg, min, max
        struc = self.api['data']["forecast"]["daily"]["o3"][2]
        avg = struc["avg"]
        min = struc["min"]
        max = struc["max"]
        if stats_type == "avg":
            return avg
        elif stats_type == "min":
            return min
        elif stats_type == "max":
            return max
        else:
            raise NameError("No " + stats_type + " found in the types of stat")

    def plotTracking(self,pollutant_type):
        plt.title(self.city)
        if pollutant_type == "PM 2.5":
            pm25 = self.api['data']["forecast"]["daily"]["pm25"]
            for i in pm25:
                pl = i["avg"]
                date = i["day"]
                self.x.append(pl)
                self.y.append(date)
            plt.plot(self.y, self.x, label="Pm 2.5 Level")
            plt.legend()
            plt.show()

        elif pollutant_type == "PM 10":
            pm25 = self.api['data']["forecast"]["daily"]["pm10"]
            for i in pm25:
                pl = i["avg"]
                date = i["day"]
                self.x.append(pl)
                self.y.append(date)
            plt.plot(self.y, self.x, label="Pm 10 Level")
            plt.legend()
            plt.show()

        elif pollutant_type == "O3":
            pm25 = self.api['data']["forecast"]["daily"]["o3"]
            for i in pm25:
                pl = i["avg"]
                date = i["day"]
                self.x.append(pl)
                self.y.append(date)
            plt.plot(self.y, self.x, label="Pm O3 Level")
            plt.legend()
            plt.show()
        else:
            raise NameError(f'{pollutant_type} not found in pollutant type')


pol = TrackPollution("Noida")
pol.plotTracking("PM 2.5")
