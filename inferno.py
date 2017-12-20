
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
import pickle
import pygame
import sys
from random import *


class pane5window:

    def run(self, gameDisplay, info):

        crashed = False
        orientation1 = 0
        orientation2 = 0
        orientation3 = 0
        orientation4 = 0
        orientation5 = 0
        orientation6 = 0

        leftmove = leftdownmove = 350
        rightdownmove = 659
        midmove = 555
        rightmove = 761

        limit1 = limit2 = 0

        leftman = pygame.image.load("data/images/man.png")
        rightman = pygame.transform.flip(leftman, True, False)
        background = pygame.image.load("data/images/up3.png")
        background1 = pygame.image.load("data/images/down2.png")

        lspike = pygame.image.load("data/images/Spike.png")
        rspike = pygame.transform.flip(lspike, True, False)

        background = pygame.transform.scale(
            background, (600, info.current_h / 2))
        background1 = pygame.transform.scale(
            background1, (600, info.current_h / 2))

        y_axis1 = 400 + 100
        y_axis2 = 700 + 80

        y_axisa = 430 + 150
        y_axisb = 700 + 150

        y_axisx = 460 + 80

        leftquad = leftman
        midquad = leftman
        rightquad = leftman

        leftdown = leftman
        rightdown = leftman

        f1 = f2 = f3 = f4 = f5 = 0
        m1 = m2 = m3 = m4 = m5 = 0
        time1 = time2 = 0

        font_path = "fonts/arial.ttf"
        font_size = 50
        font1 = pygame.font.Font(font_path, font_size)
        score = 0

        x_axis1 = x_axis2 = 350
        x_axisa = x_axisb = 659
        x_axisx = x_axisy = 761
        speed = 4
        flag = 1

        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()
        timer = pygame.time.Clock()

        sound = True
        try:
            pygame.mixer.init()
        except Exception, err:
            sound = False
            print 'error with sound', err

        jump = pygame.mixer.Sound("data/sound/jump.wav")
        scoremusic = pygame.mixer.Sound("data/sound/score.wav")
        collide = pygame.mixer.Sound("data/sound/fall.wav")

        while not crashed:
            # Gtk events

            while Gtk.events_pending():
                Gtk.main_iteration()
            event = pygame.event.poll()
            # totaltime+=timer.tick()
            if event.type == pygame.QUIT:
                # totaltime+=timer.tick()
                crashed = True

            # print event

            gameDisplay.fill(black)
            gameDisplay.blit(background, (0 + 350, 0))

            # Keypress orientation change

            if event.type == pygame.KEYDOWN and event.key == 97 and f1 == 0:
                jump.play(0)
                f1 = 1
                m1 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 115 and f2 == 0:
                jump.play(0)
                f2 = 1
                m2 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 100 and f3 == 0:
                jump.play(0)
                f3 = 1
                m3 = 1  # start moving

            # down key structure

            if event.type == pygame.KEYDOWN and event.key == 276 and f4 == 0:
                jump.play(0)
                f4 = 1
                m4 = 1  # start moving

            if event.type == pygame.KEYDOWN and event.key == 275 and f5 == 0:
                jump.play(0)
                f5 = 1
                m5 = 1  # start moving

            # Check for when to stop

            if leftmove > 484 + 20:  # left move
                leftquad = rightman
                m1 = f1 = 0
                leftmove = 484 + 20
                time1 = 0

            if leftmove < 350:
                leftquad = leftman
                m1 = f1 = 0
                leftmove = 350
                time1 = 0

            if midmove < 555:  # mid move
                midquad = leftman
                m2 = f2 = 0
                midmove = 555
                time2 = 0

            if midmove > 690 + 20:
                midquad = rightman
                m2 = f2 = 0
                midmove = 690 + 20
                time2 = 0

            if rightmove < 761:  # right move move
                rightquad = leftman
                m3 = f3 = 0
                rightmove = 761
                time2 = 0

            if rightmove > 761 + 156:
                rightquad = rightman
                m3 = f3 = 0
                rightmove = 761 + 156
                time2 = 0

            # down orintation change and stop moves

            if leftdownmove > 608:
                leftdown = rightman
                m4 = f4 = 0
                leftdownmove = 608
                time1 = 0

            if leftdownmove < 350:
                leftdown = leftman
                m4 = f4 = 0
                leftdownmove = 350
                time1 = 0

            if rightdownmove < 659:
                rightdown = leftman
                m5 = f5 = 0
                rightdownmove = 659
                time2 = 0

            if rightdownmove > 916:
                rightdown = rightman
                m5 = f5 = 0
                rightdownmove = 916
                time2 = 0

            if m1 == 1:

                if leftquad == leftman:
                    leftmove += 30
                if leftquad == rightman:
                    leftmove -= 30
                time1 += 1

            if m2 == 1:

                if midquad == leftman:
                    midmove += 30
                if midquad == rightman:
                    midmove -= 30
                time2 += 1

            if m3 == 1:

                if rightquad == leftman:
                    rightmove += 30
                if rightquad == rightman:
                    rightmove -= 30
                time2 += 1

            if m4 == 1:

                if leftdown == leftman:
                    leftdownmove += 30
                if leftdown == rightman:
                    leftdownmove -= 30
                time2 += 1

            if m5 == 1:

                if rightdown == leftman:
                    rightdownmove += 30
                if rightdown == rightman:
                    rightdownmove -= 30
                time2 += 1

            #[350,608]   [659, 916]

            # up Guys Display

            if leftquad == leftman or leftquad == rightman:
                gameDisplay.blit(leftquad, (leftmove, 30))

            if midquad == leftman or midquad == rightman:
                gameDisplay.blit(midquad, (midmove, 30))

            if rightquad == leftman or rightquad == rightman:
                gameDisplay.blit(rightquad, (rightmove, 30))

            ######### SPIKE PART###########

            if orientation1 == 0:  # orientation change
                x_axis1 = 350
                gameDisplay.blit(lspike, (x_axis1, y_axis1))

            if orientation1 == 1:
                x_axis1 = 485
                gameDisplay.blit(rspike, (x_axis1, y_axis1))

            # mid side spikes
            if orientation3 == 0:
                x_axisa = 555
                gameDisplay.blit(lspike, (x_axisa, y_axisa))

            if orientation3 == 1:
                x_axisa = 691
                gameDisplay.blit(rspike, (x_axisa, y_axisa))

            # right side spikes

            if orientation5 == 0:
                x_axisx = 761
                gameDisplay.blit(lspike, (x_axisx, y_axisx))

            if orientation5 == 1:
                x_axisx = 761 + 136
                gameDisplay.blit(rspike, (x_axisx, y_axisx))

            # bottom spikes

            if orientation2 == 0 and y_axis2 > 380:
                x_axis2 = 350
                gameDisplay.blit(lspike, (x_axis2, y_axis2))

            if orientation2 == 1 and y_axis2 > 380:
                x_axis2 = 589
                gameDisplay.blit(rspike, (x_axis2, y_axis2))

            if orientation4 == 0 and y_axisb > 380:
                x_axisb = 659
                gameDisplay.blit(lspike, (x_axisb, y_axisb))

            if orientation4 == 1 and y_axisb > 380:
                x_axisb = 659 + 238
                gameDisplay.blit(rspike, (x_axisb, y_axisb))

            y_axis1 -= speed
            y_axis2 -= speed

            y_axisa -= speed
            y_axisb -= speed

            y_axisx -= speed

            if y_axis1 <= -40 or y_axis2 <= 380 or y_axisa <= -40 or y_axisb <= 380 or \
               y_axisx <= -40:
                scoremusic.play(0)
                score += 1

            if(y_axis1 < -40):
                orientation1 = randint(0, 1)

                y_axis1 = 400

            if(y_axis2 < 380):
                orientation2 = randint(0, 1)

                y_axis2 = 700

            if(y_axisa < -40):
                orientation3 = randint(0, 1)

                y_axisa = 400

            if(y_axisb < 380):
                orientation4 = randint(0, 1)

                y_axisb = 700

            if(y_axisx < -40):
                orientation5 = randint(0, 1)

                y_axisx = 400

            gameDisplay.blit(background1, (0 + 350, 380)
                             )  # bottom part display

            # bottom guys display

            if leftdown == leftman or leftdown == rightman:
                gameDisplay.blit(leftdown, (leftdownmove, 400))

            if rightdown == leftman or rightdown == rightman:
                gameDisplay.blit(rightdown, (rightdownmove, 400))

            # bottom spikes

            if orientation2 == 0 and y_axis2 > 380:
                x_axis2 = 350
                gameDisplay.blit(lspike, (x_axis2, y_axis2))

            if orientation2 == 1 and y_axis2 > 380:
                x_axis2 = 589
                gameDisplay.blit(rspike, (x_axis2, y_axis2))

            if orientation4 == 0 and y_axisb > 380:
                x_axisb = 659
                gameDisplay.blit(lspike, (x_axisb, y_axisb))

            if orientation4 == 1 and y_axisb > 380:
                x_axisb = 659 + 238
                gameDisplay.blit(rspike, (x_axisb, y_axisb))

            scores = font1.render(str(score), 1, (0, 0, 0))
            gameDisplay.blit(scores, (200 + 650, 30))

            if leftquad.get_rect(center=(leftmove + 5, 30 + 10)).collidepoint(x_axis1 + 8, y_axis1):
              # or
              # leftquad.get_rect(center=(leftmove+5,100+10)).collidepoint(x_axis2+8,y_axis2):
                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
                return score

            if midquad.get_rect(center=(midmove + 5, 30 + 10)).collidepoint(x_axisa + 8, y_axisa):
              # or
              # midquad.get_rect(center=(midmove+5,100+10)).collidepoint(x_axisb+8,y_axisb):
                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
                return score

            if rightquad.get_rect(center=(rightmove + 5, 30 + 10)).collidepoint(x_axisx + 8, y_axisx):

                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
                return score

            # bottom boy collision collision detection

            if leftdown.get_rect(center=(leftdownmove + 5, 400 + 10)).collidepoint(x_axis2 + 8, y_axis2):

                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
                return score

            if rightdown.get_rect(center=(rightdownmove + 5, 400 + 10)).collidepoint(x_axisb + 8, y_axisb):

                pygame.mixer.music.load("data/sound/fall.wav")
                pygame.mixer.music.play(0)
                # collide.play(0)
                return score

            pygame.display.update()
            clock.tick(60)

            if crashed == True:                                   # Game crash or Close check
                pygame.quit()
                sys.exit()

        # Just a window exception check condition

        event1 = pygame.event.get()
        if event1.type == pygame.QUIT:
            crashed = True

        if crashed == True:
            pygame.quit()
            sys.exit()
