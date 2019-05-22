#Universal Python Games
#Eric Jiang, Wenqi 
#Penquin's Rescue
from gamelib import*
game=Game(800,600,"Penquin's Rescue")

tbk=Image("images//titlebk.jpg",game)
title=Image("images//title.png",game)
#font
f=Font(white,20,white,"comic sans ms")
ft=Font(blue,20,blue,"comic sans ms")


tbk.resizeTo(800,600)
title.moveTo(400,200)
title.resizeBy(10)
while not game.over:
    game.processInput()
    tbk.draw()
    title.draw()
    game.drawText("(Click to continue)",300,470,f)
    game.drawText("Universal Python Games",570,550,ft)
    if mouse.LeftClick:
        game.over=True

    game.update(30)
    game.over 
game.over=False


tbk=Image("images//titlebk.jpg",game)
htp=Image("images//p-trans.png",game)
story=Image("images//story.png",game)
play=Image("images//play.png",game)
play.moveTo(400,130)
play.resizeBy(30)
story.moveTo(400,230)
story.resizeBy(30)
htp.moveTo(400,330)
htp.resizeBy(30)
f=Font(black,40,white,"pacifico")

back=Image("images//back.png",game)
back.moveTo(70,20)
back.resizeBy(-30)
back.visible=False
con=Image("images//continue.png",game)
con.moveTo(680,20)
con.resizeBy(-30)
con.visible=False
storyimage=Image("images//storyimage.png",game)
storyimage.resizeBy(-5)
storyimage.moveTo(400,355)
storyimage.visible=False
htpimage=Image("images//htpimage.png",game)
htpimage.resizeBy(-48)
htpimage.visible=False
con2=Image("images//continue.png",game)
con2.moveTo(690,570)
con2.resizeBy(-40)
con2.visible=False
back2=Image("images//back.png",game)
back2.moveTo(70,570)
back2.resizeBy(-30)
back2.visible=False
#title
while not game.over:
    game.processInput()
    tbk.draw()
    htp.draw()
    story.draw()
    play.draw()
    htpimage.draw()
    con2.draw()
    back2.draw()
    storyimage.draw()
    back.draw()
    con.draw()
    
    if mouse.collidedWith(story,"rectangle")and mouse.LeftClick:
        storyimage.visible=True
        con.visible=True
        back.visible=True
        htpimage.visible=False
        con2.visible=False
        back2.visible=False
    if mouse.collidedWith(back,"rectangle")and mouse.LeftClick:
        storyimage.visible=False
        con.visible=False
        back.visible=False
        htpimage.visible=False
        con2.visible=False
        back2.visible=False
    if mouse.collidedWith(back2,"rectangle")and mouse.LeftClick:
        htpimage.visible=False
        con2.visible=False
        back2.visible=False
    if mouse.collidedWith(con,"rectangle")and mouse.LeftClick:
        game.over=True
    if mouse.collidedWith(play,"rectangle")and mouse.LeftClick:
        game.over=True
    if mouse.collidedWith(htp,"rectangle") and mouse.LeftClick:
        htpimage.visible=True
        con2.visible=True
        back2.visible=True
    game.update(30)
    game.over 
game.over=False


bk=Image("images//bk.jpg",game)
bear=Animation("images//bear.png",16,game,827/4,620/4)
fishc=Image("images//fishcount.png",game)
ices1=Image("images//icespikes.png",game)
ices2=Image("images//icespikes.png",game)
ices3=Image("images//icespikes.png",game)
game.setBackground(bk)
bk.resizeTo(800,600)
bear.moveTo(200,480)

f1=Font(black,40,white,"pacifico")
#level 1
jumping= False
landed=False
factor=1

ices=[]
for index in range(3):
    ices.append(Image("images//icespikes.png",game))
for index in range(3):
    ices[index].setSpeed(6,90)
    ices[0].moveTo(830,465)
    ices[1].moveTo(1200,465)
    ices[2].moveTo(1600,465)
    
fish=Image("images//fish.png",game)


fish=[]
for index in range(3):
    fish.append(Image("images//fish.png",game))
for index in range(3):
    fish[index].resizeBy(-50)
    b=randint(50,100)
    a=randint(100,300)
    fish[index].visible=True

#go
go1=Image("images//game-over.png",game)
go1.visible=False
go1.resizeTo(800,600)
f2=Font(white,20,blue,"comic sans ms")
blood=Image("images//blood.png",game)
blood.resizeBy(-75)
blood.visible=False
blood1=Image("images//blood.png",game)
blood1.resizeBy(-75)
blood1.visible=False
blood2=Image("images//blood.png",game)
blood2.resizeBy(-75)
blood2.visible=False
while not game.over:
    game.processInput()
    go1.draw()
    game.scrollBackground("left",6)
    for index in range(3):
        ices[index].move()
    game.drawText("Health:"+str(bear.health),3,3,f)
    #fish
    for index in range(3):
        fish[0].moveTo(ices[0].x-a,ices[0].y+40)
        fish[1].moveTo(ices[1].x,ices[1].y-b)
        fish[2].moveTo(ices[2].x-40,ices[2].y)
        
    # ices
    for index in range(3):
        if bear.collidedWith(fish[index]):
            fish[index].visible=False
            bear.health+=30
        if ices[2].isOffScreen("left"):
            ices[0].moveTo(830,465)
            ices[1].moveTo(1200,465)
            ices[2].moveTo(1600,465)
            ices[0].visible=True
            ices[1].visible=True
            ices[2].visible=True
            blood2.visible=False
            #fish.visible=True            
    #bear,jump,ice s
    blood.moveTo(ices[0].x,ices[0].y)
    blood1.moveTo(ices[1].x,ices[1].y)
    blood2.moveTo(ices[2].x,ices[2].y)
    if bear.collidedWith(ices[0])or bear.collidedWith(ices[1]) or bear.collidedWith(ices[2]):
        bear.health-=30
    if bear.collidedWith(ices[0]):
        blood.visible=True
        blood.moveTo(ices[0].x,ices[0].y)
        ices[0].visible=False
    if bear.collidedWith(ices[1]):
        blood1.visible=True
        blood1.moveTo(ices[1].x,ices[1].y)
        ices[1].visible=False
    if bear.collidedWith(ices[2]):
        blood2.visible=True
        blood2.moveTo(ices[2].x,ices[2].y)
        ices[2].visible=False
        
    if blood.isOffScreen("left"):
        blood.visible=False
    if blood1.isOffScreen("left"):
        blood1.visible=False
    if blood2.isOffScreen("left"):
        blood2.visible=False
    #over
    for index in range(3):
        if bear.health<0:
            go1.visible=True
            game.score=0
            #bear.visible=False
            ices[index].visible=False
            bk.visible=False
            fish[index].visible=False
            blood.visible=False
            blood1.visible=False
            blood1.visible=False
            game.drawText("(Click to restart)",300,470,f2)
        if mouse.LeftClick and mouse.collidedWith(go1) or mouse.LeftClick and mouse.collidedWith(bear):
            go1.visible=False
            bk.visible=True
            ices[0].visible=True
            ices[1].visible=True
            ices[2].visible=True
            fish[index].visible=True
            bear.health=100
            game.score=0

        
    if bear.y<480:
        landed=False
    else:
        landed=True
    if keys.Pressed[K_SPACE] and landed and not jumping:
        jumping=True
    if jumping:
        bear.stop()
        bear.y -=38*factor#adjust for the drop
        #Make the character go up.    Factor creates a slowing effect to the jump
        factor*=.95#fall slowly
        landed = False
        #Since you are jumping you are no longer staying on land
        if factor < .18:
            jumping = False
            #Stop jumping once the slowing effect finishes
            factor = 1
    
    if not landed: #is jumping
        bear.y+=10#adjust for the height of the jump - lower number higher jump
        
    if landed:
        bear.nextFrame()
    
    bear.draw()
    for index in range(3):
        fish[index].draw()
        
    game.score+=1
    if game.score>700:
        game.over=True
    
    blood.draw()
    blood1.draw()
    blood2.draw()
    game.update(30)
    game.over 
game.over=False

#transition1
bk2=Image("images//11.jpg",game)
bk2.resizeTo(800,600)
zom=Image("images//zombie.png",game)
zom.resizeBy(-65)
zom.setSpeed(5,60)
jel=Image("images//dd.png",game)
jel.resizeBy(-90)
jel.setSpeed(5,70)
pok=Image("images//13.png",game)
pok.resizeBy(-77)
pok.setSpeed(5,80)
pok1=Image("images//14.png",game)
pok1.resizeBy(-65)
pok1.setSpeed(5,90)

water=Image("images//water.png",game)
water.moveTo(900,530)
water.resizeBy(30)
bk1=Image("images//bk.jpg",game)
d=Image("images//dialogue.png",game)
d.resizeBy(-50)
d.moveTo(300,350)
d.visible=True
bear.moveTo(200,480)
arrow=Image("images//arrow.png", game)
arrow.resizeBy(-30)
arrow.moveTo(700,550)

#transition 1
while not game.over:
    game.processInput()
    bk1.draw()
    water.draw()
    bear.draw()
    d.draw()
    arrow.draw()
    bear.move()
    bear.stop()
    if mouse.collidedWith(arrow) and mouse.LeftClick:
        d.visible=False
        game.over=True
    game.update(30)
    game.over 
game.over=False


while not game.over:
    game.processInput()
    bk1.draw()
    water.draw()
    bear.x+=10
    bear.nextFrame()
    if bear.collidedWith(water):
        game.over=True
    game.update(30)
    game.over 
game.over=False

f2=Font(white,40,black,"pacifico")
#level 2
bear2=Animation("images//bg.png",16,game,827/4,620/4)
bear21=Animation("images//bg2.png",16,game,827/4,620/4)
bear3=Animation("images//bg.png",16,game,827/4,620/4)
b=Image("images//123.png",game)
b.visible=False
b.setSpeed(20,270)
b.resizeBy(-95)
b1=Image("images//1234.png",game)
b1.visible=False
b1.setSpeed(20,90)
b1.resizeBy(-95)
go=Image("images//333.png",game)
go.visible=False
go.resizeBy(80)
bk3=Image("images//11.jpg",game)
bk3.resizeTo(800,600)
bk3.visible=False
rs=Image("images//restart.png",game)
bear2.moveTo(60,50)
zom.moveTo(700,100)
jel.moveTo(100,500)
pok.moveTo(700,500)
pok1.moveTo(700,100)
rs.visible=False
go.moveTo(400,200)
rs.moveTo(400,400)
rs.resizeBy(-30)
game.score=0
bear3.setSpeed(3,315)
pct=-0.5
bear3.visible=False
bear3.moveTo(400,300)
bear21.visible=False
bear21.moveTo(60,50)
inv=Image("images//invis.png",game)
inv.resizeBy(80)

inv1=Image("images//invis.png",game)
inv1.resizeBy(80)
#underwater
while not game.over:
    game.processInput()
    
    bk2.draw()
    bear2.draw()
    b.move()
    b1.move()
    inv.draw()
    inv1.draw()
    #control
    if keys.Pressed[K_LEFT]:
        bear2.x-=7
        bear2.visible=False
        bear21.visible=True
        bear21.x-=7
        inv.moveTo(bear21.x,bear21.y)
        inv.visible=True
        inv1.visible=False
    if keys.Pressed[K_RIGHT]:
        bear2.x+=7
        bear21.x+=7
        bear21.visible=False
        bear2.visible=True
        inv1.moveTo(bear2.x,bear2.y)
        inv1.visible=True
        inv.visible=False
    if keys.Pressed[K_UP]:
        bear2.y-=7
        bear21.y-=7
    if keys.Pressed[K_DOWN]:
        bear2.y+=7
        bear21.y+=7
    if keys.Pressed[K_SPACE] and inv1.collidedWith(bear2):                
        b.visible=True
        b.moveTo(bear2.x+85,bear2.y-26)
        
    if keys.Pressed[K_SPACE] and inv.collidedWith(bear21):
        b1.visible=True
        b1.moveTo(bear21.x-85,bear21.y-26)
        b1.move()
    #bullet collition
    if b.collidedWith(zom):
        b.visible=False
        zom.visible=False
        bear2.health-=25
        game.score+=1
    if b.collidedWith(jel):
        b.visible=False
        jel.visible=False
        bear2.health-=25
        game.score+=1
    if b.collidedWith(pok):
        b.visible=False
        pok.visible=False
        bear2.health-=25
        game.score+=1
    if b.collidedWith(pok1):
        b.visible=False
        pok1.visible=False
        bear2.health-=25
        game.score+=1
  #different bullet
    if b1.collidedWith(zom):
        b1.visible=False
        zom.visible=False
        bear2.health-=25
        game.score+=1
    if b1.collidedWith(jel):
        b1.visible=False
        jel.visible=False
        bear2.health-=25
        game.score+=1
    if b1.collidedWith(pok):
        b1.visible=False
        pok.visible=False
        bear2.health-=25
        game.score+=1
    if b1.collidedWith(pok1):
        b1.visible=False
        pok1.visible=False
        bear2.health-=25
        game.score+=1
        
    #win
    if game.score>3:
        bear3.resizeBy(pct)
        bear3.visible=True
        bear3.move()
        bear21.visible=False
        bear2.visible=False
        b.visible=False
        b1.visible=False
        
        

    game.drawText("Kills:"+str(game.score),3,3,f2)
    zom.move(True)
    jel.move(True)
    pok.move(True)
    pok1.move(True)
    bk3.draw()
    go.draw()
    if mouse.collidedWith(rs) and mouse.LeftClick:
        bk3.visible=False
        go.visible=False
        rs.visible=False
        pok1.visible=True
        zom.visible=True
        jel.visible=True
        pok.visible=True
        bear2.health=100
        bear21.moveTo(60,50)
        bear2.moveTo(60,50)
        zom.moveTo(700,100)
        jel.moveTo(100,500)
        pok.moveTo(700,500)
        pok1.moveTo(700,100)
        game.score=0

    #over screen
    if bear2.collidedWith(zom)or bear2.collidedWith(jel)or bear2.collidedWith(pok)or bear2.collidedWith(pok1):
        go.visible=True
        bk3.visible=True
        rs.visible=True
        
    if bear21.collidedWith(zom)or bear21.collidedWith(jel)or bear21.collidedWith(pok)or bear21.collidedWith(pok1):
        go.visible=True
        bk3.visible=True
        rs.visible=True
    if game.score>3 and bear3.isOffScreen("top"):
        game.over=True
    rs.draw()
    bear21.draw()
    game.update(30)
    game.over 
game.over=False

#transition 2
bk3=Image("images//bk3.jpg",game)
bk3.moveTo(200,300)
arrow2=Image("images//arrow2.png",game)
arrow2.resizeBy(-30)
arrow2.moveTo(700,530)
dia=Image("images//dia.png",game)
dia.moveTo(300,350)
water.moveTo(-200,530)
bear.moveTo(150,510)
bear.setSpeed(4,270)
while not game.over:
    
    game.processInput()
    bk3.draw()
    dia.draw()
    arrow2.draw()
    bear.draw()
    if mouse.collidedWith(arrow2) and  mouse.LeftClick:
        game.over=True
    game.update(30)
    game.over 
game.over=False


while not game.over:
    game.processInput()
    bk3.draw()
    bear.x+=10
    bear.nextFrame()
    if bear.isOffScreen("right"):
        game.over=True
    game.update(30)
    game.over 
game.over=False

pl1=Image("images//pl1.png",game)
pl1.moveTo(400,500)
pl1.resizeBy(-20)
pl2=Image("images//pl2.png",game)
pl2.moveTo(150,500)
pl3=Image("images//pl3.png",game)
pl3.moveTo(400,300)
pl4=Image("images//pl4.png",game)
pl4.moveTo(650,500)
pl5=Image("images//pl5.png",game)
pl5.moveTo(570,150)
pl6=Image("images//pl6.png",game)
pl6.moveTo(250,150)
pl6.resizeBy(-20)
bear4=Animation("images//bg.png",16,game,827/4,620/4)
bear4.resizeBy(-40)
b=Image("images//123.png",game)
b.visible=False
b.setSpeed(20,270)
b.resizeBy(-95)
b1=Image("images//1234.png",game)
b1.visible=False
b1.setSpeed(20,90)
b1.resizeBy(-95)
inv=Image("images//invis.png",game)
inv.resizeBy(80)
inv1=Image("images//invis.png",game)
inv1.resizeBy(80)
bear41=Animation("images//bg2.png",16,game,827/4,620/4)
bear41.resizeBy(-40)
bear41.visible=False
h=Animation("images//human.png",13,game,464/13,44)
h.resizeBy(120)
go3=Image("images//game-over.png",game)
go3.visible=False
go3.resizeTo(800,600)
bear4.moveTo(400,400)
wa=Image("images//warrow.png",game)
wa.resizeBy(-80)
wa.setSpeed(7,90)

#level 3
while not game.over:
    game.processInput()
    bk3.draw()
    pl1.draw()
    pl2.draw()
    pl3.draw()
    pl4.draw()
    pl5.draw()
    pl6.draw()
    bear4.draw()
    bear41.draw()
    go3.draw()
    b.draw()
    b1.draw()
    h.move(True)

    #arrow
    wa.moveTo(h.x-30,h.y)
    if wa.isOffScreen("left"):
        wa.moveTo(h.x-30,h.y)
    if wa.collidedWith(bear4) or wa.collidedWith(bear41):
        bear4.health-=10
        wa.moveTo(h.x-30,h.y)
    if bear4.health<0:
        game.over=True

    
    #move
    if keys.Pressed[K_LEFT]:
        bear4.x-=7
        bear4.visible=False
        bear41.visible=True
        bear41.x-=7
        bear41.moveTo(bear4.x,bear4.y)
        inv.moveTo(bear41.x,bear41.y)
        inv.visible=True
        inv1.visible=False
    if keys.Pressed[K_RIGHT]:
        bear4.x+=7
        bear41.x+=7
        bear41.visible=False
        bear4.visible=True
        inv1.moveTo(bear4.x,bear4.y)
        inv1.visible=True
        inv.visible=False
    if keys.Pressed[K_SPACE] and inv1.collidedWith(bear4):                
        b.visible=True
        b.moveTo(bear4.x+85,bear4.y-26)
        b.move()
    if keys.Pressed[K_SPACE] and inv.collidedWith(bear41):
        b1.visible=True
        b1.moveTo(bear41.x-85,bear41.y-26)
        b1.move()
    

    
    #over
    if bear4.isOffScreen("bottom"):
        go3.visible=True
        game.drawText("(Click to restart)",300,470,f2)
        bear4.visible=False
        bear41.visible=False
        pl1.visible=False
        pl2.visible=False
        pl3.visible=False
        pl4.visible=False
        pl5.visible=False
        pl6.visible=False
        h.visible=False
        b.visible=False
        b1.visible=False
    #return
    if mouse.collidedWith(go3) and mouse.LeftClick:
        go3.visible=False
        pl1.visible=True
        pl2.visible=True
        pl3.visible=True
        pl4.visible=True
        pl5.visible=True
        pl6.visible=True
        bear4.visible=True
        h.visible=True
        bear41.visible=True
        h.health=100
        bear4.health=100
        bear4.moveTo(400,300)
        bear4.moveTo(400,300)
    if b.collidedWith(h) or b1.collidedWith(h):
        b.visible=False
        b1.visible=False
        h.health-=5

    
    game.drawText("Health:"+str(bear4.health),bear4.x+50,bear4.y,f)
    game.drawText("Health:"+str(h.health),h.x+50,h.y,f)



    
#we're trying to have the bear land on the platform
    



    
    
    game.update(30)
    game.over
game.over=False

penguin=Animation("images//penguin.png",20,game,1480/4,1500/5)
penguin.resizeBy(-35)
penguin.moveTo(500,480)
diae=Image("images//dia_end.png",game)
diae.moveTo(300,310)
diae.resizeBy(-20)
diae.visible=False
diae2=Image("images//dia_end2.png",game)
diae2.resizeBy(-40)
diae2.moveTo(600,310)
diae2.visible=False
bear.moveTo(100,510)
bear.visible=True
subB=Image("images//subB.png",game)
subB.moveTo(370,510)
subB.visible=False
end=Image("images//The-End.jpg",game)
end.resizeTo(800,600)
while not game.over:
    game.processInput()
    bk3.draw()
    bear.nextFrame()
    bear.x+=10
    if bear.x>370:
        bear.x=370
        diae.visible=True
        diae2.visible=True
        bear.visible=False
        subB.visible=True
    penguin.draw()
    diae.draw()
    diae2.draw()
    subB.draw()
    game.score+=1
    if game.score>165:
        game.over=True
    game.update(30)
    game.over
game.over=False

while not game.over:
    game.processInput()
    end.draw()
    game.update(30)
game.quit()

