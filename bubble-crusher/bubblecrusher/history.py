# -*- coding: utf8 -*-
from template import template
from bubble import bubble
from copy import deepcopy

class history(object):
  fields = list()
  xbubbles = list()

  def xbubbles_purge(self):
    self.xbubbles = list()
  
  def fields_purge(self):
    self.fields = list()

  def save_state(self, field, score_total):
    if len(self.fields) > 10:
      del self.fields[0]
    self.fields.append(deepcopy(field))


    
  def create_template(self, height, width):
    #Initialiser les minima et maxima
    min_x = height
    min_y = width
    max_x = 0
    max_y = 0
    color = ''
    for b in self.xbubbles:
      color = b['color']
      if min_x > b['x']:
        min_x = b['x']
      if min_y > b['y']:
        min_y = b['y']
      if max_x < b['x']:
        max_x = b['x']
      if max_y < b['y']:
        max_y = b['y']

    # Projection 
    for b in self.xbubbles:
      b['x'] -= min_x
      b['y'] -= min_y
    temp = template(False, width, height, '', 'blue')

    # Ecriture du template
    for b in self.xbubbles:
      w = bubble()
      w.color = 'blue'
      temp[b['x']][b['y']] = w
    return temp

    

    


    

          
          



    
