with open(file='input/names/invited_names.txt', mode='r') as file_names:
    names = file_names.read().split('\n')

for name in names:
    with open(file='input/letters/starting_letter.txt', mode='r') as file_letter:
        letter = file_letter.read().replace('[name]', name)

    with open(file=f'output/ready_to_send/letter_to_{name}', mode='w') as final_letter:
        final_letter.write(letter)
