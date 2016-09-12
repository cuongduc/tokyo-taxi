INPUT_FILE = 'data/requests_with_income.txt'
OUTPUT_FILE = 'sql/insert_requests_with_income_table.sql'

f = open(INPUT_FILE, 'r')
of = open(OUTPUT_FILE, 'w')

for line in f:
    item = line.split(',')
    if len(item) != 10:
        print('Invalid line\n\a')
        continue
    else:
        sql_string = 'INSERT INTO requests_with_income(id, requested_time, start_point, ' \
                    'end_point, forward_time_start, forward_time_end, ' \
                    'backward_time_start, backward_time_end, milc_1, milc_2) ' \
                    'VALUES({},{},{},{},{},{},{},{},{},{});'.format(
                        item[0], item[1], item[2], item[3], item[4], item[5],
                        item[6], item[7], item[8], item[9].replace('\n','')
                    )
        print(sql_string)
        of.writelines(sql_string)
        of.writelines('\n')

of.close()
f.close()
