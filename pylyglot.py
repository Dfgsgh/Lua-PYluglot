import argparse

def escape_newlines(s):
    return s.replace('\\', '\\\\').replace('\n', '\\n')

def thechar(s):
    return s.replace('"', '\\"')

parser = argparse.ArgumentParser(description="A tool for creating Python-Lua polyglots")
parser.add_argument("-p", "--python", type=str, required=True, help="Specify the Python code file")
parser.add_argument("-l", "--lua", type=str, required=True, help="Specify the Lua code file")
parser.add_argument("-o", "--output", type=str, required=False, help="Specify the output file name")

args = parser.parse_args()

with open(args.python, "r") as f:
    python = f.read()

with open(args.lua, "r") as f:
    lua = f.read()

if args.output:  
    with open(args.output, "w") as f:
        f.write('''--eval("""
function exec(s) end
{}
--""".replace('\\nfunction exec(s) end\\n{}\\n--', '1+1'))

exec("{}")

'''.format(lua,escape_newlines(lua),thechar(escape_newlines(python))))  
else:
    print('''--eval("""
function exec(s) end
{}
--""".replace('\\nfunction exec(s) end\\n{}\\n--', '1+1'))

exec("{}")

'''.format(lua,escape_newlines(lua),thechar(escape_newlines(python))))



