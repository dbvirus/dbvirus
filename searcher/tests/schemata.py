"""
This file defines the structure of the JSON
responses expected by the Searcher module.

They are generated using the JSON Schema Tool,
available here https://jsonschema.net/
"""

# pylint: skip-file
SEARCH_RESULT_SCHEMA = {
    "definitions": {},
    "$schema": "http://json-schema.org/draft-07/schema#",
    "$id": "http://example.com/root.json",
    "type": "object",
    "title": "The Root Schema",
    "required": ["header", "esearchresult"],
    "properties": {
        "header": {
            "$id": "#/properties/header",
            "type": "object",
            "title": "The Header Schema",
            "required": ["type", "version"],
            "properties": {
                "type": {
                    "$id": "#/properties/header/properties/type",
                    "type": "string",
                    "title": "The Type Schema",
                    "default": "",
                    "examples": ["esearch"],
                    "pattern": "^(.*)$",
                },
                "version": {
                    "$id": "#/properties/header/properties/version",
                    "type": "string",
                    "title": "The Version Schema",
                    "default": "",
                    "examples": ["0.3"],
                    "pattern": "^(.*)$",
                },
            },
        },
        "esearchresult": {
            "$id": "#/properties/esearchresult",
            "type": "object",
            "title": "The Esearchresult Schema",
            "required": [
                "count",
                "retmax",
                "retstart",
                "idlist",
                "translationset",
                "translationstack",
                "querytranslation",
            ],
            "properties": {
                "count": {
                    "$id": "#/properties/esearchresult/properties/count",
                    "type": "string",
                    "title": "The Count Schema",
                    "default": "",
                    "examples": ["2211223"],
                    "pattern": "^(.*)$",
                },
                "retmax": {
                    "$id": "#/properties/esearchresult/properties/retmax",
                    "type": "string",
                    "title": "The Retmax Schema",
                    "default": "",
                    "examples": ["3"],
                    "pattern": "^(.*)$",
                },
                "retstart": {
                    "$id": "#/properties/esearchresult/properties/retstart",
                    "type": "string",
                    "title": "The Retstart Schema",
                    "default": "",
                    "examples": ["0"],
                    "pattern": "^(.*)$",
                },
                "idlist": {
                    "$id": "#/properties/esearchresult/properties/idlist",
                    "type": "array",
                    "title": "The Idlist Schema",
                    "items": {
                        "$id": "#/properties/esearchresult/properties/idlist/items",
                        "type": "string",
                        "title": "The Items Schema",
                        "default": "",
                        "examples": ["8818505", "8818504", "8818503"],
                        "pattern": "^(.*)$",
                    },
                },
                "translationset": {
                    "$id": "#/properties/esearchresult/properties/translationset",
                    "type": "array",
                    "title": "The Translationset Schema",
                    "items": {
                        "$id": "#/properties/esearchresult/properties/translationset/items",
                        "type": "object",
                        "title": "The Items Schema",
                        "required": ["from", "to"],
                        "properties": {
                            "from": {
                                "$id": "#/properties/esearchresult/properties/translationset/items/properties/from",
                                "type": "string",
                                "title": "The From Schema",
                                "default": "",
                                "examples": ["Human"],
                                "pattern": "^(.*)$",
                            },
                            "to": {
                                "$id": "#/properties/esearchresult/properties/translationset/items/properties/to",
                                "type": "string",
                                "title": "The To Schema",
                                "default": "",
                                "examples": [
                                    "'Homo sapiens' [Organism] OR Human[All Fields]"
                                ],
                                "pattern": "^(.*)$",
                            },
                        },
                    },
                },
                "translationstack": {
                    "$id": "#/properties/esearchresult/properties/translationstack",
                    "type": "array",
                    "title": "The Translationstack Schema",
                },
                "querytranslation": {
                    "$id": "#/properties/esearchresult/properties/querytranslation",
                    "type": "string",
                    "title": "The Querytranslation Schema",
                    "default": "",
                    "examples": ["'Homo sapiens'[Organism] OR Human[All Fields]"],
                    "pattern": "^(.*)$",
                },
            },
        },
    },
}
