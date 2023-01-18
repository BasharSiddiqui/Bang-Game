
import pygame as py

py.init()

screen=py.display.set_mode((1280,720))
py.display.set_caption('BANG!!')

bg=py.image.load("bg2.png")

c1=py.image.load("c1prime.png")
c2=py.image.load("c2prime.png")
py.display.set_icon(c2)
c3=py.image.load("c3prime.png")
screens=py.image.load("screens.jpg")
shield=py.image.load("shield.png")
grave=py.image.load("grave.png")
ts=py.image.load("titlescreen.png")
bullet=py.image.load("bullet.png")
ammocan=py.image.load("ammo.png")

scr=py.transform.scale(screens,(1280,720))
bgg=py.transform.scale(bg,(1280,720))
asize=py.transform.scale(ammocan,(200,200))
c1size=py.transform.scale(c1,(190,190))
c2size=py.transform.scale(c2,(190,190))
c3size=py.transform.scale(c3,(250,250))
bsize=py.transform.scale(bullet,(80,30))
grave=py.transform.scale(grave,(250,250))
shield=py.transform.scale(shield,(80,80))

b1shooting3=py.transform.rotate(bsize,300)
b2shooting1=py.transform.rotate(bsize,180)
b2shooting3=py.transform.rotate(bsize,230)
b3shooting1=py.transform.rotate(bsize,125)
b3shooting2=py.transform.rotate(bsize,45)

py.mixer.music.load('song.mp3')
py.mixer.music.play(-1)
py.display.set_icon(c1)

font1 = py.font.SysFont('timesnewroman', 80)
font2 = py.font.SysFont('timesnewroman', 40)

shooting = [[0,bsize,b1shooting3],[b2shooting1,0,b2shooting3],[b3shooting1,b3shooting2]]
running=False
gamestate = -1
targetflag=False
dead=[False,False,False]
reload = [False,False,False]
safe=[False,False,False]
target=[None,None,None]
bullet=[0,0,0]
sprite = [0,0,0]
live = 3
selection=False
pc=0
anothergameflag=False
turncounter=0
running = True
ii=0
selectionflag=False

coords = [{"shield":(260,130),"grave":(215,60),"shooting":[0,(360,140),(370,180)]}
         ,{"shield":(1030,130),"grave":(1000,60),"shooting":[(935,140),0,(935,180)]}
         ,{"shield":(630,580),"grave":(570,500),"shooting":[(500,480),(720,480),0]}]




while running==True:
    #Controls loop
    

    for event in py.event.get():
        if event.type==py.QUIT: #exit
            running = False
        #print(event)
        if event.type==py.MOUSEBUTTONDOWN: #move game forward
            gamestate +=1
        if event.type==py.KEYDOWN:
            if event.key==py.K_SPACE: #move game forward
                gamestate +=1
            if anothergameflag==True: #checks to see if you are on the new game selection screen, activates controls only then
                if event.key==py.K_n:
                    gamestate=13
                if event.key==py.K_y:
                    gamestate=14

            if targetflag==True: #if on targeting screen

                if event.key==py.K_1: #select target 1
                    if bullet[pc]>0:
                        target[pc]=0
                        bullet[pc]-=1
                    selection=True

                if event.key==py.K_2: #select target 2 
                    if bullet[pc]>0: 
                        target[pc]=1
                        bullet[pc]-=1
                    selection=True

                if event.key==py.K_3: #select target 3
                    if bullet[pc]>0:
                        target[pc]=2
                        bullet[pc]-=1
                    selection=True

            if selectionflag==True: #checks to see if you are on move selection screen to activate controls

                if event.key==py.K_z: #selects shoot
                    selectionflag=False
                    if bullet[pc] == 0: #prevents bang gamestate from activating if player doesnt have bullets                
                        pass
                    else:
                        gamestate = 'BANG'
                    
                if event.key==py.K_s: #selects shield
                    selectionflag=False
                    safe[pc]=True
                    gamestate+=1


                if event.key==py.K_r: #selects reload
                    selectionflag=False
                    reload[pc] = True
                    bullet[pc]+=1
                    gamestate+=1


    #Game loop


    if gamestate == 'BANG': #targeting screen, if player chooses to shoot this is the screen that comes
            screen.blit(scr,(0,0))
            text='Select Target' 
            textsurface = font1.render(text, True, (0,0,0))
            screen.blit(textsurface,(400,1100/4))
            targetflag=True #activates controls for targeting
            if selection == True: #exits screen once selection is made in the control loop
                print("SELECTION TRIGGERED!",pc)
                targetflag=False
                
                if pc==0:
                    gamestate=2
                    selection = False
                if pc==1:
                    gamestate=4
                    selection = False
                if pc==2:
                    gamestate=6
                    selection = False
                
    if gamestate == -1: #Title Screen
        screen.blit(ts,(0,0))
    if gamestate == 0 and dead[0]==True:
        gamestate = 2
    if gamestate == 0: #Player 1 get ready
        pc=0
        screen.blit(scr,(0,0))
        text='Player '+str(pc+1)+' start!' 
        textsurface = font1.render(text, True, (0,0,0))
        screen.blit(textsurface,(400,280))


    if gamestate ==1: #Player 1 Select move
        selectionflag=True
        screen.blit(scr,(0,0))
        text='Press "z" for shoot, "s" for shield, "r" for reload' 
        textsurface = font2.render(text, True, (0,0,0))
        screen.blit(textsurface,(260,720/2))
        if bullet[pc]<1:
            text1='You are out of bullets' 
            textsurface1 = font1.render(text1, True, (255, 0, 0))
            screen.blit(textsurface1,(280,720/4))

    if gamestate == 2 and dead[1]==True:
        gamestate = 4
    if gamestate == 2: #P2 Get ready
        pc=1
        screen.blit(scr,(0,0))
        text='Player '+str(pc+1)+' start!' 
        textsurface = font1.render(text, True, (0,0,0))
        screen.blit(textsurface,(400,280))
    if gamestate ==3:#P2 select
        selectionflag=True
        screen.blit(scr,(0,0))
        text='Press "z" for shoot, "s" for shield, "r" for reload'
        textsurface = font2.render(text, True, (0,0,0))
        screen.blit(textsurface,(260,720/2))
        if bullet[pc]<1:
           text1='You are out of bullets'
           textsurface1 = font1.render(text1, True, (255, 0, 0))
           screen.blit(textsurface1,(280,720/4))

    if gamestate == 4 and dead[2]==True:
        gamestate = 6
    if gamestate == 4: #P3 get ready
        pc=2
        screen.blit(scr,(0,0))
        text='Player '+str(pc+1)+' start!' 
        textsurface = font1.render(text, True, (0,0,0))
        screen.blit(textsurface,(400,250))
    if gamestate == 5: #p3 select
        selectionflag=True
        screen.blit(scr,(0,0))
        text='Press "z" for shoot, "s" for shield, "r" for reload' 
        textsurface = font2.render(text, True, (0,0,0))
        screen.blit(textsurface,(260,720/2))
        if bullet[pc]<1:
            text1='You are out of bullets' 
            textsurface1 = font1.render(text1, True, (255, 0, 0))
            screen.blit(textsurface1,(280,720/4))

    if gamestate == 6: #current state of the game
        screen.blit(bgg,(0,0))

        screen.blit(c1size,(200,60))
        screen.blit(c2size,(1000,60))
        screen.blit(c3size,(550,500))
        for i in range(3):
            if dead[i]==True:   

                sprite[i]=grave
                spritecoords[i] = coords[i]["grave"] 
                screen.blit(sprite[i],spritecoords[i])


    if gamestate == 7: #calculations
        screen.blit(bgg,(0,0))

        screen.blit(c1size,(200,60))
        screen.blit(c2size,(1000,60))
        if target[2] == 1: #makes player 3 aim at the correct target
            c3sizef = py.transform.flip(c3size, True, False)
            screen.blit(c3sizef,(550,500))
        else:
            screen.blit(c3size, (550,500))

        for i in range (3): #calculates which player dies
            if target[i]!= None:
                if safe[target[i]]==False:
                    dead[target[i]]=True

        pass
        #print(safe,bullet,target,dead)  
    c=0
    for i in dead:
        if i == False:
            c+=1
    live=c
    if gamestate == 7: #game state after actions
        spritecoords = [0,0,0]
        for i in range(3):
            sprite[i]=shield
            spritecoords[i]= coords[i]["shield"]
            if dead[i]==True:
                sprite[i]=grave
                spritecoords[i] = coords[i]["grave"] 
            elif reload[i]==True:
                sprite[i]=asize
                #b2shooting1 to be replaced with reload sprite and better coords
                spritecoords[i] = coords[i]["shield"]
            elif target[i] != None:
                sprite[i]=shooting[i][target[i]]
                spritecoords[i] = coords[i]["shooting"][target[i]]
            


        screen.blit(sprite[0],spritecoords[0])
        screen.blit(sprite[1],spritecoords[1])
        screen.blit(sprite[2],spritecoords[2])

    if gamestate ==8:
        gamestate = 9
    
    if gamestate == 9: #checks if a winner has been decided
        if live==1 or live==0 : #in case of a winner being decided
            if live == 0:
                screen.blit(scr,(0,0))
                text='DRAW!!' 
                textsurface = font1.render(text, True, (0,0,0))
                screen.blit(textsurface,(500,300))
            if live == 1:
                screen.blit(scr,(0,0))
                winner=None
                for i in range(3):
                    if dead[i]==False:
                        winner=str(i+1)
                text='The winner is player '+winner 
                textsurface = font1.render(text, True, (0,0,0))
                screen.blit(textsurface,(260,1100/4))

            gamestate = 11
        else:
            gamestate =10

    if gamestate == 10: #next round calculations
        reload = [False,False,False]
        safe=[False,False,False]
        target=[None,None,None]
        sprite = [0,0,0]
        selection=False
        pc=0
        gamestate = 0
        selectionflag=False

    #gamestate variable checker
    ii+=1
    if ii%150==0:
        print(gamestate)
        print(safe,bullet,target,dead)

    if gamestate ==12: #new game yes or no screen
        anothergameflag=True
        screen.blit(scr,(0,0))
        text='Another game? Press "y" for yes, "n" for no' 
        textsurface = font2.render(text, True, (0,0,0))
        screen.blit(textsurface,(300,1100/4))


    if gamestate == 13: #endgame
        running = False

    if gamestate == 14: #new game initialization
        running=False
        targetflag=False
        safe=[False,False,False]
        bullet=[0,0,0]
        dead=[False,False,False]
        target=[None,None,None]
        live = 3
        safe[0]=False
        safe[1]=False
        safe[2]=False
        selection=False
        pc=0
        turncounter=0
        running = True
        ii=0
        endofgameflag=False
        anothergameflag=False
        gamestate = -1
        selectionflag=False



    py.display.flip()