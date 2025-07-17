try:
    import ujson as json  # Per MicroPython (al Fire)
except ImportError:
    import json  # Per desenvolupament local (PC)

class FMRadioMem:
    def __init__(self):
        self.filename = 'stations.json'
        self.stations = [0] * 10  # 10 emissores màxim

    def load_stations(self):
        try:
            with open(self.filename, 'r') as file:
                self.stations = json.load(file)
            print('Stations loaded:', self.stations)
        except:
            print('No stations file found. Using empty list.')
            self.stations = [0] * 10

    def save_stations(self):
        with open(self.filename, 'w') as file:
            json.dump(self.stations, file)
        print('Stations saved:', self.stations)

    def get_stations(self):
        return self.stations
