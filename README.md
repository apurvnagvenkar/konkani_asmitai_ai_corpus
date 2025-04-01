# konkani_asmitai_ai_corpus

An Open-Source Initiative to Build the First LLM for Konkani!
## Dataset Overview  
Konkani is a rich and diverse language spoken across India's western coast. A unique feature of Konkani is its **multiscript nature**, with speakers using different scripts based on geography, community, and historical influences. Despite being an **official language of India**, Konkani has very **limited digital presence**, making it challenging to build AI models for the language.  
This dataset is an **open-source effort** to create a **high-quality, multiscript corpus** for Konkani. It includes **data in multiple scripts** to ensure inclusivity and better model performance across different Konkani-speaking communities.  


Konkani is written in following scripts:  
- **Devanagari** – The official script for Konkani in Goa, widely used in literature.  
- **Roman (Romi Konkani)** – Used in media, Tiatr, and religious writings.  
- **Kannada** – Predominantly used in Karnataka by Konkani speakers.  
- **Malayalam (Obsolete)**  – Historically used by Konkani speakers in Kerala.  
- **Perso-Arabic (Obsolete)** – Used by Konkani-speaking Muslims, influenced by Urdu and Arabic vocabulary.  



## Dataset Details

### Dataset Description

<!-- Provide a longer summary of what this dataset is. -->



- **Curated by:** Apurva Nagvenkar
<!-- - **Funded by [optional]:** [More Information Needed]
- **Shared by [optional]:** [More Information Needed]
- **Language(s) (NLP):** [More Information Needed]
- **License:** Apache License 2.0 -->

### Dataset Sources
<!-- Provide the basic links for the dataset. -->

- **Repository:** https://github.com/apurvnagvenkar/konkani_asmitai_ai_corpus
- **Data Location** https://dumps.wikimedia.org/gomwiki/latest/gomwiki-latest-pages-articles.xml.bz2


## Dataset Statistics

### Dataset Split Counts
| Split       | Count |
|------------|-------|
| Train      | 2992  |
| Validation | 374   |
| Test       | 375   |
| **Total**  | **3741** |


### Train Set Script Frequencies
| Script Combination                                      | Count | Percentage |
|--------------------------------------------------------|------|------------|
| Devanagari                                           | 1241 | 41.48%     |
| Devanagari, Roman                                      | 978  | 32.69%     |
| Roman                                                 | 624  | 20.86%     |
| Roman, Kannada                                       | 100  | 3.34%      |
| Kannada                                              | 32   | 1.07%      |
| Devanagari, Roman, Kannada                           | 10   | 0.33%      |
| Malayalam, Devanagari, Roman, Kannada                | 4    | 0.13%      |
| Malayalam, Roman, Perso-Arabic, Kannada, Devanagari  | 1    | 0.03%      |
| Devanagari, Malayalam                                | 1    | 0.03%      |
| Devanagari, Kannada                                  | 1    | 0.03%      |

### Validation Set Script Frequencies
| Script Combination      | Count | Percentage |
|------------------------|------|------------|
| Devanagari           | 150  | 40.11%     |
| Devanagari, Roman   | 130  | 34.76%     |
| Roman               | 78   | 20.86%     |
| Roman, Kannada      | 13   | 3.48%      |
| Kannada            | 3    | 0.80%      |

### Test Set Script Frequencies
| Script Combination                                   | Count | Percentage |
|-----------------------------------------------------|------|------------|
| Devanagari                                        | 161  | 42.93%     |
| Devanagari, Roman                                | 118  | 31.47%     |
| Roman                                           | 83   | 22.13%     |
| Roman, Kannada                                  | 9    | 2.40%      |
| Kannada                                         | 2    | 0.53%      |
| Devanagari, Roman, Kannada                      | 1    | 0.27%      |
| Malayalam, Devanagari, Roman, Kannada           | 1    | 0.27%      |


## Running script on local sysem
### Virtual env creation
```python
virtualenv venv -p python3
source venv/bin/activate  
pip install -r requirements.txt
```
### Python Script
```python
python wiki_data_parsing.py
```
## Download & Usage

The dataset is freely available for research and development. Check out the Hugging Face repo here: https://huggingface.co/datasets/anag007/asmitai_wiki_konkani_dataset
```python
from datasets import load_dataset

dataset = load_dataset("anag007/asmitai_wiki_konkani_dataset")
```

## How to Contribute  
If you're a **researcher, student, or language enthusiast**, we invite you to:  
- **Contribute Data** – Help expand the corpus by sharing openly available Konkani texts.  
- **Improve Annotations** – Assist in refining dataset quality.  
- **Collaborate on Models** – Use this dataset to build **state-of-the-art** Konkani AI models!  

- For contributions, reach out to: apurv.research@gmail.com

## Acknowledgments

A special thanks to everyone supporting Konkani's digital future! Let’s work together to preserve, digitize, and advance Konkani AI.

Join the Movement! Let’s build a state-of-the-art Konkani LLM together!