import csv
from data.data_source import DataSource

class CSVAdapter(DataSource):
    def __init__(self, filepath):
        self.filepath = filepath

    def get_data(self):
        with open(self.filepath, newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
