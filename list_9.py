def molecula_count(atom_list, molecula_list):
  for i in range(len(atom_list)):
    atom_list[i] = atom_list[i] // molecula_list[i]
  return print('number of possible molecules: ', min(atom_list))
def formula_analysis(formula):
y = 'y'
while y == 'y':
  input_atoms = input('enter number of atoms C, O, H, using comma: ').split(',')
  input_molecula = input('enter number of atoms in molecula: [C, O, H]: ').split(',')
  atom_list = list(map(int, input_atoms))
  molecula_list = list(map(int, input_molecula))
  molecula_count(atom_list, molecula_list)
  y = input('restart?(y/n): ')
print('goodbye')
  
