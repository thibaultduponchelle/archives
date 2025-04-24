#!/usr/bin/python

import gtk
import glib
import pango
import math
import cairo
import os
import inspect


bubble_size = 30

class interface(gtk.Window):

  f = None        # The field
  history = None  # The history (undo + score + other stuff)
  cr = None       # Cairo surface/context
  cr2 = None      # Cairo surface/context
  darea = None    # Drawing area
  timer = False   # A boolean for the timer activation
  old_score = 0   # A score to nicely print score animation
  boum_alpha = 1  
  bonus_y = 30    
  w_width = 0     # Width of the darea
  w_height = 0    # Height of the darea
  timer_counter = 30  # A counter to always adjust the time for animation
  c = None        # Config object
  end = False     # A boolean to know if game is finished
  
  def __init__(self):
    super(interface, self).__init__()

  def create_game(self):
    self.end = False
    self.c = config()
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.old_score = 0
    self.history = history()
    self.history.save_state(self.f, self.f.p)
    
  def menu_item_replay(self, widget, event):
    self.history.fields_purge()
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.end = False
    self.old_score = 0
    self.queue_draw()


  def menu_item_new_classic(self, widget, event):
    self.history.fields_purge()
    self.c.game = 'classic'
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.old_score = 0
    self.end = False
    self.queue_draw()


  def menu_item_new_chillout(self, widget, event):
    self.history.fields_purge()
    self.c.game = 'chillout'
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.old_score = 0
    self.end = False
    self.queue_draw()

  def resize_window(self):
    self.history.fields_purge()
    self.w_width = self.c.width * bubble_size + 5
    self.w_height = (self.c.height + 2) * bubble_size +30
    self.set_size_request(self.w_width, self.w_height)

  def menu_item_about(self, widget, event):
    dlg = gtk.AboutDialog()
    dlg.set_name("Bubble Crusher")
    dlg.set_version("0.9")
    dlg.set_website("http://www.sourceforge.net/p/bubblecrusher/")
    dlg.set_website_label("Official Website")
    authors = list()
    authors.append("Duponchelle Thibault <thibault.duponchelle@gmail.com>")
    dlg.set_authors(authors)
    mylogo = gtk.gdk.pixbuf_new_from_file("bubblecrusher/data/pixs/logo/logo.png")
    dlg.set_logo(mylogo)
    dlg.run()
    dlg.destroy()

  def menu_item_size_small(self, widget, event):
    self.history.fields_purge()
    self.c.width = 8
    self.c.height = 10
    self.c.size = 'small'
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.old_score = 0
    self.end = False
    self.resize_window()
    self.queue_draw()

  def menu_item_size_medium(self, widget, event):
    self.history.fields_purge()
    self.c.width = 10
    self.c.height = 13
    self.c.size = 'medium'
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.old_score = 0
    self.end = False
    self.resize_window()
    self.queue_draw()

  def menu_item_size_large(self, widget, event):
    self.history.fields_purge()
    self.c.width = 12
    self.c.height = 15
    self.c.size = 'large'
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.old_score = 0
    self.end = False
    self.resize_window()
    self.queue_draw()

  def menu_item_size_extra_large(self, widget, event):
    self.history.fields_purge()
    self.c.width = 16
    self.c.height = 19
    self.c.size = 'extra_large'
    self.f = field(True, self.c.width, self.c.height, self.c.game)
    self.old_score = 0
    self.end = False
    self.resize_window()
    self.queue_draw()
  
  def quit(self, widget, event):
    self.c.write()
    gtk.main_quit()
    exit(0)


  def helpmenu(self):
    helpmenu = gtk.Menu()
    about = gtk.MenuItem("About")
    about.connect("activate", self.menu_item_about, 'About')
    helpmenu.append(about)
    root = gtk.MenuItem('?')
    root.set_submenu(helpmenu)
    root.show()
    return root
  
  def menu(self):
    menu = gtk.Menu()
    replay = gtk.MenuItem('Replay')
    new = gtk.MenuItem('New')

    newmenu = gtk.Menu()
    classic = gtk.RadioMenuItem(None, "Classic", False)
    chillout = gtk.RadioMenuItem(classic, "Chill Out", False)
    if  self.c.game == "classic":
      classic.set_active(True)
    elif self.c.game == "chillout":
      chillout.set_active(True)
    newmenu.append(classic)
    newmenu.append(chillout)
    new.set_submenu(newmenu)
    size = gtk.MenuItem("Size")
    small = gtk.RadioMenuItem(None, "Small", False)
    medium = gtk.RadioMenuItem(small, "Medium", False)
    large = gtk.RadioMenuItem(small, "Large", False)
    extralarge = gtk.RadioMenuItem(small, "Extra large", False)
    if  self.c.size == "small":
      small.set_active(True)
    elif self.c.size == "medium":
      medium.set_active(True)
    elif self.c.size == "large":
      large.set_active(True)
    elif self.c.size == "extralarge":
      extralarge.set_active(True)
    sizemenu = gtk.Menu() 
    sizemenu.append(small)
    sizemenu.append(medium)
    sizemenu.append(large)
    sizemenu.append(extralarge)
    size.set_submenu(sizemenu)

    quit = gtk.MenuItem('Quit')
    menu.append(replay)
    menu.append(new)
    menu.append(size)
    menu.append(quit)
    replay.connect("activate", self.menu_item_replay, 'Replay')
    classic.connect("activate", self.menu_item_new_classic, 'Classic')
    chillout.connect("activate", self.menu_item_new_chillout, 'ChillOut')
    small.connect("activate", self.menu_item_size_small, 'Small')
    medium.connect("activate", self.menu_item_size_medium, 'Medium')
    large.connect("activate", self.menu_item_size_large, 'Large')
    extralarge.connect("activate", self.menu_item_size_extra_large, 'Large')
    quit.connect("activate", self.quit, 'Quit')
    replay.show()
    root = gtk.MenuItem('Game')
    root.set_submenu(menu)
    root.show()
    return root

  def button_press_event(self, widget, event):
    if self.end == True:
      if (event.y >  self.w_height/1.5 - 50)and(event.y < self.w_height/1.5 + 50):
        bub.create_game()
        self.end = False
        self.queue_draw()
    else:
      if (event.x > self.f.width * bubble_size - 50)and(event.x < self.f.width * bubble_size):
        if (event.y>0)and(event.y<50):
            #print 'undo !'
            self.f = field.undo_field(self.history, self.f)
            self.old_score = self.f.score
            self.queue_draw()
            return True

      if self.timer == False: 
        self.old_score = self.f.score
        if event.button == 1:
          x = int(event.x / bubble_size) 
          
          y = self.f.height + 1 - int(event.y / bubble_size)
          if  y >= self.c.height:
            #print "Out of board"
            #print "x : %d  y : %d   (%d)" %(x, y, self.c.height)
            return True
          if self.f.has_neighbors(int(x), int(y), self.f[x][y].color):
            self.history.save_state(self.f, self.f.p)
            self.history.xbubbles_purge()
            self.f.explode(int(x),int(y), self.history)
            #print self.f
            self.f.create_history_template(self.history)
            self.launch_timer()
    return True

  def launch_timer(self):
    self.timer = True
    self.alpha = 1
    self.timer_counter = 30
    glib.timeout_add(10, self.on_timer) 

    

  def print_score(self, pt=None):
    self.cr.set_source_rgb(1, 1, 1)
    self.cr.select_font_face("Georgia", cairo.FONT_SLANT_NORMAL, 
    cairo.FONT_WEIGHT_BOLD)
    self.cr.set_font_size(16)
    self.cr.move_to(self.f.width/2 * bubble_size - 50, 1 * bubble_size/1.5 )
    if pt != None:
      self.cr.show_text('Score : %d  '% pt)
    else:
      self.cr.show_text('Score : %d  '% self.f.score)
  
  def print_bonus(self):
    if self.timer == True:
      self.cr.set_source_rgb(0.2, 0.2, 0.2)
      self.cr.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
      cairo.FONT_WEIGHT_BOLD)
      self.cr.set_font_size(45)
      self.cr.move_to(self.f.width/2 * bubble_size - 50, (self.f.height/2 * bubble_size) + self.bonus_y)
      if self.bonus_y > 0:
        self.bonus_y -= 1
      if self.f.p.current_coeff == 0:
        if self.f.p.current_pt > 0: # On ne va pas afficher 0 quand meme :)
          self.cr.show_text(' +%d'% self.f.p.current_pt)
      else:
        self.cr.show_text('%dx%d'% (self.f.p.current_coeff, self.f.p.current_pt))
    else:
      self.bonus_y = 30


  def print_bubbles(self):
    # Affichage des bulles
    alpha = 0
    # Previously, create a new ImageSurface inside the for loop was really slow for extra_size game mode...
    # Now I create only one time each ImageSurface and just choose which one must be used...
    blue = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/blue_alpha.png') 
    red = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/red_alpha.png') 
    green = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/green_alpha.png') 
    yellow = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/yellow_alpha.png') 
    boum = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/boum_alpha_big.png')
    for j in range(self.f.height-1, -1, -1):
      for i in range(0, len(self.f), 1):
        x = i * bubble_size +5
        y = (self.f.height-j+1)* bubble_size 
        if len(self.f[i]) > j:
          if self.f[i][j].is_boum():
            self.cr.set_source_surface(boum, x - 15, y - 15)
            self.cr.paint_with_alpha(self.alpha)
          else:
            if  self.f[i][j].color == "blue":
              self.cr.set_source_surface(blue, x, y)
            elif  self.f[i][j].color == "red":
              self.cr.set_source_surface(red, x, y)
            elif  self.f[i][j].color == "green":
              self.cr.set_source_surface(green, x, y)
            elif  self.f[i][j].color == "yellow":
              self.cr.set_source_surface(yellow, x, y)
            if self.end == True:
              self.cr.paint_with_alpha(0.2)
            else:
              self.cr.paint_with_alpha(1)
          

  def print_preview_next_line(self):
    if self.f.next_line != None:
      y = 1* bubble_size 
      for i in range(self.f.width):
        x = i * bubble_size +5
        img = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/%s_alpha.png' % self.f.next_line[i].color) 
        self.cr.move_to(x, y)
        self.cr.set_source_surface(img, x, y)
        self.cr.paint_with_alpha(0.5)

  def print_undo(self):
    img = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/undo.png') 
    self.cr.move_to(self.f.width * bubble_size - 50, 0)
    self.cr.set_source_surface(img, self.f.width * bubble_size - 50, 0)
    self.cr.paint_with_alpha(1)

  def end_game(self):
    self.end = True

  def on_timer(self):
    if not self.timer: return False
    if self.alpha > 0.11:
      self.alpha -= 0.10
      
    if self.old_score >= self.f.score and self.timer_counter <= 0:
      self.f.purge()
      self.f.purge()
      self.f.purge()
      self.f.purge()
      self.f.purge()
      self.f.purge()
      self.f.purge()
      if self.f.can_fill(): 
        self.f.fill()
      else:
        if self.f.is_finished():
          self.end_game()
      self.timer = False
    else:  
      self.timer_counter -= 1
      self.inc_old_score_to_score()
    
    self.queue_draw()
        
    return True
  
  def inc_old_score_to_score(self):
      ''' Increase slowly the score '''
      if self.f.score - self.old_score > 1040:
        self.old_score += 1000
      if self.f.score - self.old_score > 140:
        self.old_score += 100
      elif self.f.score - self.old_score > 40:
        self.old_score += 10
      elif self.f.score - self.old_score > 15:
        self.old_score += 5
      elif self.f.score - self.old_score > 50:
        self.old_score += 2
      elif self.f.score - self.old_score > 0:
        self.old_score += 1


  def print_finished_game_screen(self):
    # Afficher le Game Over
    img = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/font/gameover_alpha.png') 
    #print self.w_width
    #print self.w_height
    self.cr.set_source_surface(img, self.w_width/2 - 100, self.w_height/8)
    self.cr.paint_with_alpha(1)

    # Afficher l'image score
    img = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/font/score_alpha.png') 
    self.cr.set_source_surface(img, self.w_width/2 - 80, self.w_height/2.5)
    self.cr.paint_with_alpha(1)
    
    # Afficher l'image highscore
    img = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/font/highscore_alpha.png') 
    self.cr.set_source_surface(img, self.w_width/2 - 100, self.w_height/2)
    self.cr.paint_with_alpha(1)

    # Afficher l'image retry
    img = cairo.ImageSurface.create_from_png('bubblecrusher/data/pixs/font/retry_alpha.png') 
    self.cr.set_source_surface(img, self.w_width/2 - 100, self.w_height/1.5)
    self.cr.paint_with_alpha(1)

    # Afficher score et highscore
    self.cr.set_source_rgb(0, 0, 0)
    self.cr.select_font_face("Purisa", cairo.FONT_SLANT_NORMAL, 
    cairo.FONT_WEIGHT_BOLD)
    self.cr.set_font_size(23)
    self.cr.move_to(self.w_width/2 + 50, self.w_height/2.5 + 20 )
    self.cr.show_text('%d'% self.f.score)
    self.cr.set_font_size(23)
    self.cr.move_to(self.w_width/2 + 50, self.w_height/2 + 20)
    self.cr.show_text('%d'% self.c.get_highscore())
    self.cr.set_font_size(19)
    
  

  def expose(self, widget, event):
    self.cr = widget.window.cairo_create()
    self.cr.rectangle(event.area.x, event.area.y, event.area.width, event.area.height)
    self.cr.clip()
    self.cr.set_source_rgb(1, 1, 1)
    self.cr.fill()

    self.print_bubbles()
    self.print_preview_next_line()
    self.print_score(self.old_score)
    self.print_undo()
    self.print_bonus()
    if self.end == True:  
      self.c.save_highscore(self.f.score)
      self.print_finished_game_screen()

if __name__ == "__main__":
  from field import field
  from bubble import bubble
  from config import config
  from history import history
else:
  from bubblecrusher.field import field
  from bubblecrusher.bubble import bubble
  from bubblecrusher.config import config
  from bubblecrusher.history import history
bub = interface()
bub.create_game()
bub.set_title("Oo Bubble eXplode oO")
bub.set_position(gtk.WIN_POS_CENTER)
bub.resize_window()
bub.set_resizable(False)

bub.connect("destroy", bub.quit, 'Quit')

bub.darea = gtk.DrawingArea()
bub.darea.connect("expose_event", bub.expose)
bub.darea.connect("button_press_event", bub.button_press_event)
bub.darea.set_events(gtk.gdk.EXPOSURE_MASK | gtk.gdk.BUTTON_PRESS_MASK) 
bub.darea.modify_bg(gtk.STATE_NORMAL, gtk.gdk.Color(50000, 50000, 65535))

bub.darea.show()
hbox = gtk.HBox(True, 0)
vbox = gtk.VBox(False, 0)
bub.add(vbox)
menu_bar = gtk.MenuBar()
menu_bar.append(bub.menu())
menu_bar.append(bub.helpmenu())
menu_bar.show()


vbox.pack_start(menu_bar, False, False, 2)
vbox.pack_end(bub.darea, True, True, 2)
vbox.show()

bub.show_all()


gtk.main()
