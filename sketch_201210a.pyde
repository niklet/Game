menu=True
speedx=5
speedy=5
dim=50
game=False
gamestart=False
setting=False
gameprocess=False
blocks=[]
ballw=306
ballh=130
ballcw=306
ballch=130
ballsw=306
ballsh=130
collorr=100
class Block:
    def __init__(self,xblock,yblock,imageblock):
        self.x=xblock
        self.y=yblock
        self.img=imageblock
def setup():
    global x,y
    for i in range(10):
        blocks.append(Block(192*i,30,loadImage("BlockO.png")))
    for j in range (10):
        blocks.append(Block(192*j,110,loadImage("BlockG.png")))
    for g in range (10):
        blocks.append(Block(192*g,190,loadImage("BlockB.png")))
    size(1920,1000)
    x=width/2
    y=height-80#(75 размер картинки платформы + высота платформы + 2 во избежание ошибок)


def draw():
    
    global menu,game,gamestart,speedx,speedy,x,y,setting,menux,block1,dim,gameprocess,ballh,ballw,ballcw,ballch,ballsw,ballsh,collorr
    background1 = loadImage("Background.jpg")
    image(background1,0,0)
    menux=width/2-153#(153=половина ширины изображения)
    platformy=height-33#33 длинна платформы
  
    
    #Меню
    if menu == True:
        if menux+306>mouseX>menux and 280>mouseY>150:
            image(loadImage("StartR.png"),menux,150)
        else:
            image(loadImage("StartB.png"),menux,150)
        if menux+306>mouseX>menux and 580>mouseY>450:
            image(loadImage("SettingsR.png"),menux,450)
        else:
            image(loadImage("SettingsB.png"),menux,450)
        if menux+306>mouseX>menux and 880>mouseY>750:
            image(loadImage("ExitR.png"),menux,750)
        else:
            image(loadImage("ExitB.png"),menux,750)
        #y подбирается по усмотрению

   
    
    #Подготовка к игре
    if game == True:
        image(loadImage("Platform1.png"),width/2-116,platformy)
        fill(collorr,0,0)
        ellipse(x,y,dim,dim)
    
    
    
    
    #Игра старт
    if gamestart == True:
        gameprocess=True
        game=False
        y=y-speedy
        x=x+speedx
        image(loadImage("Platform1.png"),mouseX-116,platformy)
        fill(collorr,0,0)
        ellipse(x,y,dim,dim)
        otskokrandm=random(-1,1)
        if dim/2>x or x>width-dim/2:
            speedx=-1*speedx#otskokrandm
        if height>y>height-34-dim/2 and x>mouseX-116 and x<mouseX+116 or y<dim/2:
            speedy=-1*speedy#otskokrandm
        if y+dim/2>height:
            image(loadImage("Lose.png"),775,441)
            gameprocess=False
        for i in range(len(blocks)):
            image(blocks[i].img,blocks[i].x+10,blocks[i].y)
        for i in range(len(blocks)):
            if blocks[i].x+160+dim/2>x>blocks[i].x-dim/2 and blocks[i].y+80+dim/2>y>blocks[i].y-dim/2:
                if blocks[i].y+60+dim/2>y>blocks[i].y-20-dim/2:
                    speedx=-1*speedx+otskokrandm
                    blocks.pop(i)
                    break
                else:
                    speedy=-1*speedy+otskokrandm
                    blocks.pop(i) 
                    break
                    
            
        if len(blocks)==0:
            image(loadImage("Win.png"),762,427)
        #Настройки
    if setting==True: #Стрелка 35,50
        if 1035>mouseX>1000 and 150<mouseY<200:
            image(loadImage("BallR.png"),200,150,ballw,ballh)
            image(loadImage("UpR.png"),1000,150)
            image(loadImage("DownB.png"),1000,230)
        else:
            image(loadImage("BallB.png"),200,150,ballw,ballh)
            image(loadImage("UpB.png"),1000,150)
            image(loadImage("DownB.png"),1000,230)
        if 1035>mouseX>1000 and 230<mouseY<280:
            image(loadImage("BallR.png"),200,150,ballw,ballh)
            image(loadImage("UpB.png"),1000,150)
            image(loadImage("DownR.png"),1000,230)
        if 1035>mouseX>1000 and 450<mouseY<500:
            image(loadImage("BallSR.png"),200,450,ballsw,ballsh)
            image(loadImage("UpR.png"),1000,450)
            image(loadImage("DownB.png"),1000,530)
        else:
            image(loadImage("BallSB.png"),200,450,ballsw,ballsh)
            image(loadImage("UpB.png"),1000,450)
            image(loadImage("DownB.png"),1000,530)
        if 1035>mouseX>1000 and 530<mouseY<580:
            image(loadImage("BallSR.png"),200,450,ballsw,ballsh)
            image(loadImage("UpB.png"),1000,450)
            image(loadImage("DownR.png"),1000,530)
            #
        if 1035>mouseX>1000 and 750<mouseY<800:
            image(loadImage("BallCR.png"),200,750,ballcw,ballch)
            image(loadImage("UpR.png"),1000,750)
            image(loadImage("DownB.png"),1000,830)
        else:
            image(loadImage("BallCB.png"),200,750,ballcw,ballch)
            image(loadImage("UpB.png"),1000,750)
            image(loadImage("DownB.png"),1000,830)
        if 1035>mouseX>1000 and 830<mouseY<880:
            image(loadImage("BallCR.png"),200,750,ballcw,ballch)
            image(loadImage("UpB.png"),1000,750)
            image(loadImage("DownR.png"),1000,830)

            


            
            
            
            

        



#Нажатие мыши
def mouseReleased():
    global game,menu,setting,menux,ballh,ballw,ballcw,ballch,ballsw,ballsh,dim,speedy,speedx,collorr
    #Управление в меню
    if menu==True:
        if mouseButton == LEFT and menux+306>mouseX>menux and 880>mouseY>750:#Выход
            exit()
        if mouseButton == LEFT and menux+306>mouseX>menux and 580>mouseY>450:#Настройки
            menu = False
            setting= True
        if mouseButton == LEFT and menux+306>mouseX>menux and 280>mouseY>150:#Переход к игре
            menu = False
            game = True
    #Управление в насройках
    if setting==True:
        if mouseButton == LEFT and 1035>mouseX>1000 and 150<mouseY<200:
            ballw=ballw+10
            ballh=ballh+5
            dim=dim+5
        if mouseButton == LEFT and 1035>mouseX>1000 and 230<mouseY<280:
            ballw=ballw-10
            ballh=ballh-5
            dim=dim-5
        if 1035>mouseX>1000 and 450<mouseY<500 and mouseButton == LEFT :
            ballsw=ballsw+10
            ballsh=ballsh+5
            speedy=speedy+5
            speedx=speedx+5
        if 1035>mouseX>1000 and 530<mouseY<580 and mouseButton == LEFT:
            ballsw=ballsw-10
            ballsh=ballsh-5
            speedy=speedy-5
            speedx=speedx-5        
        if 1035>mouseX>1000 and 750<mouseY<800 and mouseButton == LEFT: 
            ballcw=ballcw+10
            ballch=ballch+5
            collorr=collorr+25
        if 1035>mouseX>1000 and 830<mouseY<880 and mouseButton == LEFT:
            ballcw=ballcw-10
            ballch=ballch-5
            collorr=collorr-25
            
        




#Управление с клавиатуры
def keyReleased():
    global gamestart,menu,game,setting,x,y,speedy,speedx,gameprocess
    #Старт игры
    if key== ' ' and game==True:
        gamestart=True
    #перезапуск после проигрыша или захода после выхода
    if key== ' ' and gameprocess==False:
        x=width/2
        y=height-75
        speedy=-speedy
        speedx=speedx
    #Вернуться в меню   
    if key== 'q':
        menu = True
        game = False
        gamestart = False
        setting = False 


        

    
