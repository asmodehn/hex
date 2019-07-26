#!/usr/bin/env python
"""
This is an example of "prompt_toolkit.contrib.regular_languages" which
implements a little calculator.

Type for instance::

    > add 4 4
    > sub 4 4
    > sin 3.14

This example shows how you can define the grammar of a regular language and how
to use variables in this grammar with completers and tokens attached.
"""
import math

from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.contrib.regular_languages.compiler import compile
from prompt_toolkit.contrib.regular_languages.completion import (
    GrammarCompleter,
)
from prompt_toolkit.contrib.regular_languages.lexer import GrammarLexer
from prompt_toolkit.lexers import SimpleLexer
from prompt_toolkit.styles import Style

operators = ['witness', 'assume']


def create_grammar():
    """
    Grammar
    :return:
    """
    return compile(r"""
            (\s*  (?P<operator>[a-z]+)   (\s+   (?P<var>[0-9.]+) )*)
        """)


example_style = Style.from_dict({
    'filter':       '#33aa33 bold',

    'trailing-input': 'bg:#662222 #ffffff',
})


if __name__ == '__main__':
    g = create_grammar()

    lexer = GrammarLexer(g, lexers={
        'operator': SimpleLexer('class:operator'),
        'var': SimpleLexer('class:number'),
    })

    completer = GrammarCompleter(g, {
        'operator': WordCompleter(operators),
    })

    try:
        # REPL loop.
        while True:
            # Read input and parse the result.
            text = prompt('Calculate: ', lexer=lexer, completer=completer,
                          style=example_style)
            m = g.match(text)
            if m:
                v = m.variables()
            else:
                print('Invalid command\n')
                continue

            print(v)
            if v.get('operator'):

                # Execute and print the result.
                print('Result: %s\n' % (v.get('operator')))

    except EOFError:
        pass
