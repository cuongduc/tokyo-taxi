INPUT_FILE = 'data/point_coordinates.txt'
OUTPUT_FILE = 'sql/insert_points_table.sql'

f = open(INPUT_FILE, 'r')
of = open(OUTPUT_FILE, 'w')

for line in f:
    item = line.split(',')
    if len(item) != 3:
        continue
    else:
        id = item[0]
        lng = item[1]
        lat = item[2].replace('\n', '')
        sql_string = 'INSERT INTO points(id, geometry) VALUES({},ST_GeographyFromText(\'SRID=4326;POINT({} {})\'));'.format(id, lng, lat)
        print(sql_string)
        of.writelines(sql_string)
        of.writelines('\n')

of.close()
f.close()
