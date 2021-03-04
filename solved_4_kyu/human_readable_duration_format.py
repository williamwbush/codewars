# https://www.codewars.com/kata/52742f58faf5485cae000b9a

def format_duration(seconds):    
    if seconds == 0:
        return 'now'
    
    comp = {}
    comp['y'] = seconds // (60*60*24*365)
    comp['d'] = int(seconds / (60*60*24) % 365)
    comp['h'] = int(seconds / (60*60) % 24)
    comp['m'] = int(seconds / 60 % 60)
    comp['s'] = seconds % 60
    
    comp_n = [key for key in comp.keys() if comp[key] != 0]
    
    return ((comp['y'] and str(comp['y']) or '') + ' year' * ('y' in comp_n) + 's' * (comp['y'] > 1) + ',' * ('y' in ((['x','x','x','x'] + comp_n[::-1])[6:])) +
        ' and' * (len(comp_n) > 1 and 'd' == comp_n[-1]) + ' ' * ('d' in (['x','x','x','x'] + comp_n)[5:]) + (comp['d'] and (str(comp['d'])) or '') + ' day' * ('d' in comp_n) + 's' * (comp['d'] > 1) + ',' * ('d' in ((['x','x','x','x'] + comp_n[::-1])[6:])) +
        ' and' * (len(comp_n) > 1 and 'h' == comp_n[-1]) + ' ' * ('h' in (['x','x','x','x'] + comp_n)[5:]) + (comp['h'] and (str(comp['h'])) or '') + ' hour' * ('h' in comp_n) + 's' * (comp['h'] > 1) + ',' * ('h' in ((['x','x','x','x'] + comp_n[::-1])[6:])) +
        ' and' * (len(comp_n) > 1 and 'm' == comp_n[-1]) + ' ' * ('m' in (['x','x','x','x'] + comp_n)[5:]) + (comp['m'] and (str(comp['m'])) or '') + ' minute' * ('m' in comp_n) + 's' * (comp['m'] > 1) + 
        ' and' * (len(comp_n) > 1 and 's' == comp_n[-1]) + ' ' * ('s' in (['x','x','x','x'] + comp_n)[5:]) + (comp['s'] and (str(comp['s'])) or '') + ' second' * ('s' in comp_n) + 's' * (comp['s'] > 1))

print(format_duration(3662))