# -*- coding: utf8 -*-
from bubble import bubble

class column(list):

  def __init__(self, random=False, nrow=13):
    #print 'Creation d\'une colonne avec %d lignes' % nrow
    for i in range(1, nrow, 1):
        self.append(bubble(random))

  def __str__(self):
    ''' Affichage de la colonne (debug)'''
    str = '' 
    for i in range(len(self)-1, -1, -1):
      str += self[i].__str__() + '\n'
    return str






