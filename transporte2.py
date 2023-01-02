
# ---------------------------

# ---------------------------
file = r'settings\blackboard\blackboard.txt'

lines = []
with open(file, encoding='utf-8') as f:
    for line in f:
        lines.append(line)

print(lines)



keys_type = input('Desea generar claves automaticas? (S/N): ')

if keys_type == 's' or keys_type == 'S':
    keys_type = 0
elif keys_type == 'n' or keys_type == 'N':
    keys_type = None

