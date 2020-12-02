# -*- encoding:UTF-8 -*-
# 誉天暑期训练营
import sys
import pygame

pygame.init()  # 初始化pygame
# 设置窗口
size = width, height = 640, 480
# 定义显示的屏幕
screen = pygame.display.set_mode(size)
# 设置颜色
color = (0, 0, 0)
# 加载图片
ball = pygame.image.load(r"D:\VSCode\code\PYTHON\pythonlearn\ball.png")
# 获取矩形的区域
ballrect = ball.get_rect()
# 设置移动的X轴,Y轴的距离
speed = [5, 5]
# 设置时钟
clock = pygame.time.Clock()
# 执行死循环，确保窗口一直显示
while True:
    clock.tick(60)  # 每秒执行60次
    # 检查事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    # 移动小球
    ballrect = ballrect.move(speed)
    # 碰到左右边缘
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    # 碰到上下边缘
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(color)  # 填充颜色
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame
