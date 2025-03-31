import re
from collections import Counter


def detect_scripts(text):
    """
    Detects the scripts used in a given text based on Unicode character ranges.

    Args:
        text (str): The input text to analyze.

    Returns:
        str: A comma-separated string of detected script names.
    """
    script_patterns = {
        'devanagari': r'[\u0900-\u097F]',
        'roman': r'[A-Za-z]',
        'kannada': r'[\u0C80-\u0CFF]',
        'malayalam': r'[\u0D00-\u0D7F]',
        'perso-arabic': r'[\u0600-\u06FF]',
        'goykanadi': r'[\uA8E0-\uA8FF]'  # Goykanadi is historically significant but not widely used today.
    }

    detected_scripts = set()

    for script, pattern in script_patterns.items():
        if re.search(pattern, text):
            detected_scripts.add(script)

    return ', '.join(detected_scripts)


def calculate_script_frequencies(dataset_split):
    """
    Calculates the frequency of different scripts in a given dataset split.

    Args:
        dataset_split (dict): A dictionary with a 'script' key containing script labels.

    Returns:
        tuple: A dictionary with script frequency percentages and a dictionary with raw script counts.
    """
    script_counter = Counter(dataset_split['script'])
    total_count = sum(script_counter.values())

    script_frequencies = {script: count / total_count for script, count in script_counter.items()}
    total_frequencies = {script: count for script, count in script_counter.items()}

    return script_frequencies, total_frequencies
