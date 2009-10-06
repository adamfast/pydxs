from decimal import Decimal

# frequencies in kilocycles
ARRL_BAND_PLAN = (
    (Decimal('1800.0'),    Decimal('2000.0'),    '160m'),
    (Decimal('3590.0'),    Decimal('4000.0'),    '80m'),
    (Decimal('7000.0'),    Decimal('7300.0'),    '40m'),
    (Decimal('10100.0'),   Decimal('10150.0'),   '30m'),
    (Decimal('14000.0'),   Decimal('14350.0'),   '20m'),
    (Decimal('18068.0'),   Decimal('18168.0'),   '17m'),
    (Decimal('21000.0'),   Decimal('21450.0'),   '15m'),
    (Decimal('24890.0'),   Decimal('24990.0'),   '12m'),
    (Decimal('28000.0'),   Decimal('29700.0'),   '10m'),
    (Decimal('50000.0'),   Decimal('54000.0'),   '6m'),
    (Decimal('144000.0'),  Decimal('148000.0'),  '2m'),
    (Decimal('222000.0'),  Decimal('225000.0'),  '1.25m'), # not tested
    (Decimal('420000.0'),  Decimal('450000.0'),  '70cm'),
    (Decimal('902000.0'),  Decimal('928000.0'),  '33cm'), # not tested
    (Decimal('1240000.0'), Decimal('1300000.0'), '23cm'), # not tested
)

def determine_band(value, band_plan=ARRL_BAND_PLAN):
    """Determines (based on an easily overridable band plan) which band the frequency supplied falls within."""
    value = Decimal(str(value))

    for band in band_plan:
        if value > band[0] and value < band[1]:
            return band[2]
    return '?'
