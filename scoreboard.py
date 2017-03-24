#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  未命名.py
#  
#  Copyright 2017 zhuke <zhuke@ZHUKE-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

import pygame.font
from ship import Ship
from pygame.sprite import Group
class Scoreboard():
	"""docstring for scoreboard"""
	def __init__(self, ai_settings,screen,stats):
		self.ai_settings = ai_settings
		self.screen =screen
		self.screen_rect = self.screen.get_rect()
		self.stats = stats


		self.text_color = (30,30,30)
		self.font = pygame.font.SysFont(None,48)
		#self.rect = pygame.Rect(0,0,self.width,self.height)

		self.prep_score()

		self.prep_ships()

	def prep_score(self):
		#将得分渲染成一幅图像
		rounded_score = int(round(self.stats.score, -1)) 
		score_str = "{:,}".format(rounded_score)  
		#score_str = str(self.stats.score)
		self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.bg_color)

		#将得分放在图像右上方
		self.score_image_rect = self.score_image.get_rect()
		self.score_image_rect.right = self.screen_rect.right - 20
		self.score_image_rect.top = 20

	def draw_score(self):
		#self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.score_image,self.score_image_rect)

		self.ships.draw(self.screen) 

	def prep_ships(self):
		self.ships = Group()
		for ship_number in range(self.stats.ship_left):
			ship = Ship(self.screen,self.ai_settings)
			ship.rect.x = 10 + ship_number * ship.rect.width 
			ship.rect.y = 10
			self.ships.add(ship)
		