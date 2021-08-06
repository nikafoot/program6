import requests
import urllib
import pandas as pd
from pandas import json_normalize


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    genreID = "100283"
    """
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={}&applicationId=1019079537947262807".format(
        keyword)
    """
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&applicationId=1019079537947262807&genreId={}&elements=itemName,itemPrice".format(genreID)
    jsondata = get_api(url)
    df = json_normalize(jsondata['Items'])
    df.to_csv('api.csv', encoding='utf_8_sig')



main()