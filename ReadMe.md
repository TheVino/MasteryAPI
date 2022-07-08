# Mastery API

## **Context**
Have you ever thought how many mastery points levels do you have? How many times did you count each of them? Before each game you ran into your collection to check which mastery tokens you need to level up to m7, over and over again?
**Problem Solved!** Now you can navigate through the interface to check your mastery data and collection.

## **Objective**
Easily shows your:
-	Champions with m7, m6, m4 and below
-	How many point you wills need to level up a mastery level (on each Champion)
-	How many tokens do you have for leveling up to m6 or m7 on each Champion
-	And the most important.. your MVP Champion and its mastery points and level 😉



###### Well.. How?
Riot Games provides a powerfull API which contains a lot of data to collect.
So this program basically requests all the information (I decided is important) for you to check your mastery in a *easy way*!

## **Goal**
Summoner to check anytime (mostly on Champion select) which character will them play to level up a *non-maxed* mastery.

#####  The only modification you need to made on this first version of the program is on `Summoner.name` and `.region`<sub> lines 17 and 169</sub>


## First you will need to install Cassiopeia:
######Installation
`pip install cassiopeia` or see here for more information.

#### Python　
	def my_region():    #defines which region are we searching
		region="BR"
		return region
	
	--------------------------------------------------------------------- 
	
	# Main run  
	if __name__ == "__main__":
		print("--==RUNNING MASTERY PARSER FOR LOL==--")
		
		#executes the API 
		api = getAPI_key()
		print (api)
		cass.set_riot_api_key(api) #or replace with your own api key

		#var declarations
		me = Summoner(name="Quinn Lee Spree", region=my_region())
		[...]

		#func calling
		[...]



### Example
>--==RUNNING MASTERY PARSER FOR LOL==--
RGAPI-2cb4b14f-2282-49a9-8152-8043346ceedf
Making call: https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Quinn%20Lee%20Spree
Making call: https://ddragon.leagueoflegends.com/realms/br.json
Making call: https://ddragon.leagueoflegends.com/cdn/12.12.1/data/pt_BR/championFull.json
Making call: https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/l1LFPfM6jg4KvIchL79xBr1NA-oZrDdAbD6YZuf5UzvU

>Account Name: Quinn Lee Spree
Champion Name: Trundle
Champion ID: 48
Mastery points: 271018
Mastery Level: 7
Points until next level: 0

>Quinn Lee Spree has mastery level 7 on 46 champions:
Trundle: 271018 mastery points
Quinn: 187929 mastery points
Shen: 166131 mastery points
Yorick: 106707 mastery points
Sejuani: 89957 mastery points
Maokai: 81818 mastery points
Irelia: 72077 mastery points
Syndra: 66092 mastery points
Taric: 58172 mastery points
Zac: 56897 mastery points
Nunu e Willump: 53934 mastery points
Ezreal: 53555 mastery points
Sona: 53501 mastery points
Sion: 53226 mastery points
Gragas: 51877 mastery points
Dr. Mundo: 50356 mastery points
Corki: 49136 mastery points
Caitlyn: 47768 mastery points
Sivir: 46720 mastery points
Braum: 46133 mastery points
Udyr: 45512 mastery points
Brand: 45260 mastery points
Lee Sin: 44786 mastery points
Thresh: 44506 mastery points
Vi: 44393 mastery points
Xin Zhao: 43972 mastery points
Orianna: 43913 mastery points
Kassadin: 43576 mastery points
Diana: 41555 mastery points
Varus: 40512 mastery points
Nidalee: 39850 mastery points
Lillia: 39683 mastery points
Hecarim: 38268 mastery points
Lux: 37505 mastery points
Taliyah: 36786 mastery points
Volibear: 35926 mastery points
Amumu: 35588 mastery points
Jinx: 35506 mastery points
Jayce: 35318 mastery points
Tristana: 34146 mastery points
Kai'Sa: 33702 mastery points
Poppy: 33500 mastery points
Galio: 33174 mastery points
Miss Fortune: 32446 mastery points
Kayle: 31638 mastery points
Qiyana: 28671 mastery points

>Quinn Lee Spree has mastery level 6 on 23 champions:
Elise has 3 S token(s) already
Rek'Sai has 2 S token(s) already
Skarner has 3 S token(s) already
Swain has 0 S token(s) already
Nocturne has 2 S token(s) already
Shaco has 0 S token(s) already
Cho'Gath has 2 S token(s) already
Lucian has 3 S token(s) already
Ahri has 0 S token(s) already
Ornn has 2 S token(s) already
Kalista has 3 S token(s) already
Wukong has 0 S token(s) already
Lissandra has 2 S token(s) already
Jax has 1 S token(s) already
Jarvan IV has 0 S token(s) already
Olaf has 0 S token(s) already
Leona has 0 S token(s) already
Twitch has 0 S token(s) already
Gnar has 0 S token(s) already
Karma has 0 S token(s) already
LeBlanc has 0 S token(s) already
Kindred has 0 S token(s) already
Teemo has 0 S token(s) already

>Quinn Lee Spree has mastery level 5 on 12 champions:
Kha'Zix has 2 S token(s) already
Fiora has 2 S token(s) already
Lulu has 0 S token(s) already
Morgana has 1 S token(s) already
Nasus has 1 S token(s) already
Janna has 1 S token(s) already
Renekton has 1 S token(s) already
Aurelion Sol has 0 S token(s) already
Gwen has 0 S token(s) already
Vladimir has 0 S token(s) already
Nautilus has 0 S token(s) already
Nami has 0 S token(s) already

>Quinn Lee Spree has mastery level 4 on 13 champions:
Akali needs 1618 points for mastery level up
Illaoi needs 3977 points for mastery level up
Ziggs needs 5943 points for mastery level up
Kennen needs 6033 points for mastery level up
Blitzcrank needs 6256 points for mastery level up
Garen needs 6419 points for mastery level up
Vayne needs 6458 points for mastery level up
Sylas needs 6788 points for mastery level up
Singed needs 7826 points for mastery level up
Ashe needs 7829 points for mastery level up
Alistar needs 7855 points for mastery level up
Graves needs 8382 points for mastery level up
Camille needs 8960 points for mastery level up

>Quinn Lee Spree has mastery level 3 on 11 champions:
Shyvana needs 73 points for mastery level up
Master Yi needs 575 points for mastery level up
Bardo needs 1394 points for mastery level up
Malphite needs 1761 points for mastery level up
Xayah needs 2303 points for mastery level up
Rammus needs 2660 points for mastery level up
Rell needs 2890 points for mastery level up
Yasuo needs 3202 points for mastery level up
Riven needs 3218 points for mastery level up
Soraka needs 6377 points for mastery level up
Kog'Maw needs 6511 points for mastery level up

>Quinn Lee Spree has mastery level 2 on 24 champions:
Tahm Kench needs 682 points for mastery level up
Sett needs 809 points for mastery level up
Twisted Fate needs 854 points for mastery level up
Tryndamere needs 1040 points for mastery level up
Rakan needs 1044 points for mastery level up
Jhin needs 1102 points for mastery level up
Warwick needs 1798 points for mastery level up
Ivern needs 1876 points for mastery level up
Fiddlesticks needs 2276 points for mastery level up
Ekko needs 2357 points for mastery level up
Annie needs 2583 points for mastery level up
Karthus needs 2849 points for mastery level up
Vel'Koz needs 3157 points for mastery level up
Zyra needs 3203 points for mastery level up
Draven needs 3299 points for mastery level up
Aatrox needs 3314 points for mastery level up
Zed needs 3315 points for mastery level up
Neeko needs 3560 points for mastery level up
Rumble needs 3630 points for mastery level up
Zoe needs 3651 points for mastery level up
Kled needs 3704 points for mastery level up
Zilean needs 3722 points for mastery level up
Talon needs 3734 points for mastery level up
Katarina needs 3922 points for mastery level up

>Quinn Lee Spree has mastery level 1 on 26 champions:
Mordekaiser needs 16 points for mastery level up
Senna needs 121 points for mastery level up
Anivia needs 138 points for mastery level up
Rengar needs 332 points for mastery level up
Evelynn needs 368 points for mastery level up
Pyke needs 458 points for mastery level up
Urgot needs 548 points for mastery level up
Samira needs 566 points for mastery level up
Kayn needs 724 points for mastery level up
Yuumi needs 854 points for mastery level up
Xerath needs 884 points for mastery level up
Azir needs 971 points for mastery level up
Veigar needs 982 points for mastery level up
Seraphine needs 999 points for mastery level up
Pantheon needs 1108 points for mastery level up
Darius needs 1325 points for mastery level up
Heimerdinger needs 1345 points for mastery level up
Cassiopeia needs 1345 points for mastery level up
Gangplank needs 1457 points for mastery level up
Malzahar needs 1518 points for mastery level up
Fizz needs 1521 points for mastery level up
Ryze needs 1571 points for mastery level up
Zeri needs 1619 points for mastery level up
Renata Glasc needs 1663 points for mastery level up
Aphelios needs 1672 points for mastery level up
Viego needs 1707 points for mastery level up

>Quinn Lee Spree has mastery level 0 on 5 champions:
Akshan needs 1800 points for mastery level up
Bel'Veth needs 1800 points for mastery level up
Vex needs 1800 points for mastery level up
Viktor needs 1800 points for mastery level up
Yone needs 1800 points for mastery level up

