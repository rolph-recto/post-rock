#!/usr/bin/env python
# post rock album name generator
# Rolph Recto

from random import random, choice
from functools import partial

adjectives = [
    "Starry",
    "Long",
    "Eternal",
    "Divine",
]

# these are more abstract nouns
anouns = [
    "Birth",
    "Death",
    "Ascension",
    "Crescent",
    "Infinite",
    "Divide",
    "Distintegration",
    "Heat",
]

# these are more concrete nouns
cnouns = [
    "Moon",
    "Sky",
    "Sun",
    "Land",
    "Ocean",
    "Mountain",
    "Universe",
    "Phoenix",
]

# generate a name
# there are three schemas:
# - the [adj] [anoun|cnoun]
# - the [anoun] [anoun] of the [cnoun]
# - the [adj] [anoun] of the [cnoun]
def generate_name():
    def get_word_list(name):
        if name == "adj":
            return adjectives
        elif name == "anoun":
            return anouns
        elif name == "cnoun":
            return cnouns
        else:
            return []

    def apply_word(scheme, application):
        if type(application) == list:
            word_list = reduce(lambda acc, name: acc+get_word_list(name), application, [])
        else:
            word_list = get_word_list(application)

        return partial(scheme, choice(word_list))

    schemes = [
        ("The {0} {1}", ["adj", ["anoun", "cnoun"]]),
        ("The {0} {1} of the {2}", ["adj", "anoun", "cnoun"])
    ]

    # pick a scheme
    scheme, applications = choice(schemes)

    # apply word to scheme
    name = reduce(apply_word, applications, partial(scheme.format))

    return name()

if __name__ == "__main__":
    print generate_name()
    

