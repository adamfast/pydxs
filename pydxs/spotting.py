from pydxs.bands import determine_band

class Spot(object):
    """This class can read the format used by most amateur radio spotting systems. It is specifically
    designed for the output used by CW Skimmer and read by the N3FJP logging software. It's my
    understanding that's a standard format, but I don't have any documentation on its' implementation
    so this is entirely reverse-engineered. If you have more information or test cases that don't parse
    properly please send them my way to look at."""

    def __init__(self, report=""):
        if report != "":
            self._report = report
        else:
            self._report = 'DX                                                                    0000Z\n'

    def get_preamble(self):
        if self._report:
            return self._report[0:6].strip()
        return ''
    preamble = property(get_preamble, None, None, None)

    def get_reporting_station(self):
        if self._report:
            return self._report[6:17].replace(':', '').strip()
        return ''
    reporting_station = property(get_reporting_station, None, None, None)

    def get_frequency(self):
        if self._report:
            return self._report[17:25].strip()
        return ''

    def set_frequency(self, value):
        self._report = self._report[:17] + value.ljust(8) + self._report[25:]
    frequency = property(get_frequency, set_frequency, None, None)

    def get_heard_station(self):
        if self._report:
            return self._report[26:39].strip()
        return ''

    def set_heard_station(self, value):
        self._report = self._report[:26] + value.ljust(13) + self._report[39:]
    heard_station = property(get_heard_station, set_heard_station, None, None)

    def get_comments(self):
        if self._report:
            return self._report[39:65].strip()
        return ''

    def set_comments(self, value):
        self._report = self._report[:41] + value.ljust(24) + self._report[65:]
    comments = property(get_comments, set_comments, None, None)

    def get_heard_station_location(self):
        if self._report:
            return self._report[66:69].strip()
        return ''
    heard_station_location = property(get_heard_station_location, None, None, None)

    def get_time(self):
        if self._report:
            return self._report[70:75].strip()
        return ''
    time = property(get_time, None, None, None)

    def get_reporting_station_location(self):
        if self._report:
            return self._report[76:78].strip()
        return ''
    reporting_station_location = property(get_reporting_station_location, None, None, None)

    def get_raw(self):
        if self._report:
            return self._report
        return ''
    raw = property(get_raw, None, None, None)

    def get_band(self):
        if self.raw:
            return determine_band(self.frequency)
        return ''
    band = property(get_band, None, None, None)

    def __unicode__(self):
        return self.raw

    def __str__(self):
        return self.__unicode__()

    def __repr__(self):
        return self.__unicode__()
