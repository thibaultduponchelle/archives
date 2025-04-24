# -*- coding: utf8 -*-

class highscores(dict):

  def __init__(self):
    self['classic'] = dict()
    self['chillout'] = dict()
    self['classic']['small'] = 0
    self['classic']['medium'] = 0
    self['classic']['large'] = 0
    self['classic']['extra_large'] = 0
    self['chillout']['small'] = 0
    self['chillout']['medium'] = 0
    self['chillout']['large'] = 0
    self['chillout']['extra_large'] = 0

  def __str__(self):
    str = ''
    for type in ['classic', 'chillout']:
      for size in ['small', 'medium', 'large', 'extra_large']:
        str += '%s_%s = %s\n' %(type, size, self[type][size])

    return str


h = highscores()
print h

