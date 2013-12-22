#!/usr/bin/python

__author__ = 'jdr0dn3y'

import json
import urllib2
btcurl = 'https://btc-e.com/api/2/btc_usd/ticker'
btcltcurl = 'https://btc-e.com/api/2/ltc_btc/ticker'
ltcurl = 'https://btc-e.com/api/2/ltc_usd/ticker'

#Enter the number of *coins you have
btcowned = 1
ltcowned = 1


def parse(json_data):
    json_data = json.loads(json_data)

    # get to where the days are listed with the data we want.
    high = json_data['ticker']['high']
    low = json_data['ticker']['low']
    avg = json_data['ticker']['avg']
    last = json_data['ticker']['last']

    return high, low, avg, last


def fetch(tickurl):
    # url with API code intact.............TTTHHHIIIISSSSSS
    url = tickurl

    try:
        # gets the data from the url and reads it like a file
        response = urllib2.urlopen(url).read()
    except urllib2.URLError:
        sys.exit()

    return response


if __name__ == '__main__':
    print 'BTC-E Values'
responsebtc = fetch(btcurl)
    highbtc, lowbtc, avgbtc, lastbtc = parse(responsebtc)
    print "BTC / USD"
print "High : %s" % (highbtc)
print "Low  : %s" % (lowbtc)
print "Avg  : %s" % (avgbtc)
print "Last : %s" % (lastbtc)
    print ""

    responsebtcltc = fetch(btcltcurl)
    highbtcltc, lowbtcltc, avgbtcltc, lastbtcltc = parse(responsebtcltc)
    print "LTC / BTC"
print "High : %s" % (highbtcltc)
print "Low  : %s" % (lowbtcltc)
print "Avg  : %s" % (avgbtcltc)
print "Last : %s" % (lastbtcltc)
    print ""

    responseltc = fetch(ltcurl)
    highltc, lowltc, avgltc, lastltc = parse(responseltc)
    print "LTC / USD"
print "High : %s" % (highltc)
print "Low  : %s" % (lowltc)
print "Avg  : %s" % (avgltc)
print "Last : %s" % (lastltc)
    print ""

    #Prints current value of *coins owned.
    # You will need to manually enter the number of coins you own. Will update to automated in later release.
    print "BTC Value: " + str((float(lastbtc) * btcowned))
    print "LTC Value: " + str((float(lastltc) * ltcowned))
