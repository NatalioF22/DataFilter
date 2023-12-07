from meteor_data_class import MeteorDataEntry
def test_MeteorDataEntry_object():
    meteor_data = MeteorDataEntry('Meteor1', '123', 'Type1', 'Class1', 100, 'Fall', 2022, 1.0, 2.0, 'Location1', 'State1', 'county 1')

    assert meteor_data.get_name() == "Meteor1"
    assert meteor_data.get_id() == "123"
    assert meteor_data.get_mass() == 100
    assert meteor_data.get_name_type() == "Type1"
    assert meteor_data.get_rec_class() == "Class1"
    assert meteor_data.get_fall() == "Fall"
    assert meteor_data.get_year() == 2022
    assert meteor_data.get_rec_lat() == 1.0
    assert meteor_data.get_rec_long() == 2.0
    assert meteor_data.get_geo_location() == "Location1"
    assert meteor_data.get_states() == "State1"
    assert meteor_data.get_counties() == "county 1"
