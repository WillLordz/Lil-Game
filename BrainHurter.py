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








#player returns to centure

# Get the tile type and print it
map_data = [[0 for x in range(MAP_WIDTH)] for y in range(MAP_HEIGHT)]
def generate_map():
        for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    if random.random() < 0.01:
                        map_data[y][x] = 2                    
                    elif random.random() < 0.55:
                        map_data[y][x] = 1
                    else:
                        map_data[y][x] = 0
generate_map()

def probabilty_selection():
        bomb_percentage = 0.01
        wall_percentage = 0.45
        selection = False
        while selection != True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("1")
                    selection = True
        return selection

while True:

    def probabilty_selection():
        selection = probabilty_selection()
        bomb_percentage = 0.01
        wall_percentage = 0.45
        while selection != True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    print("1")
                    selection = True
        return wall_percentage, bomb_percentage


    def generate_map():
        wall_percentage, bomb_percentage = probabilty_selection()
        for y in range(MAP_HEIGHT):
                for x in range(MAP_WIDTH):
                    if random.random() < bomb_percentage:
                        map_data[y][x] = 2                    
                    elif random.random() < wall_percentage:
                        map_data[y][x] = 1
                    else:
                        map_data[y][x] = 0

    def assign_images():
        wall_tile = pygame.image.load('Wall_Tile.png')
        background_tile = pygame.image.load('Background_Tile.png')
        bomb_tile = pygame.image.load('Bomb_Tile.png')
        player = pygame.image.load('Player.png')
        return wall_tile, background_tile, bomb_tile, player 

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

    #Draws map on screen
    def draw_map_and_player():
                wall_tile, background_tile, bomb_tile, player = assign_images()
                MAP_WIDTH = 28
                MAP_HEIGHT = 22
                TILE_SIZE = 32
                for y in range(MAP_HEIGHT):
                    for x in range(MAP_WIDTH):
                        if map_data[y][x] == 0:
                            screen.blit(background_tile, (x * TILE_SIZE, y * TILE_SIZE))
                        elif map_data[y][x] == 1:
                            screen.blit(wall_tile, (x * TILE_SIZE, y * TILE_SIZE))
                        elif map_data[y][x] == 2:
                            screen.blit(bomb_tile, (x * TILE_SIZE, y * TILE_SIZE))
                screen.blit(player, (player_x, player_y, 32, 32))

    def bomb_checks(bomb_charges):
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

        return bomb_charges
    
    
    
    



    if game_state == "game":

        #Map Logic
        if player_x < 0 or player_x >= SCREEN_WIDTH or player_y < 0 or player_y >= SCREEN_HEIGHT:
            player_location_reset()
            generate_map()
            bomb_charges = 3   

        

        # Handle keyboard input
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                bomb_charges = bomb_checks(bomb_charges)
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
                    bomb_charges = 3
                    player_location_reset()
                    generate_map()
                elif event.key == pygame.K_p:
                    probabilty_selection()



            #Pull up menu
            

            tile_x = player_x // TILE_SIZE
            tile_y = player_y // TILE_SIZE

            if get_tile_type(player_x, player_y) == 2:
                bomb_charges += 1
                map_data[tile_y][tile_x] = 0


        #Bomb Mechanics

        #print(player_x)
        #print(player_y)

        
        # Update and draw the character

        
        # Create a 2D array for the map
        

        # Place some obstacles randomly
        

        #print(map_data)

        # Draw the map tiles
        
            
        
        draw_map_and_player()
        
        
        text_surface = font.render(str(bomb_charges), True, (255, 0, 0))
        screen.blit(text_surface, (0, 0))
        pygame.display.flip()






   

