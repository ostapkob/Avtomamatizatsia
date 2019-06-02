import pyperclip
bufer = pyperclip.paste()  # clipboard
lines = bufer.split('\n')
for i in range(len(lines)):
    lines[i] = '*' + lines[i] + '\n'
print(lines)
pyperclip.copy('\r'.join(lines) + '\n---------------------')  # clipboard



