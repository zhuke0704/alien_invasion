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
class Ship(Sprite):
	#初始化飞船，并在指定位置绘制飞船,screen为飞船指定位置
	def __init__(self,screen,ai_settings):
		super().__init__()
	 	#获取飞船的surface对象
		self.image = pygame.image.load('images/ship.bmp')
		self.screen = screen
		self.ai_settings = ai_settings

	 	#获取飞船surface矩形，通过surface矩形确定飞船位置，设置rect变量是为方便blitme绘制飞船	
		self.rect = self.image.get_rect()
 		#获取飞船指定位置的矩形
		self.screen_rect = screen.get_rect()

	 	#设置飞船处于底部居中位置
		self.rect.centerx = self.screen_rect.centerx
		self.rect.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom

		#飞船移动标志
		self.move_right = False
		self.move_left = False
		self.move_up = False
		self.move_down = False

	def blitme(self):
		self.screen.blit(self.image,self.rect)


	def update(self):
		if self.move_right == True:
			if self.rect.right < self.screen_rect.right:
				self.rect.centerx += 1
		elif self.move_left == True:
			if self.rect.left > self.screen_rect.left:
				self.rect.centerx -= 1
		elif self.move_up == True:
			if self.rect.centery  > 20:
				self.rect.centery -= 1
		elif self.move_down == True:
			if self.rect.centery < 780:
				self.rect.centery += 1

	def center_ship(self):
		self.centerx = self.screen_rect.centerx
		self.centery = self.screen_rect.centery
		self.rect.bottom = self.screen_rect.bottom
		