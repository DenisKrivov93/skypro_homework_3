# -*- coding: utf-8 -*-
import csv


def read_transactions_from_csv(file_path):
    """
    Принимает путь до csv-файла и возвращает список словарей с данными о финансовых транзакциях.
    """
    with open(file_path) as file:
        reader = csv.DictReader(file)
        list_dict = []
        for row in reader:
            list_dict.append(row)

        return list_dict
