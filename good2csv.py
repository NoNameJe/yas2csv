import json
import os

lanuage_const = 1
type_keyword={
    "flower": ("flower","花"),
    "plume": ("plume","羽毛"),
    "sands": ("sands","沙漏"),
    "goblet": ("goblet","杯"),
    "circlet": ("circlet","头盔")
}
stat_keyword={
    "hp": ("HP", "生命值"),
    "hp_": ("HP%", "生命值百分比"),
    "atk": ("ATK", "攻击力"),
    "atk_": ("ATK%", "攻击力百分比"),
    "def": ("DEF", "防御力"),
    "def_": ("DEF%", "防御力百分比"),
    "eleMas": ("Elemental Mastery", "精通"),
    "enerRech_": ("Energy Recharge", "充能"),
    "heal_": ("Healing Bonus", "治疗"),
    "critRate_": ("CRIT Rate", "暴击率"),
    "critDMG_": ("CRIT DMG", "暴击伤害"),
    "physical_dmg_": ("Physical DMG Bonus", "物伤"),
    "anemo_dmg_": ("Anemo DMG Bonus", "风伤"),
    "geo_dmg_": ("Geo DMG Bonus", "岩伤"),
    "electro_dmg_": ("Electro DMG Bonus", "雷伤"),
    "hydro_dmg_": ("Hydro DMG Bonus", "水伤"),
    "pyro_dmg_": ("Pyro DMG Bonus", "火伤"),
    "cryo_dmg_": ("Cryo DMG Bonus", "冰伤"),
    "dendro_dmg_": ("Dendro DMG Bonus", "草伤")
}

data2='''Adventurer|Adventurer|冒险家
ArchaicPetra|Archaic Petra|悠古的磐岩
Berserker|Berserker|战狂
BlizzardStrayer|Blizzard Strayer|冰风迷途的勇士
BloodstainedChivalry|Bloodstained Chivalry|染血的骑士道
BraveHeart|Brave Heart|勇士之心
CrimsonWitchOfFlames|Crimson Witch of Flames|炽烈的炎之魔女
DeepwoodMemories|Deepwood Memories|深林的记忆
DefendersWill|Defender's Will|守护之心
DesertPavilionChronicle|Desert Pavilion Chronicle|沙上楼阁史话
EchoesOfAnOffering|Echoes of an Offering|来歆余响
EmblemOfSeveredFate|Emblem of Severed Fate|绝缘之旗印
FlowerOfParadiseLost|Flower of Paradise Lost|乐园遗落之花
Gambler|Gambler|赌徒
GildedDreams|Gilded Dreams|饰金之梦
GladiatorsFinale|Gladiator's Finale|角斗士的终幕礼
GoldenTroupe|Golden Troupe|黄金剧团
HeartOfDepth|Heart of Depth|沉沦之心
HuskOfOpulentDreams|Husk of Opulent Dreams|华馆梦醒形骸记
Instructor|Instructor|教官
Lavawalker|Lavawalker|渡过烈火的贤人
LuckyDog|Lucky Dog|幸运儿
MaidenBeloved|Maiden Beloved|被怜爱的少女
MarechausseeHunter|Marechaussee Hunter|逐影猎人
MartialArtist|Martial Artist|武人
NoblesseOblige|Noblesse Oblige|昔日宗室之仪
NymphsDream|Nymph's Dream|水仙之梦
OceanHuedClam|Ocean-Hued Clam|海染砗磲
PaleFlame|Pale Flame|苍白之火
PrayersForDestiny|Prayers for Destiny|祭水之人
PrayersForIllumination|Prayers for Illumination|祭火之人
PrayersForWisdom|Prayers for Wisdom|祭雷之人
PrayersToSpringtime|Prayers to Springtime|祭冰之人
ResolutionOfSojourner|Resolution of Sojourner|行者之心
RetracingBolide|Retracing Bolide|逆飞的流星
Scholar|Scholar|学士
ShimenawasReminiscence|Shimenawa's Reminiscence|追忆之注连
TenacityOfTheMillelith|Tenacity of the Millelith|千岩牢固
TheExile|The Exile|流放者
ThunderingFury|Thundering Fury|如雷的盛怒
Thundersoother|Thundersoother|平息鸣雷的尊者
TinyMiracle|Tiny Miracle|奇迹
TravelingDoctor|Traveling Doctor|游医
VermillionHereafter|Vermillion Hereafter|辰砂往生录
ViridescentVenerer|Viridescent Venerer|翠绿之影
VourukashasGlow|Vourukasha's Glow|花海甘露之光
WanderersTroupe|Wanderer's Troupe|流浪大地的乐团
'''.splitlines()

set_keyword = {}
for d in data2:
    d2 = d.split('|')
    set_keyword.update({d2[0]:(d2[1],d2[2])})

language_dict = stat_keyword.copy()
language_dict.update(set_keyword)
language_dict.update(type_keyword)
def translate(inp):
    return {i["key"]:i["value"] for i in inp}
def translate_language(word):
    if (word in language_dict):
        return language_dict[word][lanuage_const]
    else:
        return word
def makeTextLine(array):
    if (len(array)==0):
        return ""
    elif (len(array)==1):
        return translate_language(str(array[0]))
    else:
        return translate_language(array[0])+","+makeTextLine(array[1:])
key_names=['setKey', 'slotKey', 'level', 'rarity', 'mainStatKey', 'location', 'lock', 'substats']
substat_names=['atk', 'atk_', 'critDMG_', 'critRate_', 'def', 'def_', 'eleMas', 'enerRech_', 'hp', 'hp_']
titles = key_names[:-1]+substat_names

with open("good.json") as f,open("result.csv","w") as f2:
    text=f.read()
    dic=json.loads(text)
    art_array = dic["artifacts"]

    output_texts = []
    #title
    output_texts=output_texts+[makeTextLine(titles)]
    #each line
    for art in art_array:
        dict1 = translate(art["substats"])
        dict2 = art.copy()
        dict2.pop("substats")
        dict2.update(dict1)

        # print(dict2)

        text_arr = []
        for t in titles:
            if (t in dict2):
                text_arr.append(str(dict2[t]))
            else:
                text_arr.append("")
        output_texts.append(makeTextLine(text_arr))
    print(output_texts)
    f2.writelines([text+"\n" for text in output_texts])
