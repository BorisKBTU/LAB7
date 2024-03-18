import datetime
import pygame
import sys


class ClockApp:
    def __init__(self):
        pygame.init()
        self.screen_width = 1000
        self.screen_height = 800
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Clock")
        self.clock_image = pygame.image.load('mainclock.png')
        self.clock_rect = self.clock_image.get_rect(center=(self.screen_width // 2, self.screen_height // 2 - 10))
        self.hour_hand_image = pygame.image.load('rightarm.png')
        self.minute_hand_image = pygame.image.load('leftarm.png')
        self.hour_angle, self.minute_angle = self.get_time()
        self.minute_angle = self.minute_angle * 6
        self.hour_angle = self.hour_angle * 30

    def update_time(self):
        hour, minute = self.get_time()
        self.hour_angle = hour * 30
        self.minute_angle = minute * 6

    def get_time(self):
        time = datetime.datetime.now().time().strftime("%H:%M:%S")
        hours, minutes, seconds = [int(i) for i in time.split(':')]
        hours %= 12
        hours += 1.8
        hour_proportion = hours + minutes / 60 + seconds / 3600
        minutes_proportion = minutes + seconds / 60
        return hour_proportion, minutes_proportion

    def draw_clock(self):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.clock_image, self.clock_rect)

    def draw_arrows(self):
        rotated_hour_hand = pygame.transform.rotate(self.hour_hand_image, -self.hour_angle)
        rotated_minute_hand = pygame.transform.rotate(self.minute_hand_image, -self.minute_angle)
        rotated_hour_hand_rect = rotated_hour_hand.get_rect(center=self.clock_rect.center)
        rotated_minute_hand_rect = rotated_minute_hand.get_rect(center=self.clock_rect.center)
        self.screen.blit(rotated_hour_hand, rotated_hour_hand_rect)
        self.screen.blit(rotated_minute_hand, rotated_minute_hand_rect)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.update_time()
            self.draw_clock()
            self.draw_arrows()
            pygame.display.flip()
            pygame.time.Clock().tick(10)


app = ClockApp()
app.run()
