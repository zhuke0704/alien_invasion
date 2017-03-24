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


class Settings():

    #初次化游戏设置
	def __init__(self):
		#初始化游戏框架
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230,230,230)

		#子弹设置
		self.bullet_width = 3
		self.bullet_height = 5
		self.bullet_color = 60,60,60

		#飞船设置
		self.fleet_direction = 1  #外星人移动方向，1为向右移动
		

		self.ship_limit = 3	#初始化飞船个数


		self.speedup_scale = 1.1

	def initialize_dynamic_settings(self):
		self.bullet_speed_factor = 1
		self.alien_speed_factor = 1
		self.fleet_drop_speed = 10
		self.alien_points = 0

	def increase_speed(self):
		self.bullet_speed_factor *= self.speedup_scale
		self.alien_speed_factor *= self.speedup_scale
		self.fleet_drop_speed *= self.speedup_scale

		
