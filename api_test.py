from api import *
import pprint

def test_get_api():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?format=json&applicationId=1019079537947262807&genreId=100283&elements=itemName,itemPrice"
    res = get_api(url=url)

    #チェック
    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemName"]
    assert res["Items"][0]["Item"]["itemPrice"]