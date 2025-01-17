"""
    pygments.lexers.jmespath
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lexers for the JMESPath language

    :copyright: Copyright 2006-2022 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
"""

from pygments.lexer import RegexLexer, bygroups, include
from pygments.token import *

__all__ = ['JMESPathLexer']


class JMESPathLexer(RegexLexer):
    """
    For JMESPath queries.
    """
    name = 'JMESPath'
    url = 'https://jmespath.org'
    filenames = ['*.jp']
    aliases = ['jmespath', 'jp']

    tokens = {
        'string': [
            (r"'(\\(.|\n)|[^'\\])*'", String),
        ],
        'punctuation': [
            (r'(\[\?|[\.\*\[\],:\(\)\{\}\|])', Punctuation),
        ],
        'ws': [
            (r" |\t|\n|\r", Whitespace)
        ],
        'identifier': [
            (r'(")?([A-Za-z][A-Za-z0-9_]*)(")?', bygroups(Punctuation, Name.Variable, Punctuation)),
        ],
        'root': [
            include('ws'),
            include('string'),
            (r'(==|!=|<=|>=|<|>|&&|\|\||!)', Operator),
            include('punctuation'),
            (r'@', Name.Variable.Global),
            (r'(&?[A-Za-z][A-Za-z0-9_]*)(\()', bygroups(Name.Function, Punctuation)),
            include('identifier'),
            (r'-?\d+', Number),
            (r'`', Literal, 'literal'),
        ],
        'literal': [
            include('ws'),
            include('string'),
            include('punctuation'),
            (r'(false|true|null)\b', Keyword.Constant),
            include('identifier'),
            (r'-?\d+\.?\d*([eE][-+]\d+)?', Number),
            (r'\\`', Literal),
            (r'`', Literal, '#pop'),
        ]
    }
