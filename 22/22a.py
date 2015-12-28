from collections import defaultdict
import random


spells = {'Magic Missile': (53, 4), 'Drain': (73, 2), 'Shield': (113, 7, 6), 'Poison': (173, 3, 6),
          'Recharge': (229, 101, 5)}


class Character():
    def __init__(self, hp, damage, mana=0, name='Player'):
        self.mana_spent = 0
        self.mana = mana
        self.hp = hp
        self.damage = damage
        self.armor = 0
        self.effects = defaultdict(int)
        self.name = name

    def __str__(self):
        return self.name

    def use_spell(self, spell, enemy):
        if spell == 'Magic Missile':
            self.mana -= spells[spell][0]
            self.mana_spent += spells[spell][0]
            enemy.hp -= spells[spell][1]
        elif spell == 'Drain':
            self.mana -= spells[spell][0]
            self.mana_spent += spells[spell][0]
            enemy.hp -= spells[spell][1]
            self.hp += spells[spell][1]
        elif spell == 'Shield':
            if self.effects['Shield'] == 0:
                self.mana -= spells[spell][0]
                self.mana_spent += spells[spell][0]
                self.effects['Shield'] = spells[spell][2]
        elif spell == 'Poison':
            if enemy.effects['Poison'] == 0:
                self.mana -= spells[spell][0]
                self.mana_spent += spells[spell][0]
                enemy.effects['Poison'] = spells[spell][2]
        elif spell == 'Recharge':
            if self.effects['Recharge'] == 0:
                self.mana -= spells[spell][0]
                self.mana_spent += spells[spell][0]
                self.effects['Recharge'] = spells[spell][2]
            else:
                #print "%s casted %s, but it is already active!" % (self, spell)
                pass

    def apply_effects(self):
        for eff in self.effects:
            if self.effects[eff] > 0:
                if eff == 'Shield':
                    self.armor = spells[eff][1]
                    self.effects[eff] -= 1
                    #print "%s provides %s armour to %s! Timer now %s" % (eff, spells[eff][1], self, self.effects[eff])
                elif eff == 'Poison':
                    self.hp -= spells[eff][1]
                    self.effects[eff] -= 1
                    #print "%s deals %s damage to %s! Timer now %s" % (eff, spells[eff][1], self, self.effects[eff])
                elif eff == 'Recharge':
                    self.mana += spells[eff][1]
                    self.effects[eff] -= 1
                    #print "%s provides %s mana to %s! Timer now %s" % (eff, spells[eff][1], self, self.effects[eff])
            else:
                if eff == 'Shield':
                    self.armor = 0
                    #print "%s has run out!" % eff

    def attack(self, defender, action='Melee'):
        #print '\n--- %s attacks! ---' % self


        self.apply_effects()
        if self.hp <= 0:
            return

        defender.apply_effects()
        if defender.hp <= 0:
            return

        #print '%s has %s hitpoint, %s armour, %s mana' % (self, self.hp, self.armor, self.mana)
        #print '%s has %s hitpoint, %s armour, %s mana' % (defender, defender.hp, defender.armor, defender.mana)


        if action != 'Melee':
            #print '%s cast %s' % (self, action)
            self.use_spell(action, defender)

        else:
            damage = max(self.damage - defender.armor, 1)
            defender.hp -= damage
            #print "%s takes %s damage!" % (defender, damage)



results = set()

for n in range(10000000):
    boss = Character(71, 10, name='Boss')
    player = Character(50, 0, 500)
    lose = False

    while player.hp > 0 and boss.hp > 0:
        spell = random.choice(spells.keys())

        try:
            if min(results) < spells[spell][0]:
                lose = True
                break
        except ValueError:
            pass

        if player.effects[spell] > 1 or boss.effects[spell] > 1:
            continue
        if player.mana < spells[spell][0]:
            lose = True
            break

        player.attack(boss, spell)
        if boss.hp <= 0:
            break
        boss.attack(player)
        if player.hp <= 0:
            lose = True
            break

    if player.hp > boss.hp < 1 and not lose:
        results.add(player.mana_spent)

print min(results)