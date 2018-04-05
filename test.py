from pyhokchew import convert
from pyhokchew.models.CikLinSyllable import CikLinSyllable


print(CikLinSyllable.parse_ciklin_string('波光切','下上'), convert.ciklin_to_foochow_romanized(CikLinSyllable.parse_ciklin_string('波光切','下上')))

