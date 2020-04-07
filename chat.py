

def input_file(filename):    
    chat = []
    with open(filename, 'r', encoding='utf-8-sig' ) as f:
        for line in f:
            if 'Allen' in line:
                name = 'Allen'
                continue
            elif 'Tom' in line:
                name = 'Tom'
                continue
            chat.append(name + ': ' + line.strip())
    return chat

def output_file(filename, chat):
    with open(filename, 'w', encoding='utf-8' ) as f:
        for line in chat:
            f.write(line + '\n')
            
def main():
    chat = input_file('input.txt')
    output_file('output.txt', chat)

main()










            






        
  