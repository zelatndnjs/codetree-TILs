class Weather:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())
tuples = [tuple(input().split()) for _ in range(n)]
weathers = [Weather(date,day,weather) for date, day, weather in tuples]
sorted_weathers = sorted([w for w in weathers if w.weather=='Rain'], key= lambda x: x.date)
print(sorted_weathers[0].date, sorted_weathers[0].day, sorted_weathers[0].weather)