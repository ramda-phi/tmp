#!/usr/bin/env python
# -*- coding: utf-8 -*-
# greeting_by_time
# 
# return 'the Greeting',  according to place and time


TIMEZONE_TABLE = {
	"0" : u"Boa tarde. [Portuguese](UTC +0)", # ポルトガル（ポルトガル語）, UTC0
	"1" : u"Buon giorno. [Italian](UTC +1)", # イタリア（イタリア語）, UTC+1
	"2" : u"Γειά　σαζ [Greek](UTC +2)", # ギリシア（ギリシャ語）, UTC+2
	"3" : u"Jambo [Swahili](UTC +3)", # ケニア（スワヒリ語）, UTC+3
	"4" : u"السلام عليكام (assalām alaikum) [Arabic](UTC +4)", # アラビア語, UTC+4
	"5" : u"(raise eyebrows) [Maldivian](UTC +5)", # モルジブ（ディベヒ語）, UTC+5
	"6" : u"TAMIN SA PI-VI LA? [Burmese](UTC +6)", # ミャンマー（ビルマ語）, UTC+6
	"7" : u"Chào anh. / Chào chi. [Vietnamese](UTC +7)", # ヴェトナム, UTC+7
	"8" : u"你好吗？ (nǐ hǎo ma.) [Chinese](UTC +8)", # 中国、シンガポール, UTC+8
	"9" : u"こんにちは。 [Japanese](UTC +9)", # 日本, UTC+9
	"10" : u"Hafa Adai. [Chamorro](UTC +10)", # グアム（チャモロ語）, UTC+10
	"11" : u"UTC+11 [](UTC +11)", # ニューカレドニア, UTC+11
	"12" : u"Kia ora [Māori](UTC -12)", # ニュージーランド（マオリ語）, UTC-12	
	"13" : u"talofa [Samoan](UTC -11)", # サモア（サモア語）, UTC-11
	"14" : u"Kia Orana [Cook Islands Māori](UTC -10)", # クック諸島（ラロトンガ語）, UTC-10
	"15" : u"’ia ora na ’oe [Tahitian](UTC -9)", # タヒチ（タヒチ語）, UTC-9
	"16" : u"UTC-8 [](UTC -8)", # UTC-8
	"17" : u"Bonjour. [French](UTC -7)", # UTC-7, カナダ
	"18" : u"Allillanmi. [Quechua](UTC -6)", # エクアドル（ケチュア語）, UTC-6
	"19" : u"UTC-5(UTC -5)", # Hello [English]アメリカ（シカゴ）, UTC-5
	"20" : u"UTC-4 [](UTC -4)", # UTC-4
	"21" : u"fawaka? [Suriname](UTC -3)", # スリナム（スラナン語）, UTC-3
	"22" : u"Buenas tardes [español](UTC -2)", # アルゼンチン（スペイン語）, UTC-2
	"23" : u'God dag. [Greenlandic Inuktitut](UTC -1)', # グリーンランド語, UTC-1
}

# get time
def am7Greeting():
	import datetime
	d = datetime.datetime.utcnow()
	utc = (7 - d.hour) % 24
	return TIMEZONE_TABLE[str(utc)]

