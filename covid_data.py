#!/usr/bin/env python3
import requests
import sys
import locale
locale.setlocale(locale.LC_ALL, 'en_US')


def getSumData():
    response1 = requests.get(
        "https://coronavirus-19-api.herokuapp.com/all")
    data1 = response1.json()
    response2 = requests.get(
        "https://coronavirus-19-api.herokuapp.com/countries/usa")
    data2 = response2.json()
    response3 = requests.get('https://coronavirusapi.com/getTimeSeriesJson/TX')
    data3 = response3.json()
    print()
    print('Global Total Cases: ' +
          str(locale.format_string("%d", data1['cases'], grouping=True)))
    print('Global Total Deaths: ' +
          str(locale.format_string("%d", data1['deaths'], grouping=True)))
    print()
    print('USA Total Cases: ' +
          str(locale.format_string("%d", data2['cases'], grouping=True)))
    print('USA Total Deaths: ' +
          str(locale.format_string("%d", data2['deaths'], grouping=True)))
    print()
    print('Texas Total Cases: ' +
          str(locale.format_string("%d", data3[-1]['positive'], grouping=True)))
    print('Texas Total Deaths: ' +
          str(locale.format_string("%d", data3[-1]['deaths'], grouping=True)))
    print()


if len(sys.argv) > 1:
    if sys.argv[1] == 's' or sys.argv[1] == 'state':
        response3 = requests.get(
            'https://coronavirusapi.com/getTimeSeriesJson/{}'.format(sys.argv[2]))
        if response3.content != b'Please use a 2 letter state abbreviation':
            data3 = response3.json()
            print()
            print('Total Cases: ' +
                  str(locale.format_string("%d", data3[-1]['positive'], grouping=True)))
            print('Total Deaths: ' +
                  str(locale.format_string("%d", data3[-1]['deaths'], grouping=True)))
            print()
        else:
            print()
            print('Use a 2 letter state abbreviation')
            print()
    elif sys.argv[1] == 'g' or sys.argv[1] == 'global':
        response1 = requests.get(
            "https://coronavirus-19-api.herokuapp.com/all")
        data1 = response1.json()
        print()
        print('Total Cases: ' +
              str(locale.format_string("%d", data1['cases'], grouping=True)))
        print('Total Deaths: ' +
              str(locale.format_string("%d", data1['deaths'], grouping=True)))
        print()
    else:
        if sys.argv[1] == 'c' or sys.argv[1] == 'country':
            response = requests.get(
                "https://coronavirus-19-api.herokuapp.com/countries/{}".format(' '.join(sys.argv[2:])))
        else:
            response = requests.get(
                "https://coronavirus-19-api.herokuapp.com/countries/{}".format(' '.join(sys.argv[1:])))
        if response.content != b'Country not found':
            data = response.json()
            print()
            print('Total Cases: ' +
                  str(locale.format_string("%d", data['cases'], grouping=True)))
            print('Total Deaths: ' +
                  str(locale.format_string("%d", data['deaths'], grouping=True)))
            print()
        else:
            print()
            print('Country Not Found')
            print()
else:
    getSumData()
# https://coronavirus-19-api.herokuapp.com/
# https://coronavirusapi.com
