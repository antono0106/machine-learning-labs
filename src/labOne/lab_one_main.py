import string
import re
import wordcloud as wc
from matplotlib import pyplot as plt


def get_word_dictionary(input_str):
    counts = dict()
    words = input_str.split(' ')

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts


def main():
    content = ''
    try:
        path = input('Input text file path:')

        if not path.endswith('.txt'):
            raise Exception('Invalid file type')
        with open(path) as reader:
            content = reader.read()
            print('content of file:\n' + content)
    except Exception as e:
        print(e)

    content = content.lower()
    content = content.strip()
    content = content.replace('\n', ' ')
    content = re.sub(' +', ' ', content)
    content = content.translate(str.maketrans('', '', string.punctuation))

    print('\ncontent after removing punctuation marks:\n' + content)

    unnecessary_words = [
        'the', 'a', 'to', 'if', 'is', 'it', 'of', 'and', 'or', 'an', 'as', 'i', 'me', 'my',
        'we', 'our', 'ours', 'you', 'your', 'yours', 'he', 'she', 'him', 'his', 'her', 'hers',
        'its', 'they', 'them', 'their', 'what', 'which', 'who', 'whom', 'this', 'that', 'am',
        'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did',
        'but', 'at', 'by', 'with', 'from', 'here', 'when', 'where', 'how', 'all', 'any', 'both',
        'each', 'few', 'more', 'some', 'such', 'no', 'nor', 'too', 'very', 'can', 'will', 'just',
        'on', 'in'
    ]

    content = content.split(' ')
    content = list(filter(lambda word: not unnecessary_words.__contains__(word), content))

    content = ' '.join(content)

    print('\ncontent after removing unnecessary words:\n' + content)

    word_dictionary = get_word_dictionary(content)
    print('\nword dictionary:\n' + dict.__str__(word_dictionary))

    result = wc \
        .WordCloud(width=800, height=800, stopwords=None,
                   background_color='white', min_font_size=10) \
        .generate(list.__str__(list(word_dictionary.keys())).replace('\'', ''))

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(result)
    plt.axis('off')
    plt.tight_layout()

    plt.show()


if __name__ == '__main__':
    main()
