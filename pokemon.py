class Pokemon:

    def __init__(self,name, level, type_1 ):

        self.name = name
        self.level = level
        self.type_1 = type_1
        self.maximum_health = level * 10
        self.current_health = self.maximum_health
        self.knock_out = False

    def lose_health(self, points):

        if points > self.current_health:
            self.current_health = 0
            self.knock_out = True
            print("Pokemon has been knocked out")
        
        else:
            self.current_health -= points
            print("Pokemon now has {} health points!".format(self.current_health))

    
    def gain_health(self, points):

        if self.maximum_health != (self.current_health + points):
            self.current_health = self.maximum_health
            print("{} now has {} health points!".format(self.name, self.current_health))
            return
        else:
            print("{} now has {} health points, which is equal to maximum health!".format(self.name, self.current_health))
            self.current_health += points
            return

    def revive(self):

        if self.knock_out == True:
            self.current_health = self.maximum_health
            self.knock_out = False
            print("{} has been revived".format(self.name))
            return
        else:
            return None

    def attack(self, pokemon):

        if self.type_1 != pokemon.type_1:
            if (self.type_1 == "Grass" or self.type_1  == "Fire") and (self.type_1  == "Grass" or self.type_1 == "Fire"):
                if self.type_1 == "Fire":
                    winner = self.name
                    loser = pokemon.name
                    print("{} has beaten {}".format(winner, loser))
                    loser.lose_health(self.level * 2)
                    return
                else:
                    winner = pokemon.name
                    loser = self.name
                    print("{} has beaten {}".format(winner, loser))
                    loser.lose_health(pokemon.level * (1/2))
                    return

            if (self.type_1 == "Grass" or self.type_1  == "Water") and (self.type_1  == "Grass" or self.type_1 == "Water"):
                if self.type_1 == "Grass":
                    winner = self.name
                    loser = pokemon.name
                    print("{} has beaten {}".format(winner, loser))
                    loser.lose_health(self.level * 2)
                    return
                else:
                    winner = pokemon.name
                    loser = self.name
                    print("{} has beaten {}".format(winner, loser))
                    loser.lose_health(pokemon.level * (1/2))
                    return
                
            if (self.type_1 == "Fire" or self.type_1  == "Water") and (self.type_1  == "Fire" or self.type_1 == "Water"):
                if self.type_1 == "Water":
                    winner = self.name
                    loser = pokemon.name
                    print("{} has beaten {}".format(winner, loser))
                    loser.lose_health(self.level * 2)
                    return
                else:
                    winner = pokemon.name
                    loser = self.name
                    print("{} has beaten {}".format(winner, loser))
                    loser.lose_health(pokemon.level * (1/2))
                    return
        
        else:
            if self.level > pokemon.level:
                print("{} has beaten {}".format(self.name, pokemon.name))
                pokemon.lose_health(self.level)
                return
            else:
                print("{} has beaten {}".format(pokemon.name, self.name))
                self.lose_health(pokemon.level)
                return
     

                 



    