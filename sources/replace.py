import re

# String Replacer for Text


def replace(filename, oldText, newText, flags=0):
    with open(filename, "r+") as file:
        fileContents = file.read()
        textPattern = re.compile(re.escape(oldText), flags)
        fileContents = textPattern.sub(newText, fileContents)
        file.seek(0)
        file.truncate()
        file.write(fileContents)
    # Add the type test and the approximation
