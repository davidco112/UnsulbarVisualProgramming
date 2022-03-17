class Hero:
  pass

tigreal = Hero()
lesley = Hero()
eudora = Hero()
#hp = healthpoint
#att = attack
#arm = armour

tigreal.hp = '100'
tigreal.att = '10'
tigreal.arm = '40';

lesley.hp = '100'
lesley.att = '50'
lesley.arm = '20'

eudora.hp = '100'
eudora.att = '30'
eudora.arm = '5'

print(tigreal.__dict__)
