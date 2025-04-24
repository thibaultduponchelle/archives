# -*- coding: utf8 -*-

from template import template
from math import pow

class points():
  pt  = 0
  current_pt = 0
  current_coeff = 0

  def __init__(self, n):
    current_pt = 0
    current_coeff = 0
    self.pt = pow((n - 1), 2)
    self.current_pt = self.pt
    
  

  def __str__(self):
    return 'Nombre de point pour cette action : %d' % self.pt

  def apply_coeff(self, c):
    self.current_coeff = c
    self.current_pt = self.pt
    self.pt *= c

  def bonuses(self, temp, n):
    if n == 4:
      t1 = template(False, temp.ncol, temp.nrow, 'square2x2', 'blue')
      t2 = template(False, temp.ncol, temp.nrow, 'hline4x1', 'blue')
      t3 = template(False, temp.ncol, temp.nrow, 'vline1x4', 'blue')
      t4 = template(False, temp.ncol, temp.nrow, 'hzstairs3x2', 'blue')
      t5 = template(False, temp.ncol, temp.nrow, 'hsstairs3x2', 'blue')
      t6 = template(False, temp.ncol, temp.nrow, 'vsstairs2x3', 'blue')
      t7 = template(False, temp.ncol, temp.nrow, 'vzstairs2x3', 'blue')
      if t1 == temp:
        print 'C\'est un carre !'
        self.apply_coeff(8)
      elif t2 == temp:
        print 'C\'est une ligne !'
        self.apply_coeff(8)
      elif t3 == temp:
        print 'C\'est une ligne !'
        self.apply_coeff(8)
      elif (t4==temp)or(t5==temp)or(t6==temp)or(t7==temp):
        print 'C\'est une stairs !'
        self.apply_coeff(6)
    elif n == 5:
      t8 = template(False, temp.ncol, temp.nrow, 'cross3x3', 'blue')
      t9 = template(False, temp.ncol, temp.nrow, 'hline5x1', 'blue')
      t10 = template(False, temp.ncol, temp.nrow, 'vline1x5', 'blue')
      t11 = template(False, temp.ncol, temp.nrow, 'l3x3', 'blue') 
      t12 = template(False, temp.ncol, temp.nrow, 'rl3x3', 'blue')
      t13 = template(False, temp.ncol, temp.nrow, 'upl3x3', 'blue')
      t14 = template(False, temp.ncol, temp.nrow, 'rupl3x3', 'blue')
      t15 = template(False, temp.ncol, temp.nrow, 't3x3', 'blue')
      t16 = template(False, temp.ncol, temp.nrow, 'rt3x3', 'blue')
      t17 = template(False, temp.ncol, temp.nrow, 'leftt3x3', 'blue')
      t18 = template(False, temp.ncol, temp.nrow, 'rightt3x3', 'blue')
      if t8 == temp:
        print 'C\'est un cross !'
        self.apply_coeff(8)
      elif t9 == temp:
        print 'C\'est un ligne !'
        self.apply_coeff(8)
      elif t10 == temp:
        print 'C\'est un ligne !'
        self.apply_coeff(8)
      elif (t11==temp)or(t12==temp)or(t13==temp)or(t14==temp):
        print 'C\'est un L !'
        self.apply_coeff(6)
      elif (t15==temp)or(t16==temp)or(t17==temp)or(t18==temp):
        print 'C\'est un T !'
        self.apply_coeff(6)

    elif n == 6:
      t19 = template(False, temp.ncol, temp.nrow, 'rectangle3x2', 'blue')
      t20 = template(False, temp.ncol, temp.nrow, 'hupfork3x3', 'blue')
      t21 = template(False, temp.ncol, temp.nrow, 'hdownfork3x3', 'blue')
      t22 = template(False, temp.ncol, temp.nrow, 'vrightfork3x3', 'blue')
      t23 = template(False, temp.ncol, temp.nrow, 'vleftfork3x3', 'blue')
      t24 = template(False, temp.ncol, temp.nrow, 'swcorner3x3', 'blue')
      t25 = template(False, temp.ncol, temp.nrow, 'nwcorner3x3', 'blue')
      t26 = template(False, temp.ncol, temp.nrow, 'secorner3x3', 'blue')
      t27 = template(False, temp.ncol, temp.nrow, 'necorner3x3', 'blue')
      if t19 == temp:
        print 'C\'est un rectangle !'
        self.apply_coeff(8)
      elif (t20==temp)or(t21==temp)or(t22==temp)or(t23==temp):
        print 'C\'est un fork !'
        self.apply_coeff(6)
      elif (t24==temp)or(t25==temp)or(t26==temp)or(t27==temp):
        print 'C\'est un corner !'
        self.apply_coeff(14)
    elif n == 7:
      t28 = template(False, temp.ncol, temp.nrow, 'bicube3x3', 'blue')
      if t28 == temp:
        print 'C\'est un bicube !'
        self.apply_coeff(6)
    elif n >= 8:
      cam1 = template(False, temp.ncol, temp.nrow, 'upcamerton3x5', 'blue')
      cam2 = template(False, temp.ncol, temp.nrow, 'downcamerton3x5', 'blue')
      cam3 = template(False, temp.ncol, temp.nrow, 'leftcamerton5x3', 'blue')
      cam4 = template(False, temp.ncol, temp.nrow, 'rightcamerton5x3', 'blue')
      glass1 = template(False, temp.ncol, temp.nrow, 'upglass3x5', 'blue')
      glass2 = template(False, temp.ncol, temp.nrow, 'downglass3x5', 'blue')
      glass3 = template(False, temp.ncol, temp.nrow, 'leftglass5x3', 'blue')
      glass4 = template(False, temp.ncol, temp.nrow, 'rightglass5x3', 'blue')
      c1 = template(False, temp.ncol, temp.nrow, '1', 'blue')
      c2 = template(False, temp.ncol, temp.nrow, '2', 'blue')
      c3 = template(False, temp.ncol, temp.nrow, '3', 'blue')
      c4 = template(False, temp.ncol, temp.nrow, '4', 'blue')
      c5 = template(False, temp.ncol, temp.nrow, '5', 'blue')
      c6 = template(False, temp.ncol, temp.nrow, '6', 'blue')
      c8 = template(False, temp.ncol, temp.nrow, '8', 'blue')
      c9 = template(False, temp.ncol, temp.nrow, '9', 'blue')
      c10 = template(False, temp.ncol, temp.nrow, 'bigcross5x5', 'blue')
      if (cam1==temp)or(cam2==temp)or(cam3==temp)or(cam4==temp):
        print 'C\'est un camerton !'
        self.apply_coeff(20)
      if (glass1==temp)or(glass2==temp)or(glass3==temp)or(glass4==temp):
        print 'C\'est un wine glass !'
        self.apply_coeff(20)
      elif (c1==temp)or(c2==temp)or(c3==temp)or(c4==temp)or(c5==temp)or(c6==temp)or(c8==temp)or(c9==temp):
        print 'C\'est un chiffre !'
        self.apply_coeff(20)
      elif c10==temp:
        print 'C\'est une big cross !'
        self.apply_coeff(20)
        

      

      
      
      

    

    

          
          



    
