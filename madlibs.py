#!/usr/bin/env python
# coding: utf-8



def main():
    options = {'f':"funny", 'k':"kids"}
    inputs = {'f':["Name male", "Name female", "Occupation 1", "Occupation 2", "Verb 1(ending with 'ed')", "Verb 2", "Place"],'k':["Name 1","Name 2", "Verb(ending with 'ing')"]}

    c = raw_input("Press f for funny, k for kids templates:")

    story_type = options[c]
    print(story_type)

    f = open('/Users/saisrinijasakinala/Desktop/Python/templates.txt','r')
    templates = f.read()

    i = templates.index(story_type)
    helper_string = templates[i:]
    story = helper_string[0:helper_string.find('-')]


    input_users = inputs[c]
    for x in input_users:
        story = story.replace(x,raw_input(x+":"))

    print(story)

if __name__ == "__main__":
    main()


# In[ ]:




