from datasets import Dataset, load_dataset, concatenate_datasets, DatasetDict
import pandas as pd

def load_data(data_path)->pd.DataFrame:
    data = load_dataset(path='json', data_files=data_path, split='train')
    return pd.DataFrame(data)

