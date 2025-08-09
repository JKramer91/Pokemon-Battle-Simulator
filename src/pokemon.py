import random

class Pokemon:
    def __init__(self, attributes):
        self.name = attributes["name"]
        self.id = attributes["id"]
        self.stats = attributes["stats"]
        self.moves = attributes["moves"]
        self.max_hp = self.stats["hp"] * 10
        self.current_hp = self.max_hp


    def calculate_damage(self, attacker_atk, defender_def, move_power):
        base_damage = move_power * (attacker_atk / defender_def)
        damage = base_damage * random.uniform(0.85, 1.0)
        
        return max(1, int(damage))
    
    def resolve_move(self, attacker, defender, move):

        if random.random() > (move["accuracy"] / 100):
            return False, 0
        
        dmg = self.calculate_damage(attacker.stats["attack"], defender.stats["defense"], move["power"])
        print(f"{defender.name}s HP before the attack is = {defender.current_hp}")
        print(f"{attacker.name} attacks {defender.name} with {move["name"]}")
        defender.current_hp -= dmg
        print(f"{defender.name}s HP after the attack is = {defender.current_hp}")

    def has_enemy_fainted(self, pokemon):
        if pokemon.current_hp <= 0:
            return True
        return False

