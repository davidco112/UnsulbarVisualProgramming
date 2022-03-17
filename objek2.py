class Hero:
  def __init__(self, inputName, inputHp, inputAtt, inputArm):
    self.name = inputName
    self.hp = inputHp
    self.att = inputAtt
    self.arm = inputArm
tigreal = Hero("tigreal",100,10,40)
lesley = Hero("lesley",100,50,20)
eudora = Hero("eudora",100,30,5)
print(tigreal.__dict__, lesley.__dict__, eudora.__dict__)
