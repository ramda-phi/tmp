#!/usr/bin/env python
# -*- coding: utf-8 -*-
# greeting_by_time
# 
# return 'the Greeting',  according to place and time


TIMEZONE_TABLE = {
	"0" : u"Cén chaoi a bhfuil tú? [Language: Gaeilge, Republic of Ireland](UTC +0)", # アイルランド（アイルランド語）, UTC0
	"1" : u"Buon giorno. [Language: Italian, Italy](UTC +1)", # イタリア（イタリア語）, UTC+1
	"2" : u"Γειά　σαζ [Language: Greek, Hellenic Republic](UTC +2)", # ギリシア（ギリシャ語）, UTC+2
	"3" : u"Jambo [Language: Swahili, Republic of Kenya](UTC +3)", # ケニア（スワヒリ語）, UTC+3
	"4" : u"السلام عليكام (assalām alaikum) [Language: Arabic](UTC +4)", # アラビア語, UTC+4
	"5" : u"(raise eyebrows) [Language: Maldivian, Republic of Maldives](UTC +5)", # モルジブ（ディベヒ語）, UTC+5
	"6" : u"TAMIN SA PI-VI LA? [Language: Burmese, Republic of the Union of Myanmar](UTC +6)", # ミャンマー（ビルマ語）, UTC+6
	"7" : u"Chào anh. / Chào chi. [Language: Vietnamese, Socialist Republic of Vietnam](UTC +7)", # ヴェトナム（ヴェトナム語）, UTC+7
	"8" : u"你好吗？ (nǐ hǎo ma.) [Language: Chinese, China](UTC +8)", # 中国（中国語）, UTC+8
	"9" : u"こんにちは。 [Language: Japanese, Japan](UTC +9)", # 日本（日本語）, UTC+9
	"10" : u"Hafa Adai. [Language: Chamorro, Guam](UTC +10)", # グアム（チャモロ語）, UTC+10
	"11" : u"Здравствуйте! [Language: Russian、Russia](UTC +11)", # ロシア（ロシア語）, UTC+11
	"12" : u"Kia ora [Language: MāoriNew, Zealand(Aotearoa)](UTC -12)", # ニュージーランド（マオリ語）, UTC-12	
	"13" : u"talofa [Language: Samoan, Independent State of Samoa](UTC -11)", # サモア（サモア語）, UTC-11
	"14" : u"Kia Orana [Language: Rarotongan(Cook Islands Māori), Cook Islands](UTC -10)", # クック諸島（ラロトンガ語）, UTC-10
	"15" : u"’ia ora na ’oe [Language: Tahitian, Tahiti](UTC -9)", # タヒチ（タヒチ語）, UTC-9
	"16" : u"Hello [Language: English, United States of America](UTC -8)", # アメリカ（英語）UTC-8
	"17" : u"Bonjour. [Language: French, Canada](UTC -7)", # カナダ（フランス語）, UTC-7
	"18" : u"Allillanmi. [Language: Quechua, Republic of Ecuador](UTC -6)", # エクアドル（ケチュア語）, UTC-6
	"19" : u"kamisaki [Language: Aymara, Republic of Peru](UTC -5)", # ペルー（アイマラ語）, UTC-5
	"20" : u"Boa tarde. [Language: Portuguese, Federative Republic of Brazil](UTC -4)", # ブラジル（ポルトガル語）, UTC-4
	"21" : u"fawaka? [Language: Suriname, Republic of Suriname](UTC -3)", # スリナム（スラナン語）, UTC-3
	"22" : u"Buenas tardes [Language: español, Republic Argentina](UTC -2)", # アルゼンチン（スペイン語）, UTC-2
	"23" : u'God dag. [Language: Greenlandic Inuktitut, Greenland](UTC -1)', # グリーンランド語, UTC-1
}

# get time
def am7Greeting():
	import datetime
	d = datetime.datetime.utcnow()
	utc = (7 - d.hour) % 24
	return TIMEZONE_TABLE[str(utc)]

