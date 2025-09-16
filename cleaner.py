import re

def remove_chat_metadata(chat_export_file):
    ## If you export a Whatsapp chat as the training data, the pattern is as follows.
    date_time = r"(\d+\/\d+\/\d+,\s\d+:\d+)"  # e.g. "9/16/22, 06:34"
    dash_whitespace = r"\s-\s"  # " - "
    username = r"([\w\s]+)"  # e.g. "Martin"
    metadata_end = r":\s"  # ": "
    pattern = date_time + dash_whitespace + username + metadata_end
    try:
        with open(chat_export_file, "r", encoding="utf-8") as corpus_file:
            content = corpus_file.read()
    except FileNotFoundError:
        print("Error: The file was not found.")
    except UnicodeDecodeError:
        print("Error: Unable to decode the file with UTF-8 encoding.")
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))

def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]
    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))

# if __name__ == "__main__":
#     message_corpus = remove_chat_metadata("training_data.txt")
#     cleaned_corpus = remove_non_message_text(message_corpus)
#     print(cleaned_corpus)

def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus
