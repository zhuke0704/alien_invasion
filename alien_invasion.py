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

import flask

import sys
import pygame

from settings import Settings
from ship import Ship
from alien import Alien

import game_functions as gf

from pygame.sprite import Group

from game_states import GameStats

from button import Button

from scoreboard import Scoreboard

def run_game():
	#初始化游戏并创建一个屏幕对象
	pygame.init()

	#初始化游戏屏幕
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	
	#显示顶端标签
	pygame.display.set_caption("Alien Invasion")

	#初始化飞船
	ship = Ship(screen,ai_settings)

	#初始化外星人
	#alien = Alien(ai_settings,screen)


	#创建一个用于存储子弹的编组
	bullets = Group()

	#创建一个用于存储外星人的编组
	aliens = Group()
	#创建外星人群
	gf.creat_fleet(ai_settings, screen, aliens,ship) 
	#创建一个用户存储游戏统计信息的实例
	stats = GameStats(ai_settings)

	#创建开始按钮
	play_button = Button(ai_settings, screen, "Play")

	#创建计分板
	scoreboard = Scoreboard(ai_settings,screen,stats)


	#开始游戏主循环
	while True:
		gf.check_events(ship,ai_settings,screen,bullets,stats,play_button,aliens,scoreboard)    #响应外部事件
		if stats.game_active:
			ship.update() 		#根据外部事件调整飞船
			gf.update_bullets(aliens,bullets,ai_settings,screen,ship,stats,scoreboard)  #刷新子弹
			gf.update_alien(ai_settings,aliens,ship,screen,bullets,stats,scoreboard)  #刷新外星人

		gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,scoreboard)	#更新屏幕显示



run_game()


