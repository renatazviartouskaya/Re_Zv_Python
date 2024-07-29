import os
from datetime import datetime, timedelta
from Task_4_Function_3 import capitalize_sentences

# Base class for DataRecords
class DataRecord:
    def __init__(self):
        pass

# Class for creation news
class News(DataRecord):
    def create(self):
        text = input("Please enter the news text: ")
        city = input("Please enter the city: ")

        record = f"\nNEWS\nCity: {city}\nText: {text}\nDate: {datetime.now()}\n-----------\n\n"
        return record

# Class for creation Private ad
class PrivateAd(DataRecord):
    def create(self):
        text = input("Please enter the ad text: ")
        expiration_date = input("Please enter the expiration date (YYYY-MM-DD): ")
        expiration_date = datetime.strptime(expiration_date, "%Y-%m-%d")
        days_left = (expiration_date - datetime.now()).days

        record = f"\nPRIVATE AD\nText: {text}\nDays Left: {days_left}\n-----------\n\n"
        return record

# Clacc for creation VIP AD with header, text and creation date
class CustomData(DataRecord):
    def create(self):
        header = input("Please enter the header for your message: ")
        text = input("Please enter the text: ")
        discount = input("Please enter the % of discount: ")
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d %H:%M")
        record = f"\nVIP AD\n{header.upper()}\n{text}\nDiscount for the first ten callers: {discount} %\nDate: {date_time}\n-----------\n\n"
        return record


class NewsFeed:
    def __init__(self, path):
        self.path = path

    def create_record(self, record_type):
        record = record_type.create()
        self._write_record(record)

    def _write_record(self, record):
        with open(os.path.join(self.path, "records.txt"), "a") as f:
            f.write(record)


class FileDataRecord:
    def __init__(self):
        self.default_dir_path = r"C:\Users\Renata_Zviartouskaya\PycharmProjects\python_SELF_PACED_2024\venv\files\New adds"

    def process_files(self):
        file_paths = self._get_file_paths()

        for file_path in file_paths:
            self._process_file(file_path)

    def _get_file_paths(self):
        file_paths = []

        new_adds_files = os.listdir(self.default_dir_path)
        for file in new_adds_files:
            file_paths.append(os.path.join(self.default_dir_path, file))

        if not new_adds_files:
            user_file_path = input("The default directory is empty. Please provide the path to the input file: ")
            file_paths.append(user_file_path)

        return file_paths

    def _process_file(self, file_path):
        try:
            with open(file_path, "r") as file:
                lines = file.readlines()
            records = self._parse_records(lines)
            self._write_records(records)
            self._remove_file(file_path)
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    def _parse_records(self, lines):
        records = []
        for line in lines:
            if line.strip():  # Ignore empty lines
                record = line.lower()
                record = capitalize_sentences(record)  # apply the function
                records.append(record)
        return records

    def _write_records(self, records):
        with open(r"C:\Users\Renata_Zviartouskaya\PycharmProjects\python_SELF_PACED_2024\venv\files\records.txt",
                  "a") as file:
            for record in records:
                file.write(record + "\n")
            file.write("-----------\n\n")

    def _remove_file(self, file_path):
        if os.path.isfile(file_path):
            os.remove(file_path)


def main():
    news_feed = NewsFeed(
        r"C:\Users\Renata_Zviartouskaya\PycharmProjects\python_SELF_PACED_2024\venv\files")  # Define the desired path here.

    print("Please choose the data type:")
    print("1. News")
    print("2. Private Ad")
    print("3. VIP AD")
    print("4. File Records")  # Option for file

    record_type = int(input())

    if record_type == 1:
        news_feed.create_record(News())
    elif record_type == 2:
        news_feed.create_record(PrivateAd())
    elif record_type == 3:
        news_feed.create_record(CustomData())
    elif record_type == 4:
        file_data_record = FileDataRecord()
        file_data_record.process_files()
    else:
        print("Invalid type selected!")


if __name__ == "__main__":
    main()
