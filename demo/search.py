#!/usr/bin/env python
from __future__ import print_function
from termcolor import colored

# a hack so you can run it 'python demo/search.py'
import sys
sys.path.append('.')
sys.path.append('..')

try:
    get_input = raw_input
except NameError:
    get_input = input

#user_api_key = get_input("Please enter an API key if you have one (Return for none):")
#if not user_api_key: user_api_key = None
user_api_key = None

import stackexchange
so = stackexchange.Site(stackexchange.StackOverflow, app_key=user_api_key, impose_throttling=True)

if __name__ == '__main__':
    #an = Question()
    #dir(an)


    term = get_input('Please provide a search term:')
    print('Searching for %s...' % term,)
    sys.stdout.flush()

    qs = so.search(intitle=term)
    #print (qs)

    print('\r--- questions with "%s" in title ---' % (term))
    
    l1 = sorted(qs, key=lambda question: question.answer_count, reverse=False)
    l2 = sorted(l1, key=lambda question: question.is_answered, reverse=False)
    for q in l2:
        #print ('%s' % (q.__dict__))
        print('Num answer: %d, Answer: %s' % (q.answer_count, q.is_answered))
        print(colored('%s' % q.title, 'green'))
        print('%s' % (q.url))
        print('---------------------------------------------------------')


