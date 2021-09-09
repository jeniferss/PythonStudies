credit_card_number = '5610591081018250'
number_list = list(credit_card_number)
p_num = list(map(int, number_list[1::2]))
i_num = list(map(int, number_list[0::2]))

p_sum = sum(p_num)
i_by_two_num = [i * 2 for i in i_num]

i_by_two_group = map(lambda x: sum(int(digit) for digit in str(x)), i_by_two_num)

i_by_two_sum = sum(list(i_by_two_group))

sum = p_sum + i_by_two_sum

print('Valid') if sum % 10 == 0 else print('Not Valid')
