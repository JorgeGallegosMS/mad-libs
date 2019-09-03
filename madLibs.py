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

test()
