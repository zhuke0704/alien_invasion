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

class Bullet(Sprite):
	#飞船发射子弹管理类
	def __init__(self,ai_settings,screen,ship):
		super().__init__()
		self.screen = screen

		#在(0,0)处创建一个表示子弹矩形，再设置位置
		self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		self.y = float(self.rect.y)	#存储用浮点数表示子弹位置

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor

	def update(self):
		#向上移动子弹
		#更新表示子弹位置的小数值
		self.y -= self.speed_factor
		#更新表示子弹的rect的位置
		self.rect.y = self.y

	def draw_bullet(self):
		#在屏幕上绘制子弹
		pygame.draw.rect(self.screen,self.color,self.rect)

		