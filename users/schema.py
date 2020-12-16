# https://json-schema.org/understanding-json-schema/

LANGUAGE_SCHEMA = {
    'schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'array',
    "uniqueItems": True,
    'items': [
        {'type': 'object',
         'properties': {
                 'name': {'type': 'string'},
                 'category': {
                     'type': 'string',
                     "enum": ["back_end", "front_end", "devops", "mobile", "database"]},
             'score': {'type': 'number',
                       "minimum": 0,
                       "exclusiveMaximum": 11},
         }, "required": ["name", "category", "score"],
         },
    ],
}
