import re
from collections import defaultdict
from itertools import combinations

shop = defaultdict(dict)
with open('shop.txt', 'r') as shopfile:
    for line in shopfile:
        if line.startswith('Weapons'):
            category = 'Weapons'
        elif line.startswith('Armor'):
            category = 'Armor'
        elif line.startswith('Rings'):
            category = 'Rings'

        if line != '\n':
            if not line.startswith(category):
                line = re.sub(r'(\s)\1*', ',', line.strip())
                line = line.replace(',+', '').split(',')
                shop[category][line[0]] = (int(line[1]), int(line[2]), int(line[3]))


# Add options for not buying items
shop['Armor']['None'] = (0, 0, 0)
shop['Rings']['None'] = (0, 0, 0)
shop['Rings']['None2'] = (0, 0, 0)


class Character():
    def __init__(self, hp, damage, armor):
        self.gold_spent = 0
        self.hp = hp
        self.damage = damage
        self.armor = armor
        self.items = {'Weapons': {}, 'Armor': {}, 'Rings': {}}

    def buy(self, category, item_name):
        item_details = shop[category][item_name]
        self.items[category][item_name] = item_details
        self.gold_spent += item_details[0]
        self.damage += item_details[1]
        self.armor += item_details[2]


boss_stats = []
with open('21.txt', 'r') as file:
    for line in file:
        boss_stats.append(line.split(': ')[1].strip())


def fight(player, boss):
    player_damage = player.damage - boss.armor if player.damage - boss.armor > 0 else 1
    boss_damage = boss.damage - player.armor if boss.damage - player.armor > 0 else 1

    while player.hp >= 0 and boss.hp >= 0:
        boss.hp -= player_damage
        if boss.hp <= 0:
            break
        player.hp -= boss_damage

    return 'Win' if boss.hp < player.hp else 'Lose'


gold_for_losses = []
for weapon in shop['Weapons']:
    for armor in shop['Armor']:
        for rings in combinations(shop['Rings'], 2):
            boss = Character(int(boss_stats[0]), int(boss_stats[1]), int(boss_stats[2]))
            player = Character(100, 0, 0)
            
            player.buy('Weapons', weapon)
            player.buy('Armor', armor)
            player.buy('Rings', rings[0])
            player.buy('Rings', rings[1])

            if fight(player, boss) == 'Lose':
                gold_for_losses.append(player.gold_spent)


print max(gold_for_losses)