from pydxs.bands import determine_band

class Spot():
    """This class can read the format used by most amateur radio spotting systems. It is specifically
    designed for the output used by CW Skimmer and read by the N3FJP logging software. It's my
    understanding that's a standard format, but I don't have any documentation on its' implementation
    so this is entirely reverse-engineered. If you have more information or test cases that don't parse
    properly please send them my way to look at."""

    def __init__(self, report=""):
        if report:
            self._report = report
            self.make_report()

    def make_report(self):
        self.preamble = self._report[0:6].strip()
        self.reporting_station = self._report[6:17].replace(':', '').strip()
        self.frequency = self._report[17:25].strip()
        self.heard_station = self._report[26:39].strip()
        self.comments = self._report[39:65].strip()
        self.heard_station_location = self._report[66:69].strip()
        self.time = self._report[70:75].strip()
        self.reporting_station_location = self._report[76:78].strip()
        self.raw = self._report.strip()

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
