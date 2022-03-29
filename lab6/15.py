data = ''' 1 1 1 1 1 1 1
        1 1 1 1 1 1 1
        0 1 1 1 1 1 1
    '''
print(f'data: {data}')
print(any(not all(map(int, x.split())) for x in data.split('\n')))