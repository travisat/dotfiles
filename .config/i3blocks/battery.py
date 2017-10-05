#!/usr/bin/env python3
#
# A battery indicator blocklet script for i3blocks

from subprocess import check_output

status = check_output(['acpi'], universal_newlines=True)
state = status.split(": ")[1].split(", ")[0]
commasplitstatus = status.split(", ")
percentleft = int(commasplitstatus[1].rstrip("%\n"))

#ICON_COLOR = "#b58900"
ICON_COLOR = "#002b36"
TEXT_COLOR = "#002b36"

FA_PLUG = "<span color='{}' font='FontAwesome'>\uf1e6</span>".format(ICON_COLOR)
FA_BATTERY = "<span color='{}' font='FontAwesome'>{}</span>"

fulltext = ""
timeleft = ""

def getbat(percent):
    if percent < 10:
        return ("#dc322f","\uf244")
    if percent < 40:
        return (ICON_COLOR,"\uf243")
    if percent < 70:
        return (ICON_COLOR,"\uf242")
    if percent < 90:
        return (ICON_COLOR,"\uf241")
    return (ICON_COLOR,"\uf240")


if state == "Discharging":
    fulltext += FA_BATTERY.format(*getbat(percentleft))
    #time = commasplitstatus[-1].split()[0]
    #time = ":".join(time.split(":")[0:2])
    #timeleft = " ({})".format(time)
else:
    fulltext += FA_PLUG

form =  " <span color='{}'>{}%</span>"
fulltext += form.format(TEXT_COLOR, percentleft)
form = "<span color='{}'>{}</span>"
fulltext += form.format(TEXT_COLOR, timeleft)

print(fulltext)
