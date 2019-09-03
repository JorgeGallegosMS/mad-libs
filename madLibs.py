# Story from: http://www.redkid.net/cgi-bin/madlibs/videogames.pl
"""I love to {} {} video games. I can play them day and
{}! My mom and {} are not too happy with my
{} so much time in front of the television {}.
Although Dad believes that these {} games help children
develop hand-{} coordination and improve their
learning {}, he also seems to think they have {}
side effects on one's {}. Both of my {}
think this is due to a {} use of violence in the majority
of the {}. Finally, we all arrived at a {}
compromise: After dinner I can play {} hours of video games,
provided I help clear the {} and wash the {}."""

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def test():
    word = user_input("Random word: ")
    print(word)

# noun1 = user_input("Noun: ")
# noun2 = user_input("Noun: ")
# noun3 = user_input("Noun: ")
# noun4 = user_input("Noun: ")
# noun5 = user_input("Part of Body: ")
# noun6 = user_input("Part of Body: ")
# noun7 = user_input("Plural Noun: ")
# noun8 = user_input("Plural Noun: ")
# noun9 = user_input("Plural Noun: ")
# noun10 = user_input("Plural Noun: ")
#
# adj1 = user_input("Adjective: ")
# adj2 = user_input("Adjective: ")
# adj3 = user_input("Adjective: ")
# adj4 = user_input("Adjective: ")

nouns = [user_input("Noun: ") for noun in range(4)]
plural_nouns = [user_input("Plural Noun: ") for pnoun in range(4)]
adjectives = [user_input("Adjective: ") for adj in range(4)]

verb1 = user_input("Verb: ")
verb2 = user_input("Verb ending in 'ing': ")

body1 = user_input("Part of Body: ")
body2 = user_input("Part of Body: ")

num = user_input("Number: ")
