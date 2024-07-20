import pandas as pd


def read_transactions_from_xlsx(file_path):
    """
    Принимает путь до xlsx-файла и возвращает список словарей с данными о финансовых транзакциях.
    """
    excel_df = pd.read_excel(file_path)
    return excel_df
