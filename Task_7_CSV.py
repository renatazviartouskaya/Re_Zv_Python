import csv
import collections


def count_words():
    with open(r"C:\Users\Renata_Zviartouskaya\PycharmProjects\python_SELF_PACED_2024\venv\files\records.txt", 'r') as file:
        text = file.read()

    # split text into words and convert them to lower case
    words = [word.lower() for word in text.split()]

    # count occurrences of each word
    word_count = collections.Counter(words)

    # write counts to CSV
    with open(r"C:\Users\Renata_Zviartouskaya\PycharmProjects\python_SELF_PACED_2024\venv\files\word_count.csv", 'w',
              newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Word", "Count"])
        for word, count in word_count.items():
            writer.writerow([word, count])

def count_characters():
    with open(r"C:\Users\Renata_Zviartouskaya\PycharmProjects\python_SELF_PACED_2024\venv\files\records.txt",
              'r') as file:
        text = file.read()

    # Collect all alphabet characters, disregarding spaces
    letters = [ch for ch in text if ch.isalpha()]
    # Convert to lowercase for counting all occurrences
    all_letters = [ch.lower() for ch in letters]
    # Keep the original case for counting uppercase letters
    uppercase_letters = [ch for ch in letters if ch.isupper()]

    all_letter_counts = collections.Counter(all_letters)
    uppercase_letter_counts = collections.Counter(uppercase_letters)

    # Calculate total number of letters
    total_letters = len(letters)

    # write counts to CSV
    with open(r"C:\Users\Renata_Zviartouskaya\PycharmProjects\python_SELF_PACED_2024\venv\files\letter_counts.csv", 'w', newline='') as csvfile:
        field_names = ['Letter', 'Count_All', 'Count_Uppercase', 'Percentage']
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        writer.writeheader()
        for letter, count in all_letter_counts.items():
            uppercase_count = uppercase_letter_counts[letter.upper()]
            # calculate percentage of each actual letter occurrence, not uppercase presence in all occurrences
            percentage = (count / total_letters) * 100
            writer.writerow({'Letter': letter, 'Count_All': count, 'Count_Uppercase': uppercase_count, 'Percentage': percentage})

if __name__ == "__main__":
    count_characters()
    count_words()

