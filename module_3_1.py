calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    string_ = str(string)
    info = (len(string_), string_.upper(), string_.lower())
    count_calls()
    print(info)
    return

def is_contains(string, list_to_search):
    for i in list_to_search:
        unreg_a = string.lower()
        unreg_b = i.lower()
        if unreg_a == unreg_b:
            result = True
            break
        else:
            result = False
            continue
    count_calls()
    print(result)
    return


string_info('Supra')
string_info('Finish')
is_contains('DoLMotinec', ['Durak', 'Delmotinec', 'DOLMOTINEC'])
is_contains('RusIIa', ['uSA', 'RySiiA', 'Rosia'])
print(calls)
