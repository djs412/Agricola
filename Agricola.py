##Agricola Data

class player:

    item_list = ["Fields", "Pastures", "Grain", "Vegetables", "Sheep", "Wild Boar", "Cattle",
             "Unused Spaces", "Fenced Stables", "Clay Hut Rooms", "Stone House Rooms",
             "Family Members", "Points for Cards", "Bonus Points"]
    

    def __init__(self, name):
        self.name = name
        self.score = []

    def __str__(self):
        return "Player {0} has score {1}".format(self.name, self.score)

    def add_score(self, score):
        return self.score.append(score)

    def add_game(self):
        ##Adds a list of scores to self.score
        score = []
        for i in range(14):
            score.append(int(input("What is {0}'s score for {1}?".format(self.name, i))))
        return self.add_score(score)

    def add_mult_games(self):
        ##Loop to facilitate adding multiple games
        while True:
            answer = input("Add another game?")
            if answer == "n":
                break
            self.add_game()

    def delete_last_game(self):
        ##Deletes last game in list
        del self.score[-1]

    def show_totals(self):
        ##Shows totals from all games
        for (j, i) in enumerate(self.score):
            print("{0}'s score for game {1} was {2}".format(self.name, j + 1, sum(i)))

##    def calc_total(self):
##        scores = []
##        for i in self.score:
##            scores.append(sum(i))
##        return scores

    def avg(self):
        ##Calculates average total game score
        total = 0
        for i in self.score:
            for j in i:
                total += int(j)
        avg = total / len(self.score)
        return "{0}'s average over {1} games is {2:.2f}".format(self.name, len(self.score), avg)
            

    def item_avg(self, item):
        ##Calculates average from single item
        item_total = []
        count = 0
        for i in self.score:
            item_total.append(i[item])
            count += 1
        return "{0}'s average points from {1}: {2:.2f}".format(self.name, player.item_list[item], sum(item_total)/count)

    def item_avg_f(self, item):
        item_total = []
        count = 0
        for i in self.score:
            item_total.append(i[item])
            count += 1
        return sum(item_total)/count
        
    def show_item_avgs(self):
        for i in range(14):
            print(self.item_avg(i))

    def save_data(self):
        ##Saves data to a .py file
        ##Converts to str
        newfile = open("/users/dave/documents/players/{0}.py".format(self.name), "w")
        for game in self.score:
            for num in game:
                newfile.write(str(num))
                newfile.write(" ")
            newfile.write("\n")
        
    def load_data(self):
        ##Converts from str to int and loads from .py file
        data = open("/users/dave/documents/players/{0}.py".format(self.name, "r"))
        self.score = []
        while True:
            line = data.readline()
            if len(line) == 0:
                break
            line = line.split()
            intlist = []
            for i in line:
                intlist.append(int(i))
            self.score.append(intlist)

    def show_suite(self):
        print(self.avg())
        print("----------")
        print(self.show_totals())
        print("----------")
        print(self.show_item_avgs())
        return

    def compare_item(self, other, n):
        if self.item_avg_f(n) > other.item_avg_f(n):
            return "{0} averaged {1:.2f} points more than {2} in {3}".format(self.name,
                            self.item_avg_f(n) - other.item_avg_f(n), other.name, player.item_list[n])
        if self.item_avg_f(n) < other.item_avg_f(n):
            
            return "{0} averaged {1:.2f} points more than {2} in {3}".format(other.name,
                            other.item_avg_f(n) - self.item_avg_f(n), self.name, player.item_list[n])
        
    def compare_players(self, other):
        for (j, i) in enumerate(player.item_list):
            print(self.compare_item(other, j))
        
        
                    
        

z = player("Zach")
z.load_data()
d = player("Dave")
d.load_data()
s = player("Seapy")
s.load_data()
a = player("Andrew")
a.load_data()
##print(z.avg())
##print(d.avg())
##print(z.show_totals())
##print(d.show_totals())
##print(d.compare_players(z))

##s.load_data()
##s.add_mult_games()
##print(d)
##d.add_mult_games()
##z.save_data()
##z.show_item_avgs()

##
##print(z.avg())
##
##print(z.item_avg(6))
##
##print(z.show_totals())


##print(z)
##
##print(z.avg())
##
##print(z.show_item_avgs())


