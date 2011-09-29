from django.test import TestCase
from pydxs.bands import determine_band
from pydxs.spotting import Spot

class ParsingTest(TestCase):

    def test_basic_spot(self):
        spot = Spot('DX de W8IQ:      14008.1  ON1708M      CQ                          ON 1410Z OH\n')
        self.failUnlessEqual(spot.preamble, 'DX de')
        self.failUnlessEqual(spot.reporting_station, 'W8IQ')
        self.failUnlessEqual(spot.frequency, '14008.1')
        self.failUnlessEqual(spot.heard_station, 'ON1708M')
        self.failUnlessEqual(spot.comments, 'CQ')
        self.failUnlessEqual(spot.heard_station_location, 'ON')
        self.failUnlessEqual(spot.time, '1410Z')
        self.failUnlessEqual(spot.reporting_station_location, 'OH')

    def test_three_char_callsign(self):
        spot = Spot('DX de K5QQ-#:    14040.4  N6O            11 dB  30 WPM  CQ            1935Z') # intentionally left off CR
        self.failUnlessEqual(spot.reporting_station, 'K5QQ-#')
        self.failUnlessEqual(spot.frequency, '14040.4')
        self.failUnlessEqual(spot.heard_station, 'N6O')
        self.failUnlessEqual(spot.comments, '11 dB  30 WPM  CQ')
        self.failUnlessEqual(spot.time, '1935Z')

    def test_four_char_callsign(self):
        spot = Spot('DX de K5QQ-#:    14030.8  F2GL           14 dB  14 WPM  CQ            1941Z\n')
        self.failUnlessEqual(spot.reporting_station, 'K5QQ-#')
        self.failUnlessEqual(spot.frequency, '14030.8')
        self.failUnlessEqual(spot.heard_station, 'F2GL')
        self.failUnlessEqual(spot.comments, '14 dB  14 WPM  CQ')
        self.failUnlessEqual(spot.time, '1941Z')

    def test_five_char_callsign(self):
        spot = Spot('DX de K5QQ-#:    14015.1  G4FYF           7 dB  16 WPM  DE            1940Z\n')
        self.failUnlessEqual(spot.frequency, '14015.1')
        self.failUnlessEqual(spot.heard_station, 'G4FYF')
        self.failUnlessEqual(spot.comments, '7 dB  16 WPM  DE')
        self.failUnlessEqual(spot.time, '1940Z')

    def test_six_char_callsign(self):
        spot = Spot('DX de K5QQ-#:    14022.3  XE1TNC         15 dB  26 WPM  DE            1940Z\n')
        self.failUnlessEqual(spot.frequency, '14022.3')
        self.failUnlessEqual(spot.heard_station, 'XE1TNC')
        self.failUnlessEqual(spot.comments, '15 dB  26 WPM  DE')
        self.failUnlessEqual(spot.time, '1940Z')

    def test_blank(self):
        spot = Spot()
        self.failUnlessEqual(len(spot.raw), 76)
        self.failUnlessEqual(spot.raw, 'DX                                                                    0000Z\n')

class BandDeterminationTest(TestCase):
    def test_160m(self):
        self.failUnlessEqual(determine_band('1823.7'), '160m')

    def test_80m(self):
        self.failUnlessEqual(determine_band('3797.0'), '80m')

    def test_40m(self):
        self.failUnlessEqual(determine_band('7157.7'), '40m')

    def test_30m(self):
        self.failUnlessEqual(determine_band('10107.0'), '30m')

    def test_20m(self):
        self.failUnlessEqual(determine_band('14008.1'), '20m')

    def test_17m(self):
        self.failUnlessEqual(determine_band('18085.1'), '17m')

    def test_15m(self):
        self.failUnlessEqual(determine_band('21005.0'), '15m')

    def test_12m(self):
        self.failUnlessEqual(determine_band('24950.1'), '12m')

    def test_10m(self):
        self.failUnlessEqual(determine_band('28350.0'), '10m')

    def test_6m(self):
        self.failUnlessEqual(determine_band('50130.0'), '6m')

    def test_2m(self):
        self.failUnlessEqual(determine_band('145920.0'), '2m')

    def test_70cm(self):
        self.failUnlessEqual(determine_band('432270.0'), '70cm')

    def test_public_safety(self):
        self.failUnlessEqual(determine_band('165750.0'), '?')
