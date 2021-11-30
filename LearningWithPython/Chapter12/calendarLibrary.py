# --------------------------------------------------------------------------
# Author : Lilac Walia
# Date : 11/29/2021
# --------------------------------------------------------------------------

import calendar

cal = calendar.TextCalendar(firstweekday= 6)
cal.prmonth(2021, 12)

spanish = calendar.LocaleTextCalendar(6, "SPANISH")
spanish.pryear(2021)

french = calendar.LocaleTextCalendar(6, "FRENCH")
french.pryear(2021)

korean = calendar.LocaleTextCalendar(6, "KOREAN")
korean.pryear(2021)
# Instead of showing the Korean characters, symbols

calendar.isleap(2020) == "True"