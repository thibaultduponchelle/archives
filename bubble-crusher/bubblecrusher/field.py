# -*- coding: utf8 -*-
from bubble import bubble
from column import column
from template import template
from points import points

class field(list):
  width = 0
  height = 0
  score = 0
  filling_counter = -1
  next_line = None
  p = None

  def __init__(self, random=False, width=10, height=13, game='classic'):
    print 'Create a %s game' %game
    self.width = width
    self.height = height
    self.game = game
    for i in range(0, width, 1):
      self.append(column(random, height+1))

  def __str__(self):
    '''Print the board with nice terminal colors'''
    #str = '\t'
    #str += '----------------------------------'
    #str += '\n'
    str = ''
    for j in range(self.height-1, -1, -1):
      str += '\t|  '
      for i in range(0, len(self), 1):
        if len(self[i]) <= j:
          str += bubble().__str__()
        else:
          str += self[i][j].__str__()
      str += '|\n'
    #str += '\t'
    #str += '----------------------------------'
    str += '\n'
    return str

  def __eq__(self, other):
    ''' Compare 2 fields'''
    if len(self) != len(other):
      return False
    else:
      for i in range(0, len(self)-1, 1):
        if len(self[i]) != len(other[i]):
          return False
        else:
          for i in range(0, len(self)-1, 1):
            for j in range(0, len(self[i])-1, 1):
              if(self[i][j].color != other[i][j].color):
                return False
      return True

  def height_needed(self):
    h = 0
    for c in self:
      if len(c) > h:
        h = len(c)
      
    print 'height : %d' %h
    return h
    
  def explode(self, x, y, history):
    ''' Entry point for explosion (boum is recursive)'''
    self.boum(x, y, history)
    self.height_needed()


  def boum(self, x, y, history):
    '''Explose bubble but keep it in the list'''
    if ((len(self)<=x)or(x<0)):
      print 'Can\'t delete the bubble x=%s' %x
    elif ((len(self[x]) <= y)or(y<0)):
      print 'Can\'t delete the bubble y=%s' %y
    else:
      #print 'Explosion of the bubble : x=%d y=%d' %(x,y)
      color = self[x][y].color
      # Test is the bubble has neighbors
      if self.has_neighbors(x, y, color) or len(history.xbubbles) > 0:
        # Test if we can explose the bubble (not already explosed)  
        if self[x][y].boum():
          history.xbubbles.append({'x':x, 'y':y, 'color': self[x][y].color})
        # Recursive !
        for n in self.neighbors(x, y, color):
          if (self[n['x']][n['y']].is_boum() == False)and(n['x'] < len(self))and(n['y']<len(self[n['x']])):
            #print 'Propagation : %d, %d' %(n['x'], n['y'])
            if self.boum(n['x'],n['y'], history):
              history.xbubbles.append({'x':x, 'y':y, 'color': self[n['x']][n['y']].color})


  def purge(self):
    ''' Pop the bubble marked as explosed '''
    for c in self:
      for i in range(len(c)-1,-1, -1):
        if c[i].is_boum():
          c.pop(i)
    for c in self:
      if len(c)==0:
        self.remove(c)


  def can_fill(self):
    ''' Test if two lines are empty on the top'''
    if self.game == 'classic':
      if self.filling_counter == -1: # Premier jet : des que 2 lignes sont vides
        for c in self:
          if len(c) > (self.height-2):
            #print 'Do not generate new line'
            return False
        self.filling_counter = 5
        return True
      else: # Then repeat all the five explosion 
        if self.filling_counter == 0: 
          self.filling_counter = 5
          return True
        else:
          self.filling_counter -= 1
          return False

    elif self.game == 'chillout': # As soon there's a hole we fill it 
      for c in self:
        if len(c) < (self.height):
          return True
      return False

  def fill(self):
    if self.game == 'classic':
      i = 0
      for c in self:
        if self.next_line != None:
          c.append(self.next_line[i])
          i += 1
      ''' Create the next line '''
      self.next_line = list()
      for i in range(0, self.width, 1):
          self.next_line.append(bubble(True))
    else:
      for c in self:
        while len(c) < self.height:
          c.append(bubble(True))


  def neighbors(self, x, y, color):
    ''' Return a list of neighbors '''
    nb = list()
    if (x>0)and(y<len(self[x-1])):
      if(self[x-1][y].color == color):
        nb.append({'x':x-1,'y':y})
    if (x<(len(self)-1))and(y<len(self[x+1])):
      if(self[x+1][y].color == color):
        nb.append({'x':x+1,'y':y})
    if (y>0):
      if(self[x][y-1].color == color):
        nb.append({'x':x,'y':y-1})
    if (y<(len(self[x])-1)):
      if(self[x][y+1].color == color):
        nb.append({'x':x,'y':y+1})
    return nb

  def has_neighbors(self, x, y, color):
    if len(self.neighbors(x, y, color))>0:
      return True
    else:
      return False



  def is_finished(self):
    ''' Test if at least one bubble could be explosed '''
    for i in range(0, len(self)-1, 1):
      for j in range(0, len(self[i])-1, 1):
        #print 'test end with x : %d et y : %d' %(i, j)
        if self.has_neighbors(i, j, self[i][j].color):
          #print 'Find a neighboor (%d,%d)' %(i, j)
          return False
    return True
        
  def create_history_template(self, history):
    ''' Actually this template is used to calculate the bonus and that's all'''
    #print 'Explosed bubbles :' 
    #print self.history.xbubbles
    temp = history.create_template(self.height, self.width)
    n = len(history.xbubbles)
    print temp
    #print 'NNumber of explosed bubbles : %d' % n
    self.p = points(n)
    self.p.bonuses(temp, n)
    self.score += self.p.pt



  @staticmethod
  def undo_field(history, field):
    # Static yeah man :)
    if len(history.fields) > 0:
      field = history.fields.pop()
    return field

    

          
          



    
