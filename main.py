#def old_macdonald(name):
    #first_letter = name[0]
    #inbetween = name[1:3]
    #fourth_letter = name[3]
    #rest = name[4:]

    #return first_letter.upper() + inbetween + fourth_letter.upper() + rest


#print(old_macdonald('macdonald'))


#def old_macdonald(name):
    #first_half = name[:3]
    #second_half = name[3:]

    #return first_half.capitalize() + second_half.capitalize()


#print(old_macdonald('macdonald'))


#def master_yoda(text):
    #wordlist = text.split()
    #reverse_wordlist = wordlist[::-1]
    #return reverse_wordlist


#print(master_yoda('I am home'))
#print(master_yoda('We are ready'))


#mylist = ['a', 'b', 'c']
#print('--'.join(mylist))
#print(''.join(mylist))
#print(' '.join(mylist))
#print('_'.join(mylist))


#def master_yoda(text):
    #wordlist = text.split()
    #reverse_wordlist = wordlist[::-1]
    #return ' '.join(reverse_wordlist)


#print(master_yoda('I am home'))
#print(master_yoda('We are ready'))


def almost_there(n):
    return (abs(100-n) <=10) or (abs(200-n) <=10)


print(almost_there(104))
print(almost_there(150))
print(almost_there(209))


