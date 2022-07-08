# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 21:18:12 2021
@author: TheVino
IDEA= Show all your masteries, to provide information which champion to play focus on grinding.
my id: l1LFPfM6jg4KvIchL79xBr1NA-oZrDdAbD6YZuf5UzvU
my API: RGAPI-2cb4b14f-2282-49a9-8152-8043346ceedf 
"""
import cassiopeia as cass
from cassiopeia import Summoner #, Champion, ChampionMastery

def getAPI_key():   #informs the request, which API is being used
    f = open("./api_key.txt", "r")
    return f.read()

def my_region():    #defines which region are we searching
    region="BR"
    return region

def print_champion_mastery_intro(cms, cm):    #prints static information aboout my top mastery champion :D
    # Name: Quinn Lee Spree
    # ID: 21359666
    # Account ID: 34718348
    print("Account Name: {}".format(me.name))
    print("Champion Name: {}".format(mvp))
    print("Champion ID: {}".format(cm.champion.id))
    print("Mastery points: {}".format(cm.points))
    print("Mastery Level: {}".format(cm.level))
    print("Points until next level: {}".format(cm.points_until_next_level))
    return

def mastery_level_number(summoner,level,leng):
    print("\n{} has mastery level {} on {} champions:".format(summoner,level,leng))
    return

def tokens_count(level):
    pro = cms.filter(lambda cm: cm.level == level)
    xes = [cm.champion.name for cm in pro]
    yes = [cm.tokens for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} has {} S token(s) already".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return

def print_m7(cms,cm):
    pro = cms.filter(lambda cm: cm.level == 7)
    level = 7
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.points for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{}: {} mastery points".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return 

def print_m6(cms,cm):
    level = 6
    pro = cms.filter(lambda cm: cm.level == level)
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.tokens for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} has {} S token(s) already".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return

def print_m5(cms,cm):
    pro = cms.filter(lambda cm: cm.level == 5)
    level = 5
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.tokens for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} has {} S token(s) already".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return
    
def print_m4(cms,cm):
    pro = cms.filter(lambda cm: cm.level == 4)
    level = 4
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.points_until_next_level for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} needs {} points for mastery level up".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return

def print_m3(cms,cm):
    pro = cms.filter(lambda cm: cm.level == 3)
    level = 3
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.points_until_next_level for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} needs {} points for mastery level up".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return

def print_m2(cms,cm):
    pro = cms.filter(lambda cm: cm.level == 2)
    level = 2
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.points_until_next_level for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} needs {} points for mastery level up".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return

def print_m1(cms,cm):
    pro = cms.filter(lambda cm: cm.level == 1)
    level = 1
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.points_until_next_level for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} needs {} points for mastery level up".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return

def print_m0(cms,cm):
    pro = cms.filter(lambda cm: cm.level == 0)
    level = 0
    mastery_level_number(me.name, level, len(pro))
    xes = [cm.champion.name for cm in pro]
    yes = [cm.points_until_next_level for cm in pro]
    xes = xes + yes
    start = 0
    i = 0
    while i < len(yes):
        print("{} needs {} points for mastery level up".format(xes[start+i],xes[start+i+len(yes)]))
        i += 1
    return
    
#%% Main run  
if __name__ == "__main__":
    print("--==RUNNING MASTERY PARSER FOR LOL==--")
    #executes the API 
    api = getAPI_key()
    print (api)
    cass.set_riot_api_key(api) #or replace with your own api key
    
    #var declarations
    me = Summoner(name="Quinn Lee Spree", region=my_region())
    cms = me.champion_masteries
    mvp = cms[0].champion.name
    cm = cass.get_champion_mastery(champion=mvp, summoner=me, region=my_region())
    
    #func calling
    print_champion_mastery_intro(cms, cm)
    print_m7(cms,cm)
    print_m6(cms,cm)
    print_m5(cms,cm)
    print_m4(cms,cm)
    print_m3(cms,cm)
    print_m2(cms,cm)
    print_m1(cms,cm)
    print_m0(cms,cm)
    