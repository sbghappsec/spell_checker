from __future__ import print_function
import argparse
import enchant

#handle CLI argument
parser = argparse.ArgumentParser(description = 'Spellcheck the given text file.')
parser.add_argument('--file', type=str, help = 'path to file', required = True)
args = parser.parse_args()

#import dictionary
d = enchant.Dict('en_US')

def getSuggestions(word):
    suggestions = d.suggest(word)
    if len(suggestions) == 0:
        return 'no suggestions'
    suggestions = ', '.join(suggestions)
    return suggestions

def main():
    try:
        with open(args.file, 'r') as text_file:
            error_count = 0
            errors_suggestions = {}
            f = text_file.read()
            print("Beginning spellcheck...\n")

            for word in f.split(): 
                stripped_word = word.strip(":;-,!_?)(&*$#)./'\"")
                if stripped_word != '' and not d.check(stripped_word):
                    error_count += 1
                    errors_suggestions[stripped_word] = getSuggestions(stripped_word)

            print('Spellcheck Complete. Your document had {} error(s).\n'.format(error_count))
            for key in errors_suggestions:
                print("You misspelled {}. Here are some suggestions: {}.".format(key, errors_suggestions[key]))
                
    except FileNotFoundError:
        print("The file could not be found.")

if __name__ == '__main__':
    main()