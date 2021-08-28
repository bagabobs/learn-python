def func(a, b, c=7, *args, **kwargs):
    print('a, b, c:', a, b, c)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, *(5, 6, 7), **{'A': 'a', 'B': 'b'})
func(1, 2, 3, 4, 5, 6, 7, A='a', B='b')
