class SpaceAge(object):
    SECONDS_IN_DAY = 60 * 60 * 24
    EARTH_YEAR = 365.25
    MERCURY_YEAR = 0.2408467 * EARTH_YEAR
    VENUS_YEAR = 0.61519726 * EARTH_YEAR
    MARS_YEAR = 1.8808158 * EARTH_YEAR
    JUPITER_YEAR = 11.862615 * EARTH_YEAR
    SATURN_YEAR = 29.447498 * EARTH_YEAR
    URANUS_YEAR = 84.016846 * EARTH_YEAR
    NEPTUNE_YEAR = 164.79132 * EARTH_YEAR

    def __init__(self, seconds):
       self.seconds = seconds

    def on_mercury(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.MERCURY_YEAR, 2)
  
    def on_venus(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.VENUS_YEAR, 2)

    def on_earth(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.EARTH_YEAR, 2)

    def on_mars(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.MARS_YEAR, 2)

    def on_jupiter(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.JUPITER_YEAR, 2)

    def on_saturn(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.SATURN_YEAR, 2)

    def on_uranus(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.URANUS_YEAR, 2)

    def on_neptune(self):
       return round(self.seconds / SpaceAge.SECONDS_IN_DAY / SpaceAge.NEPTUNE_YEAR, 2)
       
