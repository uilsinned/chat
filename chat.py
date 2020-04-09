

def input_file(filename):    
    chat = []
    with open(filename, 'r', encoding='utf-8-sig' ) as f:
        for line in f:
            chat.append(line.strip())        
    return chat

def convert(chat):
    new = []
    name = None
    for line in chat:
        if 'Allen' in line:
            name = 'Allen'
            continue
        elif 'Tom' in line:
            name = 'Tom'
            continue
        if name:
            new.append(name + ': ' + line.strip()) 
    return new
   


def output_file(filename, chat):
    with open(filename, 'w', encoding='utf-8' ) as f:
        for line in chat:
            f.write(line + '\n')
            
def main():
    chat = input_file('input.txt')
    chat = convert(chat)
    output_file('output.txt', chat)

main()










            






        
  