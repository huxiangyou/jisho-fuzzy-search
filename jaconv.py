#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Convert Chinese Hanzi and Japanese Kanji

Hu Xiangyou
Jan 26, 2023
"""

import zhconv

zh2jaList=str.maketrans({"·":"・","乘":"乗","亂":"乱","亙":"亘","亞":"亜","佔":"占","佛":"仏","來":"来","俁":"俣","俱":"倶","值":"値","假":"仮","傳":"伝","僞":"偽","僱":"雇","價":"価","儉":"倹","兇":"凶","兒":"児","兔":"兎","內":"内","兩":"両","冰":"氷","冱":"冴","剎":"刹","剩":"剰","劍":"剣","劑":"剤","勞":"労","勳":"勲","勵":"励","勸":"勧","勻":"匀","區":"区","卷":"巻","卻":"却","參":"参","吳":"呉","咒":"呪","啞":"唖","單":"単","喻":"喩","嚙":"噛","嚴":"厳","囑":"嘱","囓":"噛","圈":"圏","國":"国","圍":"囲","圓":"円","圖":"図","團":"団","堇":"菫","堯":"尭","填":"塡","增":"増","墮":"堕","墻":"牆","壓":"圧","壘":"塁","壞":"壊","壤":"壌","壯":"壮","壹":"壱","壽":"寿","奧":"奥","妍":"姸","妒":"妬","妝":"粧","妳":"你","姊":"姉","姬":"姫","娛":"娯","孃":"嬢","學":"学","寢":"寝","實":"実","寫":"写","寬":"寛","寶":"宝","將":"将","專":"専","對":"対","屆":"届","屬":"属","峩":"峨","峯":"峰","峽":"峡","嶽":"岳","巖":"岩","巢":"巣","巤":"鼠","帚":"箒","帶":"帯","廄":"厩","廚":"厨","廢":"廃","廣":"広","廳":"庁","彈":"弾","彌":"弥","彎":"弯","彥":"彦","徑":"径","從":"従","徵":"徴","德":"徳","恆":"恒","悅":"悦","悽":"凄","惠":"恵","惡":"悪","惪":"悳","惱":"悩","慘":"惨","應":"応","懷":"懐","戀":"恋","戰":"戦","戲":"戯","戶":"戸","戾":"戻","拂":"払","拔":"抜","拜":"拝","挾":"挟","插":"挿","揔":"惣","揭":"掲","搔":"掻","搖":"揺","搜":"捜","摃":"扛","摠":"惣","擇":"択","擊":"撃","擔":"担","據":"拠","擴":"拡","攜":"携","攝":"摂","攪":"撹","收":"収","攷":"考","效":"効","敕":"勅","敘":"叙","數":"数","斷":"断","晉":"晋","晚":"晩","晝":"昼","晳":"晰","曆":"暦","曉":"暁","曬":"晒","曾":"曽","會":"会","枡":"桝","查":"査","條":"条","棧":"桟","榆":"楡","榨":"搾","榮":"栄","樂":"楽","樓":"楼","樞":"枢","樣":"様","橢":"楕","橫":"横","檜":"桧","檢":"検","櫸":"欅","櫻":"桜","權":"権","歐":"欧","歡":"歓","步":"歩","歲":"歳","歷":"歴","歸":"帰","殘":"残","殼":"殻","毆":"殴","每":"毎","氛":"雰","氣":"気","污":"汚","沒":"没","泛":"汎","涉":"渉","淚":"涙","淨":"浄","淺":"浅","渴":"渇","溉":"漑","溪":"渓","溫":"温","溯":"遡","溼":"湿","滯":"滞","滿":"満","潛":"潜","澀":"渋","澤":"沢","濕":"湿","濟":"済","濱":"浜","濾":"沪","瀧":"滝","瀨":"瀬","灑":"洒","灣":"湾","燈":"灯","燒":"焼","營":"営","爐":"炉","爭":"争","爲":"為","牀":"床","牠":"它","犧":"犠","狀":"状","狹":"狭","獎":"奨","獨":"独","獵":"猟","獸":"獣","獻":"献","瑤":"瑶","瓣":"弁","產":"産","畫":"画","當":"当","疊":"畳","痹":"痺","瘦":"痩","癡":"痴","癢":"痒","發":"発","皋":"皐","皰":"疱","盜":"盗","盡":"尽","碎":"砕","祕":"秘","祿":"禄","禪":"禅","禮":"礼","禰":"祢","禱":"祷","稅":"税","稱":"称","稻":"稲","穎":"頴","穗":"穂","穩":"穏","穰":"穣","窗":"窓","竊":"窃","竝":"並","粹":"粋","糉":"粽","絕":"絶","絲":"糸","經":"経","綠":"緑","綫":"線","緣":"縁","縣":"県","縱":"縦","總":"総","繡":"繍","繩":"縄","繪":"絵","繫":"繋","繼":"継","續":"続","纖":"繊","缺":"欠","罐":"缶","羣":"群","聰":"聡","聲":"声","聽":"聴","肅":"粛","胄":"冑","脣":"唇","脫":"脱","腦":"脳","腳":"脚","膽":"胆","臈":"﨟","臟":"臓","臺":"台","與":"与","舉":"挙","舊":"旧","舍":"舎","舖":"舗","艷":"艶","荔":"茘","莊":"荘","莓":"苺","莖":"茎","萬":"万","蔣":"蒋","蔥":"葱","薰":"薫","藏":"蔵","藝":"芸","藥":"薬","蘆":"芦","處":"処","虛":"虚","號":"号","螢":"蛍","蟆":"蟇","蟲":"虫","蠟":"蝋","蠶":"蚕","蠻":"蛮","衹":"只","裝":"装","裡":"裏","覺":"覚","覽":"覧","觀":"観","觸":"触","說":"説","謠":"謡","證":"証","譯":"訳","譽":"誉","讀":"読","變":"変","讓":"譲","讚":"讃","豎":"竪","豐":"豊","豔":"艶","豫":"予","豬":"猪","貓":"猫","貳":"弐","賣":"売","賴":"頼","贊":"賛","贗":"贋","踐":"践","踴":"踊","蹤":"踪","輕":"軽","轉":"転","辦":"弁","辨":"弁","辭":"辞","辯":"弁","迴":"廻","逬":"迸","遙":"遥","遞":"逓","遲":"遅","邊":"辺","鄉":"郷","鄰":"隣","醉":"酔","醫":"医","醬":"醤","釀":"醸","釋":"釈","釐":"厘","銳":"鋭","錄":"録","錢":"銭","鍊":"錬","鐮":"鎌","鐵":"鉄","鑄":"鋳","鑒":"鑑","鑛":"鉱","閒":"閑","閱":"閲","關":"関","陷":"陥","隨":"随","險":"険","隱":"隠","隸":"隷","雕":"彫","雙":"双","雜":"雑","雞":"鶏","霸":"覇","靈":"霊","靜":"静","韭":"韮","預":"予","頹":"頽","顏":"顔","顛":"顚","顯":"顕","飜":"翻","餘":"余","駡":"罵","騷":"騒","驅":"駆","驗":"験","驛":"駅","髓":"髄","體":"体","髮":"髪","鬥":"闘","鱉":"鼈","鱷":"鰐","鷄":"鶏","鷗":"鴎","鹼":"鹸","鹽":"塩","麥":"麦","麯":"麹","麴":"麹","麵":"麺","黃":"黄","黑":"黒","默":"黙","點":"点","黨":"党","齊":"斉","齋":"斎","齒":"歯","齡":"齢","齧":"噛","龍":"竜","龜":"亀","，":"、",})

ja2zhList=str.maketrans({"、":"，","・":"·","㑒":"僉","㑪":"儕","㨿":"據","䇳":"箋","両":"兩","乗":"乘","亀":"龜","予":"預","亜":"亞","仏":"佛","仮":"假","伜":"倅","伝":"傳","価":"價","倂":"併","値":"值","倶":"俱","倹":"儉","兎":"兔","児":"兒","円":"圓","冑":"胄","冨":"富","冴":"冱","処":"處","剣":"劍","剤":"劑","剰":"剩","剱":"劍","劔":"劍","労":"勞","効":"效","勅":"敕","勛":"勳","勠":"戮","勧":"勸","勲":"勳","単":"單","卽":"即","厳":"嚴","収":"收","吿":"告","呉":"吳","呑":"吞","唖":"啞","喩":"喻","営":"營","噛":"齧","嚢":"囊","団":"團","囲":"圍","図":"圖","圏":"圈","圧":"壓","埜":"野","塁":"壘","塡":"填","塩":"鹽","増":"增","壊":"壞","壌":"壤","壱":"壹","売":"賣","壷":"壺","変":"變","奨":"獎","奬":"獎","妬":"妒","姉":"姊","姫":"姬","姸":"妍","娯":"娛","嬢":"孃","実":"實","寛":"寬","対":"對","専":"專","尙":"尚","尭":"堯","屛":"屏","嶋":"島","巌":"巖","巣":"巢","巻":"卷","帯":"帶","帰":"歸","幷":"并","庁":"廳","広":"廣","廃":"廢","廰":"廳","弁":"辯","弍":"貳","弐":"貳","弾":"彈","彚":"彙","彫":"雕","従":"從","徳":"德","徴":"徵","応":"應","恵":"惠","悩":"惱","悪":"惡","悳":"惪","愼":"慎","懐":"懷","懴":"懺","戦":"戰","戯":"戲","戱":"戲","戸":"戶","戻":"戾","払":"拂","抜":"拔","択":"擇","拝":"拜","拠":"據","拡":"擴","挙":"舉","挿":"插","捜":"搜","掲":"揭","掻":"搔","揷":"插","揺":"搖","摂":"攝","撃":"擊","撹":"攪","擧":"舉","攅":"攢","敍":"敘","敎":"教","斉":"齊","斎":"齋","旣":"既","昿":"曠","晄":"晃","晩":"晚","暁":"曉","暦":"曆","曁":"暨","曽":"曾","枦":"櫨","査":"查","栄":"榮","桜":"櫻","桝":"枡","桟":"棧","梹":"檳","検":"檢","楕":"橢","楡":"榆","楽":"樂","榖":"穀","槇":"槙","様":"樣","槞":"櫳","槪":"概","権":"權","檪":"櫟","欅":"櫸","欠":"缺","歓":"歡","歩":"步","歯":"齒","歳":"歲","歴":"歷","殱":"殲","殻":"殼","毎":"每","気":"氣","氷":"冰","汎":"泛","汚":"污","沢":"澤","浄":"淨","浜":"濱","涙":"淚","涜":"瀆","淸":"清","渇":"渴","済":"濟","渉":"涉","渋":"澀","渓":"溪","渕":"淵","満":"滿","溌":"潑","滝":"瀧","沪":"濾","漑":"溉","潅":"灌","澁":"澀","瀬":"瀨","焔":"焰","焼":"燒","犠":"犧","猟":"獵","獣":"獸","珱":"瓔","甁":"瓶","産":"產","畳":"疊","疂":"疊","痩":"瘦","痺":"痹","発":"發","皐":"皋","県":"縣","眞":"真","砕":"碎","砿":"礦","硏":"研","稲":"稻","穂":"穗","穏":"穩","穣":"穰","窓":"窗","竃":"竈","竜":"龍","竪":"豎","箒":"帚","篭":"籠","籖":"籤","粋":"粹","粛":"肅","粧":"妝","糓":"穀","糸":"絲","絋":"纊","経":"經","絵":"繪","絶":"絕","継":"繼","続":"續","総":"總","緑":"綠","緕":"纃","緖":"緒","縁":"緣","縄":"繩","縦":"縱","繊":"纖","繋":"繫","繍":"繡","纉":"纘","纎":"纖","缶":"罐","翆":"翠","聡":"聰","聴":"聽","脳":"腦","臓":"臟","舎":"舍","舗":"舖","舮":"艫","艶":"豔","芸":"藝","苺":"莓","茘":"荔","荘":"莊","菫":"堇","萠":"萌","蓳":"堇","蔵":"藏","薗":"園","薫":"薰","薬":"藥","蛍":"螢","蝋":"蠟","蝿":"蠅","蟇":"蟆","衞":"衛","褝":"襌","襃":"褒","覇":"霸","覚":"覺","覧":"覽","観":"觀","訳":"譯","証":"證","説":"說","読":"讀","諌":"諫","謡":"謠","譛":"譖","譲":"讓","讃":"讚","豊":"豐","貭":"質","賎":"賤","賛":"贊","贋":"贗","躙":"躪","転":"轉","軣":"轟","軽":"輕","輌":"輛","辺":"邊","逓":"遞","逬":"迸","遅":"遲","遡":"溯","邉":"邊","郞":"郎","郷":"鄉","鄕":"鄉","酔":"醉","醗":"醱","醤":"醬","醸":"釀","釈":"釋","鈩":"鑪","鈬":"鐸","鉱":"鑛","銭":"錢","鋭":"銳","鋳":"鑄","錬":"鍊","録":"錄","鎌":"鐮","鎭":"鎮","鐡":"鐵","閑":"閒","閗":"鬥","関":"關","閲":"閱","闘":"鬥","陥":"陷","険":"險","隠":"隱","隣":"鄰","隷":"隸","雑":"雜","雰":"氛","霊":"靈","靑":"青","靭":"靱","韮":"韭","韲":"齏","頚":"頸","頬":"頰","頴":"穎","頼":"賴","頽":"頹","顔":"顏","顕":"顯","顚":"顛","飮":"飲","餠":"餅","駅":"驛","駆":"驅","駈":"驅","騒":"騷","験":"驗","騨":"驒","髄":"髓","髙":"高","髪":"髮","鬦":"鬥","鬪":"鬥","鯵":"鰺","鰐":"鱷","鰛":"鰮","鴎":"鷗","鴬":"鶯","鶏":"雞","鶫":"鶇","鷆":"鷏","鹸":"鹼","麪":"麵","麪":"麵","黒":"黑","黙":"默","鼡":"鼠","齢":"齡","欄":"欄","廊":"廊","朗":"朗","虜":"虜","殺":"殺","類":"類","隆":"隆","塚":"塚","﨑":"崎","晴":"晴","﨔":"櫸","猪":"豬","益":"益","礼":"禮","神":"神","祥":"祥","福":"福","靖":"靖","精":"精","羽":"羽","﨟":"臈","諸":"諸","逸":"逸","都":"都","飯":"飯","飼":"飼","館":"館","侮":"侮","僧":"僧","免":"免","勉":"勉","勤":"勤","卑":"卑","喝":"喝","嘆":"嘆","器":"器","塀":"塀","墨":"墨","層":"層","悔":"悔","慨":"慨","憎":"憎","懲":"懲","敏":"敏","既":"既","暑":"暑","梅":"梅","海":"海","渚":"渚","漢":"漢","煮":"煮","琢":"琢","碑":"碑","社":"社","祉":"祉","祈":"祈","祐":"祐","祖":"祖","祝":"祝","禍":"禍","禎":"禎","穀":"穀","突":"突","節":"節","練":"練","縉":"縉","繁":"繁","署":"署","者":"者","臭":"臭","著":"著","褐":"褐","視":"視","謁":"謁","謹":"謹","賓":"賓","贈":"贈","逸":"逸","難":"難","響":"響","頻":"頻","𠮟":"叱","𢑥":"彙","𧯇":"豅","𨻫":"隴","𪗱":"齟","𪘂":"齧","𪘚":"齬","𫠚":"齣","兔":"兔","𠈓":"倆","𫝼":"撥","𫝓":"協","𫝚":"囀","𦜝":"臍","㰖":"欖","㰸":"斂","㴞":"滔","䏮":"脇","兪":"俞","嘨":"嘯","噑":"嗥","暭":"暤",})

def convert(text:str,locale:str)->str:
	if locale=='zh2ja':
		return zhconv.convert(text,'zh-hant').translate(zh2jaList)

	if locale=='ja2hant':
		return zhconv.convert(text.translate(ja2zhList),'zh-hant')

	if locale=='ja2hans':
		return zhconv.convert(text.translate(ja2zhList),'zh-hans')