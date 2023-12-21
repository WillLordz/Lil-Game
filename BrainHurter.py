import pygame
import random
#a



# Define screen size
SCREEN_WIDTH = 896
SCREEN_HEIGHT = 704

# Initialize Pygame and create screen
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.Font(None, 32)
# Set window title
pygame.display.set_caption("OMG PYGAME AMONG US IN REAL LIFE AT 3:00 AM UNEXPECTED TURN OF EVENTS GAY POTION WITH ELMO AT 3 AM I ALMOST DIED REAL!!!!! NOT CLICKBAIT PLEASE WATCH FIRST VIDEO VIDEO GAMES WITH ELMO IN VIRTUAL REALITY BIG BABES NOT CLICKBAIT 18+")


# Define character position and movement speed
player_x = 96
player_y = 96
player_direction = "right"
movement_speed = 32
bomb_charges = 3
game_state = "game"


# Define map size and tile size
MAP_WIDTH = 28
MAP_HEIGHT = 22
TILE_SIZE = 32
tile_x = 96
tile_y = 96
player_reseting = False




map_data = [[0 for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
def genrate_map():
    for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if random.random() < 0.01:
                    map_data[y][x] = 2                    
                elif random.random() < 0.55:
                    map_data[y][x] = 1
                else:
                    map_data[y][x] = 0
genrate_map()


#player returns to centure
def player_location_reset():
    global player_x, player_y
    player_x = 32 * (random.randint(12, 16))
    player_y = 32 * (random.randint(9, 13))


def get_tile_type(player_x, player_y):
    if player_x < 0 or player_x >= SCREEN_WIDTH or player_y < 0 or player_y >= SCREEN_HEIGHT:
        return 0
    else:
        tile_x = player_x // TILE_SIZE
        tile_y = player_y // TILE_SIZE
        return map_data[tile_y][tile_x]

# Get the tile type and print it


while True:
    
    if game_state == "game":

        #Map Logic
        if player_x < 0 or player_x >= SCREEN_WIDTH or player_y < 0 or player_y >= SCREEN_HEIGHT:
            player_location_reset()
            genrate_map()
            bomb_charges = 3   

        

        # Handle keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player_direction = "left"
                    tile_type = get_tile_type(player_x - movement_speed, player_y)
                    if tile_type != 1:
                        player_x -= movement_speed
                elif event.key == pygame.K_d:
                    player_direction = "right"
                    tile_type = get_tile_type(player_x + movement_speed, player_y)
                    if tile_type != 1:
                        player_x += movement_speed
                elif event.key == pygame.K_w:
                    player_direction = "up"
                    tile_type = get_tile_type(player_x, player_y - movement_speed)
                    if tile_type != 1:
                        player_y -= movement_speed
                elif event.key == pygame.K_s:
                    player_direction = "down"
                    tile_type = get_tile_type(player_x, player_y + movement_speed)
                    if tile_type != 1:
                        player_y += movement_speed
                elif event.key == pygame.K_r:
                        player_location_reset()
                        genrate_map()


            #Pull up menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    if game_state == "game":
                        game_state = "menu"


            tile_x = player_x // TILE_SIZE
            tile_y = player_y // TILE_SIZE

            if get_tile_type(player_x, player_y) == 2:
                bomb_charges += 1
                map_data[tile_y][tile_x] = 0


            #Bomb Mechanics
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    if bomb_charges >= 0:
                        bomb_charges -= 1    
                        if player_direction == "right":
                            map_data[tile_y][tile_x + 1] = 0
                        if player_direction == "left":
                            map_data[tile_y][tile_x - 1] = 0
                        if player_direction == "up":
                            map_data[tile_y - 1][tile_x] = 0
                        if player_direction == "down":
                            map_data[tile_y + 1][tile_x] = 0    

        #print(player_x)
        #print(player_y)

        
        # Update and draw the character

        
        # Create a 2D array for the map
        

        # Place some obstacles randomly
        

        #print(map_data)

        # Draw the map tiles
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                if map_data[y][x] == 0:
                    pygame.draw.rect(screen, (0, 5, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif map_data[y][x] == 1:
                    pygame.draw.rect(screen, (139, 69, 30), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                elif map_data[y][x] == 2:
                    pygame.draw.rect(screen, (255, 255, 255), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        

        

        pygame.draw.rect(screen, (128, 0, 128), (player_x, player_y, 32, 32))

        text_surface = font.render(str(bomb_charges), True, (255, 0, 0))
        screen.blit(text_surface, (0, 0))
        pygame.display.flip()


    elif game_state == "menu":
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_n:
                if game_state == "menu":
                    game_state = "game"




   

