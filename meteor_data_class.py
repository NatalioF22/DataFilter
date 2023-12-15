"""
This is the MeteorDataEntry class definition, where we can create Meteors objects which holds data individually.
Author: Natalio Gomes
Date: December 5th, 2023
"""


class MeteorDataEntry:
    """
    This clss represents an individual meteor data entry. This class allows for the creation of Meteor objects, 
    each encapsulating detailed information about a meteorite, such as its name, classification, mass, and geographical 
    location data. Objects of this class can be used to store and retrieve meteor-related data efficiently.
    """

    def __init__(self, name: str,id: int, name_type: str, rec_class: str, mass_g: int, fall: str, year: int,
                 rec_lat: float, rec_long: float, geo_location: str, states: str, counties: str):
        """
        All the fields passed in the parameters are stored in the fields preset by self.
        Attributes:
            name (str): The name of the meteorite.
            id (int): A unique identifier for the meteorite.
            name_type (str): The type of name assigned to the meteorite.
            rec_class (str): The meteorite's classification.
            mass_g (int): The mass of the meteorite in grams.
            fall (str): The fall status of the meteorite (e.g., "Fell" or "Found").
            year (datetime): The year of the meteorite's fall or discovery.
            rec_lat (float): The recorded latitude of the meteorite's location.
            rec_long (float): The recorded longitude of the meteorite's location.
            geo_location (str): A string representation of the meteorite's geographical location.
            states (int): The state or states associated with the meteorite's location.
            counties (int): The county or counties associated with the meteorite's location.
        """
        self.name = name
        self.id = id
        self.name_type = name_type
        self.rec_class = rec_class
        self.mass_g = mass_g
        self.fall = fall
        self.year = year
        self.rec_lat = rec_lat
        self.rec_long = rec_long
        self.geo_location = geo_location
        self.states = states
        self.counties = counties

    def get_name(self):
        """ Returns the name of the meteorite. """
        return self.name

    def get_mass(self):
        """  Returns the mass of the meteorite in grams. """
        return self.mass_g

    def get_year(self):
        """ Returns the year of the meteorite's fall or discovery. """
        return self.year

    def get_id(self):
        """ Returns the unique identifier of the meteorite. """
        return self.id
    
    def get_name_type(self):
        """ Returns the type of name assigned to the meteorite. """
        return self.name_type
    
    def get_rec_class(self):
        """ Returns the classification of the meteorite. """
        return self.rec_class
    
    def get_fall(self):
        """ Returns the fall status of the meteorite. """
        return self.fall
    
    def get_rec_lat(self):
        """ Returns the recorded latitude of the meteorite's location. """
        return self.rec_lat
    
    def get_rec_long(self):
        """  Returns the recorded longitude of the meteorite's location. """
        return self.rec_long
    
    def get_geo_location(self):
        """  Returns a string representation of the meteorite's geographical location. """
        return self.geo_location
    
    def get_states(self):
        """ Returns the state or states associated with the meteorite's location. """
        return self.states
    
    def get_counties(self):
        """ Returns the county or counties associated with the meteorite's location. """
        return self.counties
    

