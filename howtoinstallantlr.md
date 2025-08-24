# How to Install ANTLR

1. Download the [official ANTLR website](https://www.antlr.org/download.html).
The correct file is the "Complete ANTLR x.x.x Java binaries jar"
2. Put it in the directory of your choice. I will call it "antlr".
On the directory where the file is do "java -jar FILENAME"
If you get an output saying "ANTLR Parser Generator" ya good to go
3. Install the pip library for ANTLR:

```sh
pip install antlr4-python3-runtime
```

4. To make things easier, create an alias for the java command.
To make it permanent, add this line to your `.bashrc`

```
alias toniAntlr=' java -jar FULLPATH/antlr-x.x.x-complete.jar'
```

5. Now, on the directory where the grammar is run, generate the Parser:

```
toniAntlr -Dlanguage=Python3 toniParser.g4 toniLexer.g4
```

## Source

<https://yetanotherprogrammingblog.medium.com/antlr-with-python-974c756bdb1b>
