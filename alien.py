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

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	def __init__(self,ai_settings,screen):
		super().__init__()
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.ai_settings = ai_settings

		#获取外星人的surface对象
		self.image = pygame.image.load('images/alien.bmp')

	 	#获取外星人surface矩形，通过surface矩形确定飞船位置，设置rect变量是为方便blitme绘制飞船	
		self.rect = self.image.get_rect()	#默认的get_rect.width和get_rect.heigth应该是屏幕左上方
		#print(self.rect.width,self.rect.height)   打印结果为60,58
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)   #定义该变量是用于在每行中显示每个外星人，并且用于飞船移动

	def blitme(self):
		self.screen.blit(self.image,self.rect)


	def check_edges(self):
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True


	def update(self):
		#self.check_edges()
		self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
		self.rect.x = self.x


		