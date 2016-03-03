#coding:utf-8
from bottlenose import api
from bs4 import BeautifulSoup as bs
import sys
import traceback



#エラーは(-1, err_msg)って感じのタプルで返します。
#成功は(0, success_msg)
class amazonAPI:
    __AK = ""
    __SK = ""
    __AT = ""
    __amazon   = None
    __soup     = None
    _keyword = ""

    def __init__(self, ACCESS_KEY, SECRET_KEY, TAG, region="JP"):
        self.__AK = ACCESS_KEY
        self.__SK = SECRET_KEY
        self.__AT = TAG
        self.__amazon = api.Amazon(self.__AK, self.__SK, self.__AT, Region=region)


    #検索する時は最初のこのメソッドを呼び出す
    def search(self, Keywords,
                     ItemPage=1,
                     SearchIndex="Books", 
                     ResponseGroup="ItemAttributes,Images,OfferFull",
                     MerchantId="All",
                     Condition="All",
                     Version="2011-08-02"):

        try:
            res = self.__amazon.ItemSearch(Keywords=Keywords,
                                           ItemPage=ItemPage,
                                           SearchIndex=SearchIndex,
                                           ResponseGroup=ResponseGroup,
                                           MerchantId=MerchantId,
                                           Condition=Condition,
                                           Version=Version)

            self.__soup = bs(res,"html.parser")
            self._keyword = Keywords

        except:
            print(traceback.format_exc(sys.exc_info()[2]))
            return (-1, "something is wrong. Make instance and try again!")

        return (0,"OK")
        

    #検索結果のURLを返す
    def get_moreURL(self):
        if not self._keyword:
            return (-1, "Call search method first!")

        return self.__soup.find("moresearchresultsurl").text


    #現在設定されている検索ワードを返す
    def getKeyword(self):
        return self._keyword


    #number:1〜10を指定して検索結果から一件取得。辞書型で返す。
    def get_with_number(self,number):
        if not 1 <= number <= 10:
            return (-1, "Please set number in range of 1 to 10")

        try:
            tmp = self.__soup.findAll("item")[number-1]

            #商品へのリンク
            if tmp.detailpageurl:
                URL = tmp.detailpageurl.text
            else:
                URL = None

            #中古ショップの一覧へのリンク
            if tmp.moreoffersurl:
                used_URL = tmp.moreoffersurl.text
            else:
                used_URL = None

            #本のタイトル
            if tmp.title:
                title = tmp.title.text
            else:
                title = None

            #本の著者
            if tmp.itemattributes.author:
                author = tmp.itemattributes.author.text
            else:
                author = None

            #出版社
            if tmp.studio:
                studio = tmp.studio.text
            else:
                studio = None

            #サムネイル小
            if tmp.smallimage.url:
                small = tmp.smallimage.url.text
            else:
                small = None

            #サムネイル中
            if tmp.mediumimage.url:
                middle = tmp.mediumimage.url.text
            else:
                middle = None

            #サムネイル大
            if tmp.largeimage.url:
                large = tmp.largeimage.url.text
            else:
                large = None

            #新品で最も安い価格(基本的に商品の最高価格)
            if tmp.offersummary.lowestnewprice:
                amount_new = tmp.offersummary.lowestnewprice.amount.text
            else:
                amount_new = None
            if tmp.offersummary.lowestnewprice:
                format_new = tmp.offersummary.lowestnewprice.formattedprice.text
            else:
                format_new = None

            #中古で最も安い価格(基本的に商品の最低価格)
            if tmp.offersummary.lowestusedprice:
                amount_used = tmp.offersummary.lowestusedprice.amount.text
            else:
                amount_used = None
            if tmp.offersummary.lowestusedprice:
                format_used = tmp.offersummary.lowestusedprice.formattedprice.text
            else:
                format_used = None


            #新品商品のコンディションと在庫状況
            try:
                zaiko_new = tmp.findAll("offer")[0].availability.text
            except:
                zaiko_new = None

            #中古商品のコンディションと在庫状況
            try:
                zaiko_used = tmp.findAll("offer")[1].availability.text
            except:
                zaiko_used = None

            return dict(URL=URL,
                        used_URL=used_URL,
                        title=title,
                        author=author,
                        studio=studio,
                        thumbnail=[small, middle, large],
                        new_price=[amount_new,format_new],
                        used_price=[amount_used,format_used],
                        new_cond=["new",zaiko_new],
                        used_cond=["used",zaiko_used])

        except:
            print(traceback.format_exc(sys.exc_info()[2]))
            return (-1, "APIの仕様が変わった可能性があります…")


    def soup(self):
        if not self._keyword:
            return (-1, "Call search method first!")

        return self.__soup


if __name__ == "__main__":
    myapi = amazonAPI(AK, SK, AT)

    myapi.search("応用物理学")

    for val in range(1,11):
        print(myapi.get_with_number(number=val))
        print("-"*30)
