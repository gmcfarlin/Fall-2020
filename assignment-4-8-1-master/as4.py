import random
import math

from gamelib import *

class ZombieCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)

    def selectBehavior(self):
        prob = random.random()

        # If health is less than 50%, then heal with a 10% probability
        if prob < 0.1 and self.getHealth() < self.getInitHealth() * 0.5:
            return HealEvent(self)

        # Pick a random direction to walk 1 unit (Manhattan distance)
        x_off = random.randint(-1, 1)
        y_off = random.randint(-1, 1)

        # Check the bounds
        map_view = self.getMapView()
        size_x, size_y = map_view.getMapSize()
        x, y = self.getPos()
        if x + x_off < 0 or x + x_off >= size_x:
            x_off = 0
        if y + y_off < 0 or y + y_off >= size_y:
            y_off = 0

        return MoveEvent(self, x + x_off, y + y_off)

class PlayerCharacter(ICharacter):
    def __init__(self, obj_id, health, x, y, map_view):
        ICharacter.__init__(self, obj_id, health, x, y, map_view)
        # You may add any instance attributes you find useful to save information between frames
        # Store moves in a list (none for scan conditional)
        self._moves = [None]
        # Initial direction of player
        self._dir = 'br'
    def selectBehavior(self):
        # get current pos and potential new pos
        my_x, my_y = self.getPos()
        size_x, size_y = self.getMapView().getMapSize()

        # Switch orientation if you're going to hit the edge
        if self._dir == 'br' and my_x + 3 >= size_x and my_y + 3 >= size_y:
            self._dir = 'tl'
        elif self._dir == 'tl' and my_x - 3 < 0 and my_y - 3 < 0:
            self._dir = 'br'

        # Move towards the bottom right of the map (+x then +y)
        if self._dir == 'br':
            new_x = my_x + 3 if my_x + 3 <= size_x else my_x
            new_y = my_y + 3 if new_x == my_x else my_y
        # Move towards the top left of the map (-x then -y)
        elif self._dir == 'tl':
            new_x = my_x - 3 if my_x - 3 >= 0 else my_x
            new_y = my_y - 3 if new_x == my_x else my_y
            
        # read scan results to see if any zombies within 3 units
        distances = dict()
        attack = False
        for obj in self.getScanResults():
            target_pos_x, target_pos_y = obj.getPos()
            dist = math.hypot(my_x - target_pos_x, my_y - target_pos_y)
            new_dist = math.hypot(new_x - target_pos_x, new_y - target_pos_y)
            if dist <= 3:
                attack = True   
            distances[obj.getID()] = [dist, new_dist]
        
        # Heal if you could die to one attack
        if self.getHealth() <= self._init_health * 0.37:
            self._moves.append(HealEvent(self))
            return(HealEvent(self))

        # Scan if your last move was to move or attack
        elif type(self._moves[-1]) == type(AttackEvent(self,0)) or type(self._moves[-1]) == type(MoveEvent(self,0,0)):
            self._moves.append(ScanEvent(self))
            return ScanEvent(self)
        
        elif attack == True:
            targetIDs = []
            IDs_list = list(distances.keys())
            dist_list = list(distances.values())
            for value in dist_list:
                if value[0] <= 3 and value[1] <= 3:
                    targetID = IDs_list[dist_list.index(value)]
                else:
                    nearest_dist = min(dist[0] for dist in dist_list)
                    if value[0] == nearest_dist:
                        targetID = IDs_list[dist_list.index(value)]
            
            self._moves.append(AttackEvent(self,targetID))    
            return AttackEvent(self,targetID)
        
        # Otherwise, move around the map counter-clockwise
        else:
            # Store MoveEvent and excecute
            self._moves.append(MoveEvent(self, new_x, new_y))
            return MoveEvent(self, new_x, new_y)
        
