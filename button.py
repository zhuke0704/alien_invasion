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

import pygame.font

class Button():
	"""docstring for Button"""
	def __init__(self,ai_settings,screen,msg):
		#初始化按钮属性
		self.screen = screen
		self.screen_rect = screen.get_rect()

		#设置按钮属性
		self.width,self.height = 200,50
		self.button_color = (0,255,0)
		self.text_color = (255,255,255)
		self.font = pygame.font.SysFont(None,48)

		#创建按钮的rect对象，并使其居中
		self.rect = pygame.Rect(0,0,self.width,self.height)
		self.rect.center = self.screen_rect.center

		#按钮只需创建一次
		self.prep_msg(msg)

	def prep_msg(self,msg):
		self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
		self.msg_image_rect = self.msg_image.get_rect()
		self.msg_image_rect.center = self.rect.center

	def draw_button(self):
		self.screen.fill(self.button_color,self.rect)
		self.screen.blit(self.msg_image,self.msg_image_rect)