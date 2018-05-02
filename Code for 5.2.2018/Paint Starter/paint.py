## Paint Program
## Author: 
## A basic painting program for freehand drawing

import pygame, sys

def main():
    
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption("Paint:  (r)ed, (g)reen, (b)lue, (w)hite, blac(k), (1-9) width, (c)lear, (s)ave, (l)oad, (q)uit")  #This is all on one line
    drawingSurface = pygame.Surface(screen.get_size())
    drawingSurface.fill((255, 255, 255))
    clock = pygame.time.Clock()
    keepGoing = True
    lineStart = (0, 0)
    drawColor = (0, 0, 0)
    lineWidth = 3
    
    #Game loop
    while keepGoing:
        clock.tick(30)  #set frame rate

        #check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
                
            elif event.type == pygame.MOUSEMOTION:
                lineEnd = pygame.mouse.get_pos()
                #check for left mouse button pressed
                if pygame.mouse.get_pressed() == (1, 0, 0):
                    pygame.draw.line(drawingSurface, drawColor, lineStart,
                                     lineEnd, lineWidth) #draw a line
                lineStart = lineEnd
                
            elif event.type == pygame.KEYDOWN:
            #place myData into a tuple to be passed to checkKeys
                myData = (event, drawingSurface, drawColor, lineWidth, keepGoing)
                myData = checkKeys(myData)
                (event, drawingSurface, drawColor, lineWidth, keepGoing) = myData

        screen.blit(drawingSurface, (0, 0))
        myLabel = showStats(drawColor, lineWidth)
        screen.blit(myLabel, (850, 730))
        pygame.display.flip()
        #End of game loop
        
    pygame.display.quit()
    sys.exit()
    
def checkKeys(myData):
    filename = 'myPainting.bmp'
    """test for various keyboard inputs"""
    #extract the data
    (event, drawingSurface, drawColor, lineWidth, keepGoing) = myData
    if event.key == pygame.K_q:
        #quit
        #set keepGoing to False
        #Add code here
        
    elif event.key == pygame.K_c:
        #clear screen
        #Fill drawingSurface with white
        #Add code here
        
    elif event.key == pygame.K_s:
        #save picture
        #save drawingSurface to filename
        #Add code here
        
    elif event.key == pygame.K_l:
        #load picture
        #load filename to drawingSurface
        #Add code here
        
    elif event.key == pygame.K_r:
        #red
        drawColor = (255, 0, 0)
    #Add code for more colors
        

#line widths
    elif event.key == pygame.K_1:
        lineWidth = 1
    #Add code for more line widths

#return all values 
    myData = (event, drawingSurface, drawColor, lineWidth, keepGoing)
    return myData

def showStats(drawColor, lineWidth):
    """ shows the current statistics """
    myFont = pygame.font.SysFont("None", 20)
    stats = "color: %s, width: %d" % (drawColor, lineWidth)
    statSurf = myFont.render(stats, 1, (drawColor))
    return statSurf

main()
