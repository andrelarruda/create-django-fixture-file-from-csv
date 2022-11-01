from tkinter.ttk import Separator
import pandas as pd
import sys
from datetime import datetime

try:
    df = pd.read_csv('./resources/Ocupacao.csv', sep=';', encoding='latin-1')

    result = '['
    for elem in df.values:
        result += ('\n    {')
        result += ('\n        "model": "CBO.cbo",')
        result += ('\n        "fields": {')
        result += ('\n            "is_removed": false,')
        result += ('\n            "created": "{}",'.format(str(datetime.utcnow()).replace(' ', 'T')))
        result += ('\n            "modified": "{}",'.format(str(datetime.utcnow()).replace(' ', 'T')))
        result += ('\n            "code": {},'.format(elem[0]))
        result += ('\n            "description": "{}",'.format(elem[1]))
        result += ('\n            "CBO2002": "{}",'.format(elem[0]))
        result += ('\n            "CBO94": null')
        result += ('\n        }')
        result += ('\n    },')
    result += ('\n]')

    result = ''.join(result.rsplit(',', 1)) # remove the last comma
    
    result_file = open(r"CBOs.json", "w", encoding='utf-8')
    result_file.write(result)
    print('The file was generated successfully.')
except:
    print('Something went wrong.')
    print("Error: " + sys.exc_info()[0])
