def count_word(filename,word):
        print(f'Analyzing the book "{filename}": ')

        try:
            with open(filename) as f:
                contents = f.read()
                count = contents.lower().count(word)
        except FileNotFoundError:
            print(f"Error: file {filename} no found.")
        else:
            print(f'Number of occurences of the word "{word}" : {count}\n')


filenames = [
    'data/sawyer.txt', 
    'data/prejudice.txt', 
    'data/sherlock.txt',
    ]

for filename in filenames:
    count_word(filename,'there')
    count_word(filename,'the ')
    count_word(filename,'sherlock')
