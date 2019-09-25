import tqdm
import seaborn as sns
from pandas import Series

def standardize_word(word: str) -> str:
    '''
    Takes in a word in the form of a string and returns it in a standardized output. 
    '''
    assert type(word) == str, 'input must be a string.'
    
    chars_to_replace = ["'", '/', '|', ',', ';', ':', '.', '?', '$', '%','&','!', '£', '-','_', '(', ')']
    
    for x in chars_to_replace:
        word = word.replace(x, '')
    
    return word.lower()

def count_words(input_list: list) -> dict:
    '''
    Takes in a List of String and returns a dictionary containing the number of occurences for each word. 
    '''
    word_counts = {}
    # Iterate through list of headlines
    for headline in tqdm.tqdm(input_list):
        # Take split headline and count the words in it.
        try:
            for word in headline.split():
                standardized_word = standardize_word(word)
                if standardized_word not in word_counts:
                    word_counts[standardized_word] = 1
                else:
                    word_counts[standardized_word] += 1
        except AttributeError:
            continue
    return word_counts


def bar_words(word_counts: dict, n=10) -> None:
    '''
    Takes in a dictionary of words and returns a barchart of the top n words sorted in descending order. 
    '''

    series = Series(list(word_counts.values()), list(word_counts.keys())).sort_values(ascending=False)

    fig = sns.barplot(x=series[:n].values, y=series[:n].index)

    return fig
