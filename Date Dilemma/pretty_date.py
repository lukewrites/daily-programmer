"""
Yesterday, Devon the developer made an awesome webform, which the sales team would use to record the results from today's big new marketing campaign, but now he realised he forgot to add a validator to the "delivery_date" field! He proceeds to open the generated spreadsheet but, as he expected, the dates are all but normalized... Some of them use M D Y and others Y M D, and even arbitrary separators are used! Can you help him parse all the messy text into properly ISO 8601 (YYYY-MM-DD) formatted dates before beer o'clock?
Assume only dates starting with 4 digits use Y M D, and others use M D Y.

Sample Input

2/13/15
1-31-10
5 10 2015
2012 3 17
2001-01-01
2008/01/07

Sample Output

2015-02-13
2010-01-31
2015-05-10
2012-03-17
2001-01-01
2008-01-07

"""

import datetime

def pretty_date(input):
    remap = {
      ord('/'): ' ',
      ord('-'): ' ',
    }
    cleaned_input = input.translate(remap).split()
    cleaned_input = [int(cleaned_input[0]), int(cleaned_input[1]), int(cleaned_input[2])]
    if cleaned_input[0] > 99:
        return datetime.date.isoformat(datetime.date(cleaned_input[0],
                                                     cleaned_input[1],
                                                     cleaned_input[2]))
    else:
        if cleaned_input[2] < 2000:
            cleaned_input[2] += 2000
        return datetime.date.isoformat(datetime.date(cleaned_input[2],
                                                     cleaned_input[0],
                                                     cleaned_input[1]))
