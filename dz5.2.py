print('\nКлюч')
names = ['Дмитрий', 'Алексей', "Анна"]
salaries = [15000, 20000, 25000]
awards = ['10.0%', '7.25%', '5%']
print(f'исходные данные:\n{names}\n{salaries}\n{awards}')
print('Решение:')

print({name: salary * float(award[:-1]) / 100 for name, salary, award in zip(names, salaries, awards)})
