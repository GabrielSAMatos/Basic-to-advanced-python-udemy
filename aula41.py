try:
    print('Begin')
    a = 1/1
    a/0
    print(a)
    print('End')

except Exception as error:
    print('Name:', error.__class__.__name__)
    print('MSG:', error)

finally: 
    print('Finally')