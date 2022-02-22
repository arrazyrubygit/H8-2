#Grouping statement: Identation
if 'mamalia' in ['mamalia','kucing','kelelawar']:
    print('Outer condition is true')
    
    if 50/2 == 20:
        print('Inner condition 1')
    print('Between inner condition')
    
    if 100 < 3000: 
        print('Inner condition 2')

    print('end of outer condition')
print('After outer condition')
print('-' * 20)
#Grouping statement: Block
if 'foo' in ['bar', 'baz', 'qux']:
    print('Expression was true')
    print('Executing statement in suite')
    print('...')
    print('Done.')
    
print('After conditional')