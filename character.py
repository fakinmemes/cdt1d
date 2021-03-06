class hero:

	def stats(self):
		statistics = {
			"name":"Hero",
			"maxhp":20,
			"hp":20,
			"minatk":1,
			"maxatk":5,
			"block":0,
			"tempbonus":0,
			"days":0,
			"eq":{
				"Weapon":"Basic Sword",
				"Shield":"None",
				"Armor":"None"
			},
			"inventory":{
				"Berry":{"count":5,"eline":"You regain 5 HP!","effect":"self.pstats['hp'] += 5"},
				"Bomb":{"count":1,"eline":"Your next attack does 5 extra damage!","effect":"self.pstats['tempbonus']+=5"}
				}
			}
		return statistics