import json

settings_json = json.dumps([
    {'type': 'title',
     'title': 'Common settings'},

    # {'type': 'bool',
    #  'title': 'A boolean setting',
    #  'desc': 'Boolean description text',
    #  'section': 'example',
    #  'key': 'boolexample'},

    {'type': 'numeric',
     'title': 'Font size',
     'desc': 'Enter the font size',
     'section': 'Common settings',
     'key': 'fontsizesettings'},

    {'type': 'options',
     'title': 'Theme',
     'desc': 'Choose the theme of the app',
     'section': 'Common settings',
     'key': 'themesettings',
     'options': ['Light', 'Dark']},

    # {'type': 'string',
    #  'title': 'A string setting',
    #  'desc': 'String description text',
    #  'section': 'example',
    #  'key': 'stringexample'},

    {'type': 'path',
     'title': 'Path',
     'desc': 'Choose where to store your entries',
     'section': 'Common settings',
     'key': 'pathsettings'},

    {'type': 'options',
     'title': 'Language',
     'desc': 'Choose the language',
     'section': 'Common settings',
     'key': 'languagesettings',
     'options': ['English', 'Русский']}])