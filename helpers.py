from prettytable import PrettyTable
import ollama
import csv
import os

itinerary = []

def read_csv(f):
    file_path = "/Users/alexp/Documents/code/python_dev/csv/"
    if os.path.exists(file_path + f):
        f = open(file_path + f, 'r')
        data = []
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            data.append(row)
        f.close()
        return data
    else:
        print(f"File not found:{f}!")
        exit()


def display_table(data):
#create a better output for the itinerary
    table = PrettyTable()

    if data:
        table.field_names = data[0].keys() #set column headers
        for row_dict in data:
            table.add_row(row_dict.values()) #set rows
    print(table)

def get_llm_response(prompt):
    model ='gemma2:2b'
    print("Generating LLM Response ....")
    response = ollama.generate(model, prompt)
    return response["response"]

def read_txt(f):

    file_path = "/Users/alexp/Documents/code/python_dev/journals/"
    if os.path.exists(file_path + f):
        with open(file_path + f, "r") as file:
            data = file.read()
        return data
    else:
        print(f"File not found: {f}!")
        exit()

if __name__ == "__main__":
    print("Importing the >> helpers module")
