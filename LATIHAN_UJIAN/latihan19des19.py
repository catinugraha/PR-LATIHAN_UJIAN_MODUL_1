def alphanumeric(string):
    y = list(filter(lambda num: len(num)<100,string))
    for i in y:
        if i.isdigit() or i.isalpha():
            hasil = True
        else:
            hasil = False
            break
    return hasil

print(alphanumeric('Heyho 124'))
print(alphanumeric('Heyho124'))
print(alphanumeric('Heyho124!'))
print(alphanumeric('.Heyho124'))