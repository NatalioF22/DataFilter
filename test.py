file_obj = open("meteorite_landings_data.txt")
header = file_obj.readline()
for i in file_obj:
    values = i.split("\t")
    name, meteorite_id, name_type, rec_class, mass_g, fall, year, rec_lat, rec_long, geo_location, states, counties = values
    try:
        if 2900000 <= int(mass_g) <=1000000000000000:
            print(name)
    except ValueError:
        pass