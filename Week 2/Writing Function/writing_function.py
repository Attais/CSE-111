import random

# My stretch goal was adding an adverb function into the program


# The purpose of this program is to perform a very basic Turing test
# by generating simple sentences in random tenses, with singular/plural agreement and adverbs.

def main():
    # Determine if past, present, or future
    tenses = ["past", "present", "future"]
    tense = random.choice(tenses)

    # Create a sentence based on the selected tense
    sentence = make_sentence(tense)
    print(sentence)

# Function to return a random determiner (article)
def get_determiner(is_plural):
    if is_plural:
        return random.choice(["some", "many", "the"])
    else:
        return random.choice(["the", "a", "one"])

# Function to return a random noun and determine if it's singular or plural
def get_noun():
    # List of singular and plural nouns
    singular_nouns = ["dog", "cat", "man", "woman", "child", "teacher", "student", "car", "bicycle", "house"]
    plural_nouns = ["dogs", "cats", "men", "women", "children", "teachers", "students", "cars", "bicycles", "houses"]

    # Randomly choose between singular or plural
    if random.choice([True, False]):
        return random.choice(plural_nouns), True  # True indicates plural
    else:
        return random.choice(singular_nouns), False  # False indicates singular

# Function to return a random verb based on the selected tense and whether the noun is plural or singular
def get_verb(tense, is_plural):
    if tense == "past":
        words = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if is_plural:
            words = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
        else:
            words = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "future":
        words = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]
    return random.choice(words)

# Function to return a random adverb
def get_adverb():
    adverbs = ["quickly", "slowly", "happily", "sadly", "gracefully", "awkwardly", "silently", "loudly", "eagerly", "carefully"]
    return random.choice(adverbs)

# Function to assemble a sentence using a determiner, noun, verb, and adverb
def make_sentence(tense):
    noun, is_plural = get_noun()  # Get noun and its plurality
    determiner = get_determiner(is_plural)  # Get appropriate determiner
    verb = get_verb(tense, is_plural)  # Get appropriate verb based on plurality
    adverb = get_adverb()  # Get a random adverb
    
    # Combine to form a sentence with the adverb before the verb
    sentence = f"{determiner.capitalize()} {noun} {adverb} {verb}."
    return sentence

# Call the main function
main()
