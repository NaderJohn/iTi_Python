def mario_pyramid():
    lst=[' ',' ',' ',' ',' ',' ']
    pyramid = []
    for i in range(6):
        lst.remove(' ')
        lst.append('*')
        pyramid.append(''.join(lst))
    return '\n'.join(pyramid)