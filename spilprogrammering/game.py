import random
import pygame


class Game():
    def __init__(self):
        if random.randint(1,10) == 1:
            self.grid = [[6 for y in range(0,10)] for x in range(0,10)]
        else:
            self.grid = [[random.randint(1,5) for y in range(0,10)] for x in range(0,10)]
        self.anim = [[0 for y in range(0,10)] for x in range(0,10)]
        self.scorre = 0
        self.done = False
        self.movesleft = 100
        self.background_music = pygame.mixer.Sound('y2mate.com - Wii Music - Gaming Background Music (HD)_x2NzoLMWAwQ (online-audio-converter.com).wav')
        self.point_sound = pygame.mixer.Sound('zapsplat_multimedia_game_sound_digital_high_pitched_generic_tone_001_55831 (online-audio-converter.com).wav')
        # self.point_sound = pygame.mixer.Sound('sound_spark_Glitch_Factory_01_Decimated_01 (online-audio-converter.com).wav')
        self.End_sound = pygame.mixer.Sound('human_audience_laughter_comedy_club_x200_people_komedia_brighton_comic_boom_011 (online-audio-converter.com).wav')

        print(self.grid)
    def build_grid(self):
        #import pdb; pdb.set_trace()
        for x in range(0, len(self.grid)):
            for y in range(0, len(self.grid)):
                if self.grid[x][y] == 0:
                    if y < len(self.grid[x])-1 and not all(self.grid[x][yy] == 0 for yy in range(y, len(self.grid[x]))):
                        # Flyt kolonnen ned
                        while(self.grid[x][y] == 0):
                            self.grid[x][y:] = self.shift_column(self.grid[x][y:], 1)
                            self.anim[x][y:] = [50 for i in range(y,len(self.anim[x]))]
                    # Fyld op med nye tiles
                    for fill in range(0,len(self.grid[x])):
                        if self.grid[x][fill] == 0:
                            if random.randint(1,10) == 1:
                                self.grid[x][fill] = 6
                            else:
                                self.grid[x][fill] = random.randint(1,5)


    def shift_column(self, l, n):
        return l[n:] + l[:n]


    def swap_tiles(self, x1, y1, x2, y2):
        self.movesleft -=1
        if self.movesleft == 0:
            self.done = True
        #Sørg for, at vi kun kan bytte naboceller.
        if abs(x1-x2) <= 1 and abs(y1-y2) <= 1:
            self.grid[x1][y1], self.grid[x2][y2] = self.grid[x2][y2], self.grid[x1][y1]


    def detect_matches(self, auto = False):
        points = 0
        for x in range(1, len(self.grid)-1):
            for y in range(0, len(self.grid)):
                #Detect horizontal match
                if self.grid[x][y] == self.grid[x-1][y] and self.grid[x][y] == self.grid[x+1][y]:
                    c = self.grid[x][y]

                    if self.grid[x][y] == 6:
                        for x_pos in range(0,len(self.grid[y])):
                            self.grid[x_pos][y] = 0
                            self.scorre += len(self.grid[y])*2
                    else:
                        self.grid[x-1][y] = 0
                        self.grid[x][y] = 0
                        self.grid[x+1][y] = 0
                        x1 = x+2
                        while x1 < len(self.grid) and self.grid[x1][y] == c:
                            self.grid[x1][y] = 0
                            x1 += 1
                        self.scorre += 1
                        #Hvis vi har fjernet brikker, skal pladen fyldes igen
                        self.point_sound.play(1)
                    self.build_grid()
        for y in range(1, len(self.grid)-1):
            for x in range(0, len(self.grid)):
                #Detect vertical match
                if self.grid[x][y] == self.grid[x][y-1] and self.grid[x][y] == self.grid[x][y+1]:
                    c = self.grid[x][y]

                    if self.grid[x][y] == 6:
                        for y_pos in range(0,len(self.grid[x])):
                            self.grid[x][y_pos] = 0
                            self.scorre += len(self.grid[x])*2
                    else:
                        self.grid[x][y-1] = 0
                        self.grid[x][y] = 0
                        self.grid[x][y+1] = 0
                        y1 = y+2
                        while y1 < len(self.grid) and self.grid[x][y1] == c:
                            self.grid[x][y1] = 0
                            y1 += 1
                        self.scorre += 1
                        #Hvis vi har fjernet brikker, skal pladen fyldes igen
                        self.point_sound.play(1)
                    self.build_grid()
        for y in range(1, len(self.grid)-1):
            for x in range(0, len(self.grid)-1):
                #Detect vertical match
                if self.grid[x][y] == self.grid[x-1][y-1] and self.grid[x][y] == self.grid[x+1][y+1]:
                    c = self.grid[x][y]
                    if self.grid[x][y] == 6:
                        pass
                    else:
                        self.grid[x-1][y-1] = 0
                        self.grid[x][y] = 0
                        self.grid[x+1][y+1] = 0
                        y1 = y+2
                        x1 = x+2
                        while y1 < len(self.grid) and x1 < len(self.grid) and self.grid[x1][y1] == c:
                            self.grid[x1][y1] = 0
                            y1 += 1
                            x1 += 1
                        self.scorre += 1
                        #Hvis vi har fjernet brikker, skal pladen fyldes igen
                        self.point_sound.play(1)
                    self.build_grid()
        for y in range(1, len(self.grid)-1):
            for x in range(0, len(self.grid)-1):
                #Detect vertical match
                    if self.grid[x][y] == self.grid[x+1][y-1] and self.grid[x][y] == self.grid[x-1][y+1]:
                        c = self.grid[x][y]
                        if self.grid[x][y] == 6:
                            pass
                        else:
                            self.grid[x+1][y-1] = 0
                            self.grid[x][y] = 0
                            self.grid[x-1][y+1] = 0
                            y1 = y+2
                            x1 = x+2
                            while y1 < len(self.grid) and x1 < len(self.grid) and self.grid[x1][y1] == c:
                                self.grid[x1][y1] = 0
                                y1 += 1
                                x1 += 1
                            self.scorre += 1
                            #Hvis vi har fjernet brikker, skal pladen fyldes igen
                            self.point_sound.play(1)
                            self.build_grid()
