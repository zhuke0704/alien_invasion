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

import sys
import pygame

from bullet import Bullet
from alien import Alien

from random import randint
from time import sleep

def check_key_down(ship,event,ai_settings,screen,bullets):
	if event.key == pygame.K_RIGHT:
		ship.move_right = True
	elif event.key == pygame.K_LEFT:
		ship.move_left = True
	if event.key == pygame.K_UP:
		ship.move_up = True
	elif event.key == pygame.K_DOWN:
		ship.move_down = True
	elif event.key == pygame.K_SPACE:
		new_bullet = Bullet(ai_settings,screen,ship)
		bullets.add(new_bullet)
	elif event.key == pygame.K_q:	#event.key为按下或松开键盘的值，所以该判断不能再check_events调用
			sys.exit()


def check_key_up(ship,event):
	if event.key == pygame.K_RIGHT:
		ship.move_right = False
	if event.key == pygame.K_LEFT:
		ship.move_left = False
	if event.key == pygame.K_UP:
		ship.move_up = False
	elif event.key == pygame.K_DOWN:
		ship.move_down = False	

#响应外部事件
def check_events(ship,ai_settings,screen,bullets,stats,play_button,aliens,scoreboard):
	#监听键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:	#键盘按键响应
			check_key_down(ship,event,ai_settings,screen,bullets)
		elif event.type == pygame.KEYUP:	#键盘松开响应
			check_key_up(ship,event)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x,mouse_y = pygame.mouse.get_pos()
			check_play_button(stats, play_button, mouse_x, mouse_y,ship,ai_settings,screen,aliens,bullets,scoreboard)


def check_play_button(stats,play_button,mouse_x,mouse_y,ship,ai_settings,screen,aliens,bullets,scoreboard):
	button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
	if button_clicked and not stats.game_active:
		#隐藏光标
		#pygame.mouse.set_visible(False)
		#重置游戏速度
		ai_settings.initialize_dynamic_settings()
		stats.game_active = True
	
		stats.rest_stats()

		aliens.empty()
		bullets.empty()

		creat_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()

		#重置得分
		scoreboard.prep_score()
		scoreboard.prep_ships() 
	

#删除子弹
def update_bullets(aliens,bullets,ai_settings,screen,ship,stats,scoreboard):
	#更新子弹位置，并删除已消失子弹
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
	collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)

	if collisions:
		for aliens in collisions.values():
			stats.score += 10 * len(aliens)
			scoreboard.prep_score()

	#当前屏幕外星人消灭完后清屏重建外星人
	if len(aliens) == 0:
		#增加游戏速度
		ai_settings.increase_speed()
		#清空子弹并新建外星人
		bullets.empty()
		creat_fleet(ai_settings, screen, aliens,ship)


def get_number_aliens_x(ai_settings, alien_width):
	available_space_x = ai_settings.screen_width - 2 * alien_width 
	number_aliens_x = int(available_space_x / (2 * alien_width))
	return number_aliens_x

def get_number_rows(ai_settings,ship_height,alien_height):
	available_space_y = (ai_settings.screen_height -(3 * alien_height) - ship_height)
	number_rows = int(available_space_y / (2 * alien_height))
	return number_rows

def creat_alien(ai_settings,screen,aliens,alien_number,row_number):
	alien = Alien(ai_settings, screen)
	alien_width = alien.rect.width
	alien.x = alien_width + 2 * alien_width * alien_number
	alien.rect.x = alien.x
	alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
	aliens.add(alien)

#创建外星人编队
def creat_fleet(ai_settings,screen,aliens,ship):
	alien = Alien(ai_settings, screen)
	#计算一行最多容纳多少外星人
	number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
	
	number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
	
	for row_number in range(number_rows):
		number_aliens_x = randint(1,number_aliens_x)
		for alien_number in range(number_aliens_x):
			creat_alien(ai_settings, screen, aliens, alien_number,row_number)

#外星人向下飞行
def change_fleet_direction(ai_settings,aliens):
	for alien in aliens.sprites():
		alien.rect.y += ai_settings.fleet_drop_speed
	ai_settings.fleet_direction *= -1
	#print(ai_settings.fleet_direction)

#判断是否触碰边缘
def check_fleet_edges(ai_settings,aliens):
	for alien in aliens.sprites():
		if alien.check_edges():
			change_fleet_direction(ai_settings,aliens)
			break

#外星人移动
def update_alien(ai_settings,aliens,ship,screen,bullets,stats,scoreboard):
	check_fleet_edges(ai_settings, aliens)
	aliens.update()

	#检测外星人和飞船之间碰撞
	if pygame.sprite.spritecollideany(ship,aliens):
		ship_hit(ai_settings, screen, ship, bullets, aliens, stats,scoreboard)

	#检测外星人是否抵达屏幕底部边缘
	check_alien_bottom(ai_settings, screen, ship, bullets, aliens, stats,scoreboard)


#外星人撞到飞船
def ship_hit(ai_settings,screen,ship,bullets,aliens,stats,scoreboard):
	#减少一个飞船个数
	stats.ship_left -= 1

	if stats.ship_left > 0:
		#清空外星人和子弹
		aliens.empty()
		bullets.empty()
	
		#创建新的外星人
		creat_fleet(ai_settings, screen, aliens, ship)
		ship.center_ship()

		scoreboard.prep_ships()

		sleep(0.5)
	else:
		stats.game_active = False


#检测外星人是否抵达屏幕下边缘
def check_alien_bottom(ai_settings,screen,ship,bullets,aliens,stats,scoreboard):
	for alien in aliens.sprites():
		if alien.rect.bottom >= screen.get_rect().bottom:
			ship_hit(ai_settings,screen,ship,bullets,aliens,stats,scoreboard)
			break

#刷新屏幕
def update_screen(ai_settings,screen,ship,bullets,aliens,stats,play_button,scoreboard):
	screen.fill(ai_settings.bg_color)

	#绘制开始按钮
	if stats.game_active == False:
		play_button.draw_button()

	#绘制子弹
	for bullet in bullets.sprites():
		bullet.draw_bullet()

	#绘制飞船
	ship.blitme()

	#绘制外星人
	aliens.draw(screen)

	#绘制计分按钮
	scoreboard.draw_score()

	#让最近绘制屏幕可见
	pygame.display.flip()