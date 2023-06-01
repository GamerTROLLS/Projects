import random
import string


def keytablegen():
    
    
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    random_key = ''
    random_len = 0
    while random_len != 26:
        random_string = ''.join(random.choices(string.ascii_lowercase, k=26 - random_len))
            
        random_key += random_string
        
        random_key = ''.join(set(random_key))
        random_len = len(random_key)
        print(f"{random_key}---------->{random_len}")
        continue
    
    print('\n\n\n\n')   
    random_key = list(random_key)
    random.shuffle(random_key)
    random_key = ''.join(random_key).upper()
    print(random_key)
    print(random_len)
    
    
    key_map = dict(zip(list(alpha),list(random_key)))
    for i, j in key_map.items():
        print(f"{i}--->{j}")



print(bool(0%2))

initial = 25
final = initial%26
print(final)

print("\n\n\n")


alpha = 'abcdefghijklmnopqrstuvwxyz'
key = 'hilwmkbdpcvazusjgrynqxofte'

keytable = dict(zip(list(alpha),list(key)))


translated = ''
original = input("enter text pls: ")
n = len(original)
temp = 0
index = 0

for i in range(n):
    index += 1
    letter = original[i]
    print(letter)
    initial_pos = alpha.find(letter)
    
    
    if letter == ' ':
        index += 1
        
        translated += ' '
        continue
        
    
    
    if index%2 != 0:
        
        translated += keytable[letter]
        temp = initial_pos
        #print(temp)
        
        
    else:
        final_pos = initial_pos + temp + 1
        final_pos = final_pos % 26
        
        cipher_letter = alpha[final_pos]
        
        translated += cipher_letter
        
        
    
    
print(translated)
    





