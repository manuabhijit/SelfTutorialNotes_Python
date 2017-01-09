first = ['f_aman', 'f_varun', 'f_rajan']
second = ['s_amit', 's_rauf', 's_rahul']

combine_sf = zip(first, second)

third =['t_tarun','t_varun', 't_abdul']

combine = zip(first, second, third)

for f, s, t in combine:
    print combine