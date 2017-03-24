#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  δ����.py
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
	#��ʼ����Ϸ������һ����Ļ����
	pygame.init()

	#��ʼ����Ϸ��Ļ
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	
	#��ʾ���˱�ǩ
	pygame.display.set_caption("Alien Invasion")

	#��ʼ���ɴ�
	ship = Ship(screen,ai_settings)

	#��ʼ��������
	#alien = Alien(ai_settings,screen)


	#����һ�����ڴ洢�ӵ��ı���
	bullets = Group()

	#����һ�����ڴ洢�����˵ı���
	aliens = Group()
	#����������Ⱥ
	gf.creat_fleet(ai_settings, screen, aliens,ship) 
	#����һ���û��洢��Ϸͳ����Ϣ��ʵ��
	stats = GameStats(ai_settings)

	#������ʼ��ť
	play_button = Button(ai_settings, screen, "Play")

	#�����Ʒְ�
	scoreboard = Scoreboard(ai_settings,screen,stats)


	#��ʼ��Ϸ��ѭ��
	while True:
		gf.check_events(ship,ai_settings,screen,bullets,stats,play_button,aliens,scoreboard)    #��Ӧ�ⲿ�¼�
		if stats.game_active:
			ship.update() 		#�����ⲿ�¼������ɴ�
			gf.update_bullets(aliens,bullets,ai_settings,screen,ship,stats,scoreboard)  #ˢ���ӵ�
			gf.update_alien(ai_settings,aliens,ship,screen,bullets,stats,scoreboard)  #ˢ��������

		gf.update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,scoreboard)	#������Ļ��ʾ



run_game()


