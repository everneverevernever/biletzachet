slovar = {}
f_in = open('in.txt', 'r')
for line in f_in:
    date, reader, book, writer = line.split()

    book = (book.replace('-', ' '))

    if date in slovar:
        slovar[date].append(reader)
    else:
        slovar[reader] = [book]

slovar.pop('Пятачок')

f_in.close()

f_out = open('out.txt', 'w')

for reader in sorted(slovar):
    f_out.write(reader + ':' + ';'.join(sorted(slovar[reader])) + '\n')

f_out.close()