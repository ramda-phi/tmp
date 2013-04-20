#!/usr/bin/env python
# -*- coding: utf-8 -*-
# greeting_by_time
# 
# return 'the Greeting',  according to place and time


TIMEZONE_TABLE = {
	"0" : "Boa tarde. [Portuguese](UTC +0)", # ポルトガル（ポルトガル語）, UTC0
	"1" : "Buon giorno. [Italian](UTC +1)", # イタリア（イタリア語）, UTC+1
	"2" : "Γειά　σαζ [Greek](UTC +2)", # ギリシア（ギリシャ語）, UTC+2
	"3" : "Jambo [Swahili](UTC +3)", # ケニア（スワヒリ語）, UTC+3
	"4" : "السلام عليكام (assalām alaikum) [Arabic](UTC +4)", # アラビア語, UTC+4
	"5" : "(raise eyebrows) [Maldivian](UTC +5)", # モルジブ（ディベヒ語）, UTC+5
	"6" : "TAMIN SA PI-VI LA? [Burmese](UTC +6)", # ミャンマー（ビルマ語）, UTC+6
	"7" : "Chào anh. / Chào chi. [Vietnamese](UTC +7)", # ヴェトナム, UTC+7
	"8" : "你好吗？ (nǐ hǎo ma.) [Chinese](UTC +8)", # 中国、シンガポール, UTC+8
	"9" : "こんにちは。 [Japanese](UTC +9)", # 日本, UTC+9
	"10" : "Hafa Adai. [Chamorro](UTC +10)", # グアム（チャモロ語）, UTC+10
	"11" : "UTC+11 [](UTC +11)", # ニューカレドニア, UTC+11
	"12" : "Kia ora [Māori](UTC -12)", # ニュージーランド（マオリ語）, UTC-12	
	"13" : "talofa [Samoan](UTC -11)", # サモア（サモア語）, UTC-11
	"14" : "Kia Orana [Cook Islands Māori](UTC -10)", # クック諸島（ラロトンガ語）, UTC-10
	"15" : "’ia ora na ’oe [Tahitian](UTC -9)", # タヒチ（タヒチ語）, UTC-9
	"16" : "UTC-8 [](UTC -8)", # UTC-8
	"17" : "UTC-7 [](UTC -7)", # UTC-7
	"18" : "Allillanmi. [Quechua](UTC -6)", # エクアドル（ケチュア語）, UTC-6
	"19" : "UTC-5(UTC -5)", # Hello [English]アメリカ（シカゴ）, UTC-5
	"20" : "UTC-4 [](UTC -4)", # UTC-4
	"21" : "fawaka? [Suriname](UTC -3)", # スリナム（スラナン語）, UTC-3
	"22" : "Buenas tardes [español](UTC -2)", # アルゼンチン（スペイン語）, UTC-2
	"23" : 'God dag. [Greenlandic Inuktitut](UTC -1)', # グリーンランド語, UTC-1
}

# get time
import datetime
d = datetime.datetime.utcnow()
utc = (7 - d.hour) % 24


# return Unicode text
def str_to_unicode(text):
    if type(text) == str:
        u_text = text.decode("utf-8")
    elif type(text) == unicode:
        u_text = text
    return u_text


greeting = str_to_unicode(TIMEZONE_TABLE[str(utc)])
print greeting
