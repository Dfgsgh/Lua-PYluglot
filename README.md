# Lua–Python Polyglot Generator

This tool lets you generate a **polyglot script** that runs valid code in both **Python** and **Lua**. You can feed it separate `.py` and `.lua` files, and it will produce a single script that behaves correctly in either interpreter.

## ✨ Features

- Generates a script that runs as valid **Python** and valid **Lua**
- Lua runs natively
- Python string-evals Lua as a multiline string
- Automatically escapes characters and newlines
- Optional output file or prints to stdout

## 🛠 Usage

```bash
python polyglotgen.py -p yourscript.py -l yourscript.lua -o output.lua
```

-p / --python: Path to your Python file <br>
-l / --lua: Path to your Lua file<br>
-o / --output: (Optional) Output polyglot file. If omitted, output is printed.

## 📄 How It Works

Lua sees a normal script, including a fake exec function and some hidden Lua code inside a Python multiline string.
Python treats everything in the triple-quoted string as a string and uses .replace() to simulate the Lua part, before exec-ing the real Python code.

