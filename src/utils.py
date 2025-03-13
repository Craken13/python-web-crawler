def save_to_file(articles, filename):
    with open(filename, 'a') as file:
        for article in articles:
            file.write(f"{article['title']}\n{article['content']}\n{article['date']}\n\n")

def load_config(config_file):
    import json
    with open(config_file, 'r') as file:
        return json.load(file)