import pygame
pygame.init()
screen = pygame.display.set_mode((600,300))
pygame.display.set_caption('Dinosaur')
#Đặt màu
WHITE=(255,255,255)
RED=(255,0,0)
#Đặt tọa độ vật thể
background_x=0
background_y=0
dinosaur_x=0
dinosaur_y=230
tree_x=550
tree_y=230
#độ cao khi con khủng long nhảy
x_velocity=5
y_velocity=7
#Điểm_Cỡ chữ
score=0
font=pygame.font.SysFont('san',20)
font1=pygame.font.SysFont('san',40)
#set ảnh background
background=pygame.image.load('background.jpg')
dinosaur=pygame.image.load('dinosaur.png')
tree=pygame.image.load('tree.png')
#âm thanh
sound1=pygame.mixer.Sound('tick.wav')
sound2=pygame.mixer.Sound('te.wav')
#biến tốc độ chụp ảnh trong 1 khoảng thời gian
clock=pygame.time.Clock()
#các biến
pausing=False
jump=False
running=True
#while Loop
while running:
    clock.tick(60)#PDF
    #tạo trên màn hình background
    screen.fill(WHITE)
    background1_rect=screen.blit(background,(background_x,background_y))
    background2_rect=screen.blit(background,(background_x+600,background_y))
    #tạo điểm trên màn hình
    score_txt=font.render("Score:"+str(score),True,RED)
    screen.blit(score_txt,(5,5))
    #các điều kiện chạy 
    #lặp background
    background_x-=x_velocity
    if background_x+600<=0:
        background_x=0
    #lặp cây
    tree_x-=x_velocity
    if tree_x<=-20:
        tree_x=550  #có thể thu hẹp khoảng cách cây-=
        score+=1#tính điểm
    if 230>=dinosaur_y>=80:#cho khủng long nhảy
        if jump==True:
            dinosaur_y-=y_velocity
    else:
        jump=False
    if dinosaur_y<230:
        if jump==False:
            dinosaur_y+=y_velocity #có thể thêm trọng lực để rơi nhanh dần   
    #tạo không gian hình chữu nhật xung quanh cây và khủng long
    dinosaur_rect=screen.blit(dinosaur,(dinosaur_x,dinosaur_y))
    tree_rect=screen.blit(tree,(tree_x,tree_y))
    #xét va chạm của cây với khủng long
    if dinosaur_rect.colliderect(tree_rect):
        pygame.mixer.Sound.play(sound2)#âm thanh khi va chạm
        pausing=True
        gameover_txt=font1.render("GAME OVER:",True,RED)
        screen.blit(gameover_txt,(200,150))
        x_velocity=0
        y_velocity=0
    #event
    for event in pygame.event.get():
        if event.type==pygame.QUIT:#cài phím thoát game
            running=False
        if event.type==pygame.KEYDOWN:#cài phím nhảy == Space x1
            if event.key==pygame.K_SPACE:
                if dinosaur_y==230:
                    pygame.mixer.Sound.play(sound1)#âm thanh khi nhảy
                    jump=True
                if pausing:#khi khủng long va chạm với cây thì setup lại game về như ban đầu
                    background_x=0
                    background_y=0
                    dinosaur_x=0
                    dinosaur_y=230
                    tree_x=550
                    tree_y=230
                    x_velocity=5
                    y_velocity=7
                    score=0
                    pausing=False
    pygame.display.flip()
pygame.quit()