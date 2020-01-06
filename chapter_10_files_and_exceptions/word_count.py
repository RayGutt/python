def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
#        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = [
    'data/alice.txt',
    'data/siddhartha.txt',
    'data/iddhartha.txt',
    'data/moby_dick.txt',
    'data/little_women.txt',
    ]

for filename in filenames:
    count_words(filename)
