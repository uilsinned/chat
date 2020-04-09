#計算每個人聊天總字數
#計算每個人一共傳了幾個貼圖
#計算每個人一共傳了幾張圖片

def input_file(filename):    
    chat = []
    with open(filename, 'r', encoding='utf-8-sig' ) as f:
        for line in f:
            chat.append(line.strip())       
    return chat


def convert(chat):
    Allen_count = 0
    Allen_sticker_count = 0
    Allen_image_count = 0
    Viki_count = 0
    Viki_sticker_count = 0
    Viki_image_count = 0
    for line in chat:
        s = line.split(' ')
        if s[1] == 'Allen':
            if s[2] == '貼圖':
                Allen_sticker_count += 1
            elif s[2] == '圖片':
                Allen_image_count += 1
            else:
                for d in s[2:]:
                    Allen_count += len(d)
        elif s[1] == 'Viki':
            if s[2] == '貼圖':
                Viki_sticker_count += 1
            elif s[2] == '圖片':
                Viki_image_count += 1
            else:
                for d in s[2:]:
                    Viki_count += len(d)
    print('Allen一共講了', Allen_count, '個字')
    print('Allen一共傳了', Allen_sticker_count, '個貼圖')
    print('Allen一共傳了', Allen_image_count, '張圖片')
    print('Viki一共講了', Viki_count, '個字') 
    print('Viki一共傳了', Viki_sticker_count, '個貼圖')
    print('Viki一共傳了', Viki_image_count, '張圖片')     


def main():
    chat = input_file('Line.txt')
    convert(chat)

main()