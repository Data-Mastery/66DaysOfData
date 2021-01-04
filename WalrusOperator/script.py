### Walrus Operator

# :=

teststring = "Ichbineinlangerstring"

# Variante 1
if len(teststring) > 10:
    print(f'String of length {len(teststring)} is too long! Max = 10')

# Variante 2
length = len(teststring)
if length > 10:
    print(f'String of length {length} is too long! Max = 10')
    
# Variante 3
if (length := len(teststring)) > 10:
    print(f'String of length {length} is too long! Max = 10')