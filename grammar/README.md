# TONI Grammar

In the heart of this project sits ANTLR, a powerful
parser generator, which is able to create the abstract
syntax tree (AST) need to process the given regex and
apply Thompson's algorithm to it.

To generate the lexer and corresponding parser, as well
as a listener, ANTLR needs a grammar. This is where it is
defined.

We credit [this](https://github.com/antlr/grammars-v4/blob/master/xsd-regex/regexParser.g4)
very useful grammar, which we adapted for our needs.
