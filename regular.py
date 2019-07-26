"""
A potentially eternal configurable & observable runtime.
We interpret here regular logic as a filter syntax for logging ->
. / and / concat : filter combination (semantics : boolean and relation)
Exists : logged something at least once
T :
"""

import structlog
import logging
import pyparsing


# A RUNTIME (AKA interpreter)

# from pyparsing import Word, alphas
# greet = Word( alphas ) + "," + Word( alphas ) + "!"
# hello = "Hello, World!"
# print(hello, "->", greet.parseString( hello ))



#!/usr/bin/env python
from prompt_toolkit.widgets import TextArea

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
from prompt_toolkit.document import Document
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.contrib.regular_languages.compiler import compile
from prompt_toolkit.contrib.regular_languages.completion import (
    GrammarCompleter,
)
from prompt_toolkit.contrib.regular_languages.lexer import GrammarLexer
from prompt_toolkit.lexers import SimpleLexer
from prompt_toolkit.styles import Style
from prompt_toolkit.application import Application
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.key_binding import KeyBindings

operators1 = ['add', 'sub', 'div', 'mul']
operators2 = ['cos', 'sin']


def create_grammar():
    return compile(r"""
        (\s*  (?P<operator1>[a-z]+)   \s+   (?P<var1>[0-9.]+)   \s+   (?P<var2>[0-9.]+)   \s*) |
        (\s*  (?P<operator2>[a-z]+)   \s+   (?P<var1>[0-9.]+)   \s*)
    """)


example_style = Style.from_dict({
    'operator':       '#33aa33 bold',
    'number':         '#ff0000 bold',

    'trailing-input': 'bg:#662222 #ffffff',
})


g = create_grammar()

lexer = GrammarLexer(g, lexers={
    'operator1': SimpleLexer('class:operator'),
    'operator2': SimpleLexer('class:operator'),
    'var1': SimpleLexer('class:number'),
    'var2': SimpleLexer('class:number'),
})

completer = GrammarCompleter(g, {
    'operator1': WordCompleter(operators1),
    'operator2': WordCompleter(operators2),
})


#TODO : this should probably be a functor/lens (two way communication, see ML applications...)
def dummy_inner_loop(inner_in):
    """A dummy pure function as scaffold"""
    return f"inner out: {inner_in}"

# A REPL (AKA interactive differential configuration)


kb = KeyBindings()


@kb.add('c-c', eager=True)
@kb.add('c-q', eager=True)
def exit_(event):
    """
    Pressing Ctrl-Q will exit the user interface.

    Setting a return value means: quit the event loop that drives the user
    interface and return this value from the `Application.run()` call.
    """
    event.app.exit()


# Now we add an event handler that captures change events to the buffer on the
# left. If the text changes over there, we'll update the buffer on the right.

right_buffer = Buffer()  # Output buffer.


input_field = TextArea(
            height=1, prompt='>>> ', style='class:input-field', multiline=False,
            wrap_lines=False)

# Attach accept handler to the input field. We do this by assigning the
# handler to the `TextArea` that we created earlier. it is also possible to
# pass it to the constructor of `TextArea`.
# NOTE: It's better to assign an `accept_handler`, rather then adding a
#       custom ENTER key binding. This will automatically reset the input
#       field and add the strings to the history.
def accept(buff):
    # Evaluate "calculator" expression.
    try:
        output = '\n\nIn:  {}\nOut: {}'.format(
            input_field.text,
            eval(input_field.text))  # Don't do 'eval' in real code!
    except BaseException as e:
        output = '\n\n{}'.format(e)
    new_text = right_buffer.text + output

    # Add text to output buffer.
    right_buffer.document = Document(
        text=new_text, cursor_position=len(new_text))


input_field.accept_handler = accept


def application():

    root_container = VSplit([
        # One window that holds the BufferControl with the default buffer on
        # the left.
        input_field,

        # A vertical line in the middle. We explicitly specify the width, to
        # make sure that the layout engine will not try to divide the whole
        # width by three for all these windows. The window will simply fill its
        # content by repeating this character.
        Window(width=1, char='|'),

        # Display the text 'Hello world' on the right.
        Window(content=BufferControl(buffer=right_buffer)),
    ])

    layout = Layout(root_container)

    # TODO : different layout if input/output not a terminal...
    application = Application(
        key_bindings=kb,
        layout=layout,
        full_screen=True,
    )
    return application


async def main():

    result = await application().run_async()
    print(result)


if __name__ == '__main__':

    # handle arguments. one arg is config file or pipe...

    print(application().run())

    # TODO : async (careful with key bindings and I/O...)
    #import asyncio  # TODO : trio ?
    #asyncio.get_event_loop().run_until_complete(main())

