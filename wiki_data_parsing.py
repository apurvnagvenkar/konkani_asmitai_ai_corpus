import os
import requests
import subprocess
import shutil
from sklearn.model_selection import train_test_split
from datasets import Dataset, DatasetDict
from utils import detect_scripts, calculate_script_frequencies
from huggingface_hub import HfApi, HfFolder

# Step 1: Define URLs and Paths
dump_url = 'https://dumps.wikimedia.org/gomwiki/latest/gomwiki-latest-pages-articles.xml.bz2'
dump_file = 'data/gomwiki-latest-pages-articles.xml.bz2'
extracted_dir = 'data/extracted'
repo_name = 'anag007/asmitai_wiki_konkani_dataset'


def download_dump(url, filename):
    """
    Downloads a Wikipedia dump file from the specified URL.

    Args:
        url (str): The URL of the Wikipedia dump.
        filename (str): The destination filename for the downloaded dump.

    Returns:
        None
    """
    print(f"Downloading {url}...")
    response = requests.get(url, stream=True)
    with open(filename, 'wb') as f:
        shutil.copyfileobj(response.raw, f)
    print(f"Downloaded {filename}")


def extract_text(dump_file, output_dir):
    """
    Extracts text from a Wikipedia dump using WikiExtractor.

    Args:
        dump_file (str): The Wikipedia dump file to process.
        output_dir (str): The directory where extracted text will be stored.

    Returns:
        None
    """
    print(f"Extracting text from {dump_file}...")
    subprocess.run(['wikiextractor', '--json', '-o', output_dir, dump_file])
    print(f"Extraction completed. Extracted files are in {output_dir}")


def load_extracted_data(output_dir):
    """
    Loads extracted Wikipedia data from the specified directory.

    Args:
        output_dir (str): Directory containing extracted JSON files.

    Returns:
        list: A list of dictionaries representing extracted articles.
    """
    print(f"Loading extracted data from {output_dir}...")
    data = []
    for root, _, files in os.walk(output_dir):
        for file in files:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                for line in f:
                    datapoint = eval(line)
                    if len(datapoint["text"].split()) > 10:
                        datapoint["script"] = detect_scripts(datapoint["text"])
                        data.append(datapoint)
    print(f"Loaded {len(data)} articles.")
    return data


def split_data(data, train_size=0.8, val_size=0.1, test_size=0.1, random_state=42):
    """
    Splits the dataset into train, validation, and test sets.

    Args:
        data (list): The dataset to split.
        train_size (float): Proportion of training data.
        val_size (float): Proportion of validation data.
        test_size (float): Proportion of test data.
        random_state (int): Seed for reproducibility.

    Returns:
        tuple: Train, validation, and test datasets.
    """
    train_data, temp_data = train_test_split(data, train_size=train_size, random_state=random_state)
    val_data, test_data = train_test_split(temp_data, test_size=test_size / (test_size + val_size),
                                           random_state=random_state)
    print(f"Data split as follows: Train: {len(train_data)}, Validation: {len(val_data)}, Test: {len(test_data)}")
    return train_data, val_data, test_data


def create_dataset_dict(train_data, val_data, test_data):
    """
    Creates a Hugging Face DatasetDict from train, validation, and test datasets.

    Args:
        train_data (list): Training data.
        val_data (list): Validation data.
        test_data (list): Test data.

    Returns:
        DatasetDict: Hugging Face dataset dictionary.
    """
    print(f"Creating DatasetDict...")
    dataset_dict = DatasetDict({
        'train': Dataset.from_list(train_data),
        'validation': Dataset.from_list(val_data),
        'test': Dataset.from_list(test_data)
    })
    print(f"DatasetDict created with splits: {dataset_dict}")
    return dataset_dict


def upload_to_huggingface(dataset_dict, repo_name):
    """
    Uploads the dataset to the Hugging Face Hub.

    Args:
        dataset_dict (DatasetDict): The dataset to upload.
        repo_name (str): The Hugging Face repository name.

    Returns:
        None
    """
    print(f"Uploading dataset to Hugging Face Hub under {repo_name}...")
    dataset_dict.push_to_hub(repo_name)
    print(f"Dataset uploaded successfully.")


if __name__ == "__main__":
    if not os.path.exists(dump_file):
        download_dump(dump_url, dump_file)
    else:
        print(f"{dump_file} already exists. Skipping download.")

    if not os.path.exists(extracted_dir):
        os.makedirs(extracted_dir)
        extract_text(dump_file, extracted_dir)
    else:
        print(f"{extracted_dir} already exists. Skipping extraction.")

    # Prepare Data
    data = load_extracted_data(extracted_dir)
    train_data, val_data, test_data = split_data(data)
    dataset_dict = create_dataset_dict(train_data, val_data, test_data)
    # Upload to huggingface
    upload_to_huggingface(dataset_dict, repo_name)


    train_frequencies, train_count = calculate_script_frequencies(dataset_dict['train'])
    validation_frequencies, val_count = calculate_script_frequencies(dataset_dict['validation'])
    test_frequencies, test_count = calculate_script_frequencies(dataset_dict['test'])

    print("Train Script Frequencies:")
    for script, freq in train_frequencies.items():
        print(f"{script}: {freq:.2%} : {train_count[script]}")

    print("\nValidation Script Frequencies:")
    for script, freq in validation_frequencies.items():
        print(f"{script}: {freq:.2%} : {val_count[script]}")

    print("\nTest Script Frequencies:")
    for script, freq in test_frequencies.items():
        print(f"{script}: {freq:.2%} : {test_count[script]}")

