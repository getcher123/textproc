# Git Readme.md 

This repository contains a Python script `app.py` that provides a REST API to process text data. The script is based on Flask and uses pymorphy2 and spaCy libraries for natural language processing. 

## Installation

1. Clone the repository
   ```
   git clone https://github.com/username/repository.git
   ```
2. Install required libraries using pip
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Flask server by running `app.py`
   ```
   python app.py
   ```
   By default, the server will start on `http://localhost:5000/`.

2. Initialize the text processing by sending a GET request to `http://localhost:5000/init`.

3. Send a POST request to `http://localhost:5000/textproc` with the following JSON data in the body:
   ```
   {
       "text": "your text to be processed",
       "json_data": "your JSON criteria for text processing"
   }
   ```
   The `json_data` should be in the following format:
   ```
   {
       "key1": "word1, word2, ...",
       "key2": "tag:POS&animacy|Case",
       ...
   }
   ```
   The values can be either a list of words or a tag that specifies the criteria for selecting words.

   Here is an example of a JSON data:
   ```
   {
       "nouns": "кот, собака, животное",
       "verbs": "бежать, прыгать, плавать",
       "adjectives": "быстрый, медленный",
       "pronouns": "tag:POS&animacy|Case"
   }
   ```
   In this example, the script will return all the nouns, verbs, and adjectives in the text, as well as the pronouns that have the specified tag.

4. The server will return a JSON response with the processed text data:
   ```
   {
       "key1": ["selected_word1", "selected_word2", ...],
       "key2": ["selected_word3", "selected_word4", ...],
       ...
   }
   ```
   The response time is also included in the log.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.