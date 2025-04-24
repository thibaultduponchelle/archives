# -*- coding: utf8 -*-

from random import randrange

class bubble():
  color = None

  def __init__(self, random=False):
    ''' Create a bubble '''
    if random==True:
      r = randrange(0, 4, 1)
      if r == 0:
        self.color = 'red'
      elif r == 1:
        self.color = 'green'
      elif r == 2:
        self.color = 'yellow'
      elif r == 3:
        self.color = 'blue'
  
  def is_boum(self):
    ''' Test if explosed '''
    if(self.color == 'red_boum' or self.color == 'yellow_boum' or self.color == 'blue_boum' or self.color == 'green_boum'):
      return True
    else:
      return False

  def boum(self):
    '''Explose the bubble (don't give points, jut explose the bubble ) ''' 
    if self.color == 'boum':
      print 'Erreur, la bulle est deja explosee'
      return False
    else:
      self.color = '%s_boum' % self.color
      return True

  def set_color(self, color=None):
    ''' Set a color to bubble, "boum" means that the bubble is explosed'''
    if ((self.color == 'blue')or(self.color == 'red')or(self.color == 'yellow')or(self.color == 'green')):
      print 'Erreur, la bulle est deja coloree'
    else:
      self.color = color

  def __str__(self):
    ''' Print the bubble with colors '''
    str = ''
    if self.color=='red':
      str += '\033[31m' + '*' + '\033[0m' + '  '
    elif self.color=='green':
      str += '\033[32m' + '*' + '\033[0m' + '  '
    elif self.color=='yellow':
      str += '\033[33m' + '*' + '\033[0m' + '  '
    elif self.color=='blue':
      str += '\033[34m' + '*' + '\033[0m' + '  '
    else:
      str += '.' + '  '
    return str
      
