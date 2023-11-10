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
So this program basically requests all the information (I decided is important) for you to check your mastery in an *easy way*!

## **Goal**
Summoner to check anytime (mostly on Champion select) which character will them play to level up a *non-maxed* mastery.

#####  The only modification you need to made on this first version of the program is on `Summoner.name` and `.region`<sub> lines 17 and 169</sub>


## First you will need to install Cassiopeia:
###### Installation
`pip install cassiopeia` or see [here](http://cassiopeia.readthedocs.io/en/latest/setup.html) for more information.

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

![m1 call](https://i.imgur.com/D9PEkwQ.png)

>--==RUNNING MASTERY PARSER FOR LOL==--
RGAPI-6d44e78d-534b-4ebf-a494-7104c62b0f90
Making call: https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Solareh
Making call: https://ddragon.leagueoflegends.com/realms/br.json
Making call: https://ddragon.leagueoflegends.com/cdn/13.22.1/data/pt_BR/championFull.json
Making call: https://br1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/8Ey_Yfg989rku9qXtOiDP-kRig64Zrqp_kmmXF0PSzQ0f5g

>Account Name: Solareh
Champion Name: Trundle
Champion ID: 48
Mastery points: 271018
Mastery Level: 7
Points until next level: 0

Solareh has mastery level 7 on 3 champions:
Nami: 256004 mastery points
Lulu: 128023 mastery points
Jinx: 83083 mastery points

Solareh has mastery level 6 on 14 champions:
Sona has 2 S token(s) already
Morgana has 2 S token(s) already
Caitlyn has 0 S token(s) already
Lux has 0 S token(s) already
Janna has 0 S token(s) already
Nautilus has 0 S token(s) already
Ahri has 0 S token(s) already
Soraka has 0 S token(s) already
Karma has 0 S token(s) already
Senna has 0 S token(s) already
Ashe has 0 S token(s) already
Miss Fortune has 0 S token(s) already
Rakan has 0 S token(s) already
Tristana has 0 S token(s) already

Solareh has mastery level 5 on 18 champions:
Ziggs has 0 S token(s) already
Annie has 0 S token(s) already
Brand has 0 S token(s) already
Teemo has 0 S token(s) already
Yuumi has 0 S token(s) already
Ezreal has 0 S token(s) already
Zyra has 0 S token(s) already
Amumu has 0 S token(s) already
Kai'Sa has 0 S token(s) already
Xayah has 0 S token(s) already
Kog'Maw has 0 S token(s) already
Braum has 1 S token(s) already
Alistar has 0 S token(s) already
Leona has 0 S token(s) already
Veigar has 0 S token(s) already
Vel'Koz has 0 S token(s) already
Xerath has 0 S token(s) already
Malphite has 0 S token(s) already

Solareh has mastery level 4 on 12 champions:
Irelia needs 562 points for mastery level up
Vayne needs 1206 points for mastery level up
Blitzcrank needs 1375 points for mastery level up
Cho'Gath needs 2606 points for mastery level up
Bardo needs 3085 points for mastery level up
Thresh needs 3193 points for mastery level up
Orianna needs 4876 points for mastery level up
Lillia needs 5924 points for mastery level up
LeBlanc needs 6055 points for mastery level up
Zilean needs 7272 points for mastery level up
Shen needs 8223 points for mastery level up
Syndra needs 8870 points for mastery level up

