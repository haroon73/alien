import random


class PlayGame:
    """Sample class that user will play game and stop the alien attack"""

    def __init__(self, player_name):
        """Initializing all filed"""
        self.player_name = player_name
        self.points = 0
        self.aliens = ["Zix", "Glorp", "Quib", "Vex", "Blipzor"]
        self.player_life = []
        self.player_hit_points = 0
        self.player_hit_aliens = []

    def alien_attack(self):
        """Generate alien to attacking the earth"""
        aline = random.choice(self.aliens)
        return aline

    def buy_points(self):
        """Player can buy points here to play the game"""
        print(f"Welcome ( {self.player_name} ) to LandBase")
        self.points = int(input(f"Enter your point ( {self.player_name} ) to start the game => "))
        return self.points

    def build_life(self):
        """This function will build armar base on the points of the player"""
        points = self.buy_points()
        for point in range(points):
            self.player_life.append("*")

    def aline_win(self, alien, aline2):
        """Function that handles alien wining"""
        game_point = len(self.player_life)
        if game_point > 0:
            if alien == aline2:
                self.points -= 2

                if game_point < 2:
                    for i in range(game_point):
                        self.player_life.pop()
                        print("Watch for your life")
                        print(self.player_life)
                        print("\n")
                else:
                    for i in range(2):
                        self.player_life.pop()
                    print("Watch for your life")
                    print(self.player_life)
                    print("\n")
        else:
            print("You lost the game")



    def play_the_game(self):
        """The main engine that will play the game"""
        self.build_life()
        print(self.player_life)
        while True:
            if self.points == 0:
                break
            alien_name = self.alien_attack()
            alien_name = alien_name.lower()
            player_fire = input("Enter (Zix, Glorp, Quib, Vex, Blipzor) to fire on alien =>---- ").lower()
            if player_fire == alien_name:
                if player_fire == "zix":
                    print(f"You hit ({alien_name}) and you got 5 points\n")
                    self.player_hit_points += 5
                    self.player_hit_aliens.append(alien_name)
                    life = len(self.player_life)
                    if life < 10:
                        print("You losing your power")
                        print("see your life")
                        print(self.player_life)
                        buy_life = input("Do you want to buy more life y ")
                        if buy_life == "y":
                            if self.player_hit_points != 0:
                                num_life = int(input("How much want to spend from earning points "))
                                for i in range(num_life):
                                    self.player_life.append("*")
                                print(f"You spent {num_life}")
                            else:
                                print(f"Sorry you dont have any points")
                        print("\n")
                    else:
                        print("Keep up ")
                        print(self.player_life)
                        print("\n")
                elif player_fire == "glorp":
                    print(f"You hit ({alien_name}) and you got 4 points\n")
                    self.player_hit_points += 4
                    self.player_hit_aliens.append(alien_name)
                    life = len(self.player_life)
                    if life < 10:
                        print("You losing your power")
                        print("see your life")
                        print(self.player_life)
                        buy_life = input("Do you want to buy more life y ")
                        if buy_life == "y":
                            if self.player_hit_points != 0:
                                num_life = int(input("How much want to spend from earning points "))
                                for i in range(num_life):
                                    self.player_life.append("*")
                                print(f"You spent {num_life}")
                            else:
                                print(f"Sorry you dont have any points")
                        print("\n")
                    else:
                        print("Keep up ")
                        print(self.player_life)
                        print("\n")
                elif player_fire == "quib":
                    print(f"You hit ({alien_name}) and you got 3 points\n")
                    self.player_hit_points += 3
                    self.player_hit_aliens.append(alien_name)
                    life = len(self.player_life)
                    if life < 10:
                        print("You losing your power")
                        print("see your life")
                        print(self.player_life)
                        buy_life = input("Do you want to buy more life y ")
                        if buy_life == "y":
                            if self.player_hit_points != 0:
                                num_life = int(input("How much want to spend from earning points "))
                                for i in range(num_life):
                                    self.player_life.append("*")
                                print(f"You spent {num_life}")
                            else:
                                print(f"Sorry you dont have any points")
                        print("\n")
                    else:
                        print("Keep up ")
                        print(self.player_life)
                        print("\n")
                elif player_fire == "vex":
                    print(f"You hit ({alien_name}) and you got 2 points\n")
                    self.player_hit_points += 2
                    self.player_hit_aliens.append(alien_name)
                    life = len(self.player_life)
                    if life < 10:
                        print("You losing your power")
                        print("see your life")
                        print(self.player_life)
                        buy_life = input("Do you want to buy more life y ")
                        if buy_life == "y":
                            if self.player_hit_points != 0:
                                num_life = int(input("How much want to spend from earning points "))
                                for i in range(num_life):
                                    self.player_life.append("*")
                                print(f"You spent {num_life}")
                            else:
                                print(f"Sorry you dont have any points")
                        print("\n")
                    else:
                        print("Keep up ")
                        print(self.player_life)
                        print("\n")
                elif player_fire == "blipzor":
                    print(f"You hit ({alien_name}) and you got 1 points\n")
                    self.player_hit_points += 1
                    self.player_hit_aliens.append(alien_name)
                    if life < 10:
                        print("You losing your power")
                        print("see your life")
                        print(self.player_life)
                        buy_life = input("Do you want to buy more life y ")
                        if buy_life == "y":
                            if self.player_hit_points != 0:
                                num_life = int(input("How much want to spend from earning points "))
                                for i in range(num_life):
                                    self.player_life.append("*")
                                print(f"You spent {num_life}")
                            else:
                                print(f"Sorry you dont have any points")
                        print("\n")
                    else:
                        print("Keep up ")
                        print(self.player_life)
                        print("\n")
            else:
                print(f"You got attack by ({alien_name}) alien!")
                print("Watch out\n")
                if alien_name == "zix":
                    self.aline_win(alien_name, "zix")
                elif alien_name == "glorp":
                    self.aline_win(alien_name, "glorp")
                elif alien_name == "quib":
                    self.aline_win(alien_name, "quib")
                elif alien_name == "vex":
                    self.aline_win(alien_name, "vex")
                elif alien_name == "blipzor":
                    self.aline_win(alien_name, "blipzor")




game1 = PlayGame("Khan")
game1.play_the_game()


