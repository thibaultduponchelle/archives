# -*- coding: utf8 -*-
from bubble import bubble
from column import column
import field

class template(list):
  nrow = 0
  ncol = 0
  coeff = 1

  def __init__(self, random=True, ncol=10, nrow=13, type='empty', color=''):
    #print 'Creation d\'une liste de %d colonnes' % ncol
    self.nrow = nrow
    self.ncol = ncol
    for i in range(0, ncol, 1):
      self.append(column(random, nrow))
    self.create(type, color)

  def __str__(self):
    '''Affichage de la matrice en couleur'''
    str = ''
    for j in range(12, -1, -1):
      str += '\t|  '
      for i in range(0, len(self), 1):
        if len(self[i]) <= j:
          str += bubble().__str__()
        else:
          str += self[i][j].__str__()
      str += '|\n'
    str += '\n'
    return str

  def __eq__(self, other):
    '''Compare 2 fields en cherchant a savoir s'ils sont equivalent'''
    #print 'Comparaison de 2 field:'
    if len(self) != len(other):
      return False
    else:
      for i in range(0,len(self)-1,1):
        if len(self[i]) != len(other[i]):
          return False
        else:
          for i in range(0,len(self)-1,1):
            for j in range(0,len(self[i])-1,1):
              if(self[i][j].color != other[i][j].color):
                return False
    return True



  def create(self, type, color):
    b = bubble()
    w = bubble()
    b.color = color

    # Squares
    if type=='square2x2':
      self.coeff = 8
      self[0][0] = self[0][1] = self[1][0] = self[1][1] = b
    if type=='square3x3':
      self.coeff = 8
      self[0][0] = self[0][1] = self[0][2] = self[1][0] = self[1][1] = self[1][2] = self[2][0] = self[2][1] = self[2][2] = b 
    if type=='emptysquare3x3':
      self.coeff = 8
      self[0][0] = self[0][1] = self[0][2] = self[1][0] = self[1][2] = self[2][0] = self[2][1] = self[2][2] = b 

    # Cross
    if type=='cross3x3':
      self.coeff = 8
      self[0][1] = self[1][1] = self[2][1] = self[1][0] = self[1][2] = b

    # Rectangles
    if type=='rectangle3x2':
      self.coeff = 8
      self[0][0] = self[0][1] = self[1][0] = self[1][1] = self[2][0] = self[2][1] =  b 
    if type=='rectangle4x3':
      self.coeff = 8
      self[0][0] = self[0][1] = self[0][2] = self[1][0] = self[1][1] = self[1][2] = self[2][0] = self[2][1] = self[2][2] = b 

    # Horizontal lines
    if type=='hline4x1':
      self.coeff = 8
      self[0][0] = self[1][0] = self[2][0] = self[3][0] = b
    if type=='hline5x1':
      self.coeff = 8
      self[0][0] = self[1][0] = self[2][0] = self[3][0] = self[4][0] = b
    if type=='hline6x1':
      self.coeff = 8
      self[0][0] = self[1][0] = self[2][0] = self[3][0] = self[4][0] = self[5][0] = b
    if type=='hline7x1':
      self.coeff = 8
      self[0][0] = self[1][0] = self[2][0] = self[3][0] = self[4][0] = self[5][0] = self[6][0] = b

    # Verical lines
    if type=='vline4x1':
      self.coeff = 8
      self[0][0] = self[0][1] = self[0][2] = self[0][3] = b
    if type=='vline5x1':
      self.coeff = 8
      self[0][0] = self[0][1] = self[0][2] = self[0][3] = self[0][4] = b
    if type=='vline6x1':
      self.coeff = 8
      self[0][0] = self[0][1] = self[0][2] = self[0][3] = self[0][4] = self[0][5] = b
    if type=='vline7x1':
      self.coeff = 8
      self[0][0] = self[0][1] = self[0][2] = self[0][3] = self[0][4] = self[0][5] = self[0][6] = b

    # Des stairs
    if type=='hzstairs3x2':
      self.coeff = 6
      self[0][1] = self[1][1] = self[1][0] = self[2][0] = b
    if type=='hsstairs3x2':
      self.coeff = 6
      self[0][0] = self[1][0] = self[1][1] = self[2][1] = b
    if type=='vsstairs2x3':
      self.coeff = 6
      self[1][0] = self[1][1] = self[0][1] = self[0][2] = b
    if type=='vzstairs2x3':
      self.coeff = 6
      self[0][0] = self[0][1] = self[1][1] = self[1][2] = b
      
    # Fork
    if type=='hupfork3x3': # La version vers le haut
      self.coeff = 6
      self[1][0] = self[1][1] = self[0][1] = self[0][2] = self[2][1] = self[2][2] = b
    if type=='hdownfork3x3': # La version vers le bas
      self.coeff = 6
      self[0][0] = self[0][1] = self[1][1] = self[1][2] = self[2][0] = self[2][1] = b
    if type=='vrightfork3x3': # La version vers la droite
      self.coeff = 6
      self[0][1] = self[1][1] = self[1][0] = self[2][0] = self[1][2] = self[2][2] = b
    if type=='vleftfork3x3': # La version vers la gauche
      self.coeff = 6
      self[0][0] = self[1][0] = self[0][2] = self[1][2] = self[1][1] = self[2][1] = b

    # Corner
    if type=='swcorner3x3':
      self.coeff = 14
      self[0][0] = self[1][0] = self[2][0] = self[0][1] = self[0][2] = self[1][1] = b
    if type=='nwcorner3x3':
      self.coeff = 14
      self[0][0] = self[0][1] = self[0][2] = self[1][1] = self[1][2] = self[2][2] = b
    if type=='secorner3x3':
      self.coeff = 14
      self[0][0] = self[1][0] = self[2][0] = self[1][1] = self[2][1] = self[2][2] = b
    if type=='necorner3x3':
      self.coeff = 14
      self[2][0] = self[2][1] = self[2][2] = self[1][1] = self[1][2] = self[0][2] = b
      
    # Bicubes
    if type=='bicube3x3': # La version fusionnee
      self.coeff = 6
      self[0][1] = self[0][2] = self[1][1] = self[1][2] = self[1][0] = self[1][1] = self[2][0] = self[2][1] = b
    if type=='bicube3x4': # La version collee
      self.coeff = 6
      self[0][2] = self[0][3] = self[1][2] = self[1][3] = self[1][0] = self[1][1] = self[2][0] = self[2][1] = b
      
    # H
    if type=='h3x5':
      self.coeff = 20
      self[0][0] = self[0][1] = self[0][2] = self[0][3] = self[0][4] = self[1][2] = self[2][0] = self[2][1] = self[2][2] = self[2][3] = self[2][4] = b

    # Le L
    if type=='l3x3': # La version classique
      self.coeff = 6
      self[0][0] = self[0][1] = self[0][2] = self[1][0] = self[2][0] = b
    if type=='rl3x3': # Miroir
      self.coeff = 6
      self[0][0] = self[1][0] = self[2][0] = self[2][1] = self[2][2] = b
    if type=='upl3x3': # Version vers le haut
      self.coeff = 6
      self[0][0] = self[0][1] = self[0][2] = self[1][2] = self[2][2] = b
    if type=='rupl3x3': # Version vers le haut et reverse
      self.coeff = 6
      self[2][0] = self[2][1] = self[2][2] = self[1][2] = self[0][2] = b

    # T
    if type=='t3x3':  # La version classique
      self.coeff = 6
      self[1][0] = self[1][1] = self[0][2] = self[1][2] = self[2][2] = b
    if type=='rt3x3': # La version reverse
      self.coeff = 6
      self[0][0] = self[1][0] = self[2][0] = self[1][1] = self[1][2] = b
    if type=='leftt3x3': # Pointe a gauche
      self.coeff = 6
      self[0][1] = self[1][1] = self[2][2] = self[2][1] = self[2][0] = b
    if type=='rightt3x3': # Pointe a droite
      self.coeff = 6
      self[0][0] = self[0][1] = self[0][2] = self[1][1] = self[2][1] = b

    # Gull
    if type=='rightgull2x5' :
      self.coeff = 10
      self[0][0] = self[0][1] = self[0][2] = self[0][3] = self[0][4] = self[1][2] = b
    if type=='leftgull2x5': 
      self.coeff = 10
      self[1][0] = self[1][1] = self[1][2] = self[1][3] = self[1][4] = self[0][2] = b
    if type=='upgull2x5':
      self.coeff = 10
      self[0][0] = self[1][0] = self[2][0] = self[3][0] = self[4][0] = self[2][1] = b
    if type=='downgull2x5': 
      self.coeff = 10
      self[0][1] = self[1][1] = self[2][1] = self[3][1] = self[4][1] = self[2][0] = b
    
    # Camerton
    if type=='upcamerton3x5': # Ouvert en haut
      self.coeff = 20
      self[1][0] = self[1][1] = self[1][2] = self[0][2] = self[0][3] = self[0][4] = self[2][2] = self[2][3] = self[2][4] = b
    if type=='downcamerton3x5': # Ouvert en bas
      self.coeff = 20
      self[0][0] = self[0][1] = self[0][2] = self[1][2] = self[2][2] = self[2][1] = self[2][0] = self[1][3] = self[1][4] = b
    if type=='leftcamerton5x3': # Ouvert a gauche
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[0][2] = self[1][2] = self[2][2] = self[2][1] = self[3][1] = self[4][1] = b
    if type=='rightcamerton5x3': # Ouvert a droite
      self.coeff = 20
      self[0][1] = self[1][1] = self[2][1] = self[2][0] = self[3][0] = self[2][2] = self[3][2] = self[4][0] = self[4][2] = b


    # Wine glass
    if type=='upglass3x5': # Ouvert en haut
      self.coeff = 20
      self[0][0] = self[2][0] = self[1][0] = self[1][1] = self[1][2] = self[0][2] = self[0][3] = self[0][4] = self[2][2] = self[2][3] = self[2][4] = b
    if type=='downglass3x5': # Ouvert en bas
      self.coeff = 20
      self[0][4] = self[2][4] = self[0][0] = self[0][1] = self[0][2] = self[1][2] = self[2][2] = self[2][1] = self[2][0] = self[1][3] = self[1][4] = b
    if type=='leftglass5x3': # Ouvert a gauche
      self.coeff = 20
      self[4][0] = self[4][2] = self[0][0] = self[1][0] = self[2][0] = self[0][2] = self[1][2] = self[2][2] = self[2][1] = self[3][1] = self[4][1] = b
    if type=='rightglass5x3': # Ouvert a droite
      self.coeff = 20
      self[0][0] = self[0][2] = self[0][1] = self[1][1] = self[2][1] = self[2][0] = self[3][0] = self[4][0] = self[2][2] = self[3][2] = self[4][2] = b

    # Numbers !
    if type=='1':
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[1][1] = self[1][2] = self[1][3] = self[1][4] = self[0][3] = b
    if type=='2':
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[0][1] = self[0][2] = self[1][2] = self[2][2] = self[2][3] = self[2][4] = self[1][4] = self[0][4] = b
    if type=='3':
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[2][1] = self[2][2] = self[1][2] = self[2][2] = self[2][3] = self[2][4] = self[1][4] = self[0][4] = b
    if type=='4':
      self.coeff = 20
      self[0][2] = self[0][3] = self[0][4] = self[2][0] = self[2][1] = self[2][2] = self[1][2] = self[2][3] = self[2][4] = self[0][4] = b
    if type=='5':
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[2][1] = self[0][2] = self[1][2] = self[2][2] = self[0][3] = self[2][4] = self[1][4] = self[0][4] = b
    if type=='6':
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[0][1] = self[2][1] = self[0][2] = self[1][2] = self[2][2] = self[0][3] = self[2][4] = self[1][4] = self[0][4] = b
    if type=='8':
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[0][1] = self[2][1] = self[0][2] = self[1][2] = self[2][2] = self[2][3] = self[0][3] = self[2][4] = self[1][4] = self[0][4] = b
    if type=='9':
      self.coeff = 20
      self[0][0] = self[1][0] = self[2][0] = self[2][1] = self[0][2] = self[1][2] = self[2][2] = self[2][3] = self[0][3] = self[2][4] = self[1][4] = self[0][4] = b

    # Big cross
    if type=='bigcross5x5':
      self.coeff = 20
      self[2][0] = self[2][1] = self[2][2] = self[2][1] = self[2][3] = self[2][4] = self[0][2] = self[1][2] = self[3][2] = self[4][2] = b

