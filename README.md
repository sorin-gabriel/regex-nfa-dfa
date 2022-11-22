A simple Regex to DFA transformer.

The input is a file containing a single line, with a regular expression in prenex form, for example: `UNION STAR a CONCAT b c`, equivalent to the regular expression `a* U bc`.

Possible regular expressions: `CONCAT`, `UNION`, `STAR`, `PLUS` or literals.

The output is a file with the definition of a DFA that accepts the given regex.
