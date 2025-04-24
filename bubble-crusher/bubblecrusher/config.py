# -*- coding: utf8 -*-

import ConfigParser
import os
import inspect
from highscores import highscores

home=os.path.expanduser('~')
template = '''[highscores]
classic_small = 0
classic_medium = 0
classic_large = 0
classic_extra_large = 0
chillout_small = 0
chillout_medium = 0
chillout_large = 0
chillout_extra_large = 0

[general]
game = classic
type = 'colored'
size = small
width = 8
height = 10'''


class config():
  type = 'colored'
  height = 13
  width = 10
  game = 'classic'
  size = 'medium'
  small_classic=0
  small_chillout=0
  medium_classic=0
  medium_chillout=0
  large_classic=0
  large_chillout=0
  extra_large_classic=0
  extra_large_chillout=0
  highscores = None


  def __init__(self):
    #print "config __init__"
    if os.path.exists(home + '/.bubblecrusher') == False:
      #print "create dir"
      os.mkdir(home + '/.bubblecrusher/')
    if os.path.exists(home + '/.bubblecrusher/bubble.cfg') == False:
      #print "create config file"
      file = open(home + '/.bubblecrusher/bubble.cfg', 'w+')
      file.write(template)
      file.close()

    self.highscores = highscores()
    c = ConfigParser.ConfigParser()
    c.read(home + '/.bubblecrusher/bubble.cfg')
    try:
      if c.get('general', 'game'):
        self.game = c.get('general', 'game')
      if c.get('general', 'type'):
        self.type = c.get('general', 'type')
      if c.get('general', 'size'):
        self.size = c.get('general', 'size')
      if c.getint('general', 'height'):
        self.height = c.getint('general', 'height')
      if c.getint('general', 'width'):
        self.width = c.getint('general', 'width')
      for type in ['classic', 'chillout']:
        for size in ['small', 'medium', 'large', 'extra_large']:
          if c.get('highscores', '%s_%s' %(type, size)):
            self.highscores[type][size] = c.getint('highscores', '%s_%s' % (type, size))
    except:
      print 'erreur de parsing (bubble.cfg)'

  def save_highscore(self, score):
    if self.highscores[self.game][self.size] < score:
      self.highscores[self.game][self.size] = score
    else:
      print "else "


  def __str__(self):
    ''' Affichage de la config actuelle'''
    str = '[general]\n'
    str += 'game : %s\n' % self.game
    str += 'type : %s\n' % self.type
    str += 'size : %s\n' % self.size
    str += 'height : %d\n' % self.height
    str += 'width : %d\n\n' % self.width
    str += '[highscores]\n'
    str += '%s' % self.highscores
    return str

  def get_highscore(self):
    return self.highscores[self.game][self.size]

  def write(self):
    config = ConfigParser.RawConfigParser()
    config.add_section('highscores')
    for type in ['classic', 'chillout']:
      for size in ['small', 'medium', 'large', 'extra_large']:
        config.set('highscores', '%s_%s' % (type, size),  self.highscores[type][size])
    
    config.add_section('general')
    config.set('general', 'game', self.game)
    config.set('general', 'type', self.type)
    config.set('general', 'size', self.size)
    config.set('general', 'width', self.width)
    config.set('general', 'height', self.height)
    configfile = open(home + '/.bubblecrusher/bubble.cfg', 'w+')
    config.write(configfile)


c = config()
print c
c.write()
      
