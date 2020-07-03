Group Number: 8
Group Members:

  Full Name: Grant McFarlin
  EID: gjm923

  Full Name: Christina Fu
  EID: clf2524

  Full Name: Michael Dang
  EID: mhd523

  Full Name:
  EID:

Strategy Summary:
Heal
  Health is <= The max potential damage of one attack from a zombie
    This will yield the most consistent life-span but at the sacrifice of a few frames of life from a riskier strategy
Move
  We will move around the map in a CW circle close to the edge of the map, this will allow us to hunt zombies
Scan
  We need to keep track of the zombies so we scan after each move and after each attack
    Want an updated scan results
    Scan after each attack to know if the attack killed the zombie or else we will keep attacking a dead zombie
Attack
  If the distance from zombie <= 3 units, we attack
    We want to attack when the zombie is close enough, or else it will be a waste of a turn to attack from a distance (since damage is exponential)
    If there is a zombie close to where we plan to move, attack that one
    Else, attack the closest zombie
