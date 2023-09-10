import pygame

 

# 스크린 전체 크기 지정

SCREEN_WIDTH = 400
SCREEN_HEIGHT  = 500

 

# pygame 초기화

pygame.init()

 

# 스크린 객체 저장
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("pygame test")

 

# FPS를 위한 Clock 생성
clock = pygame.time.Clock()

 

# 이미지 로딩 및 크기 변경

player = pygame.image.load("C:\Downloads\\23_mega_python3_project-main\김강희\image\dino\idle_0.png")
player = pygame.transform.scale(player, (40, 102))

 

# 이미지의 Rect 정보를 저장

player_Rect = player.get_rect()

 

# 이미지가 가운데 올 수 있도록 좌표값 수정

# python 3.8 이상에서 integer가 필요한 곳에 float가 들어가면 DeprecationWarning이 나옴.

# 따라서 round() 처리를 해준다.

player_Rect.centerx = round(SCREEN_WIDTH / 2)

player_Rect.centery = round(SCREEN_HEIGHT / 2)

 

dx = 0

dy = 0

 

# 마우스로 이미지를 옮기기 위한 flag

MOVE = False

 

playing = True
while playing:

    # 이벤트 처리
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()

 

        # 마우스 버튼이 눌렸을 때
        if event.type == pygame.MOUSEBUTTONDOWN:
            # 마우스의 이동 경로를 위해 get_rel() 메서드를 호출한다. 첫 호출값은 (0,0)
            pygame.mouse.get_rel()         

            # 마우스의 포지션을 받아서 mouse_pos에 저장

            mouse_pos = pygame.mouse.get_pos()

            # 마우스 포지션이 image의 Rect 안에 들어오는지 체크           

            # mouse_pos[0]은 x, mouse_pos[1]은 y 좌표값.
            if mouse_pos[0] > player_Rect.left and mouse_pos[0] < player_Rect.right and mouse_pos[1] > player_Rect.top and mouse_pos[1] < player_Rect.bottom:

                # 마우스 포지션이 Image의 Rect안에 있으면 MOVE를 True로 전환
                MOVE = True

                # 마우스 커서의 모양을 깨진 X 모양으로 변경
                pygame.mouse.set_cursor(*pygame.cursors.broken_x)

 

 

        # 마우스 버튼이 올라갔을 때
        if event.type == pygame.MOUSEBUTTONUP:
            # Image가 이동하면 안되므로 MOVE는 False로
            MOVE = False

            # 마우스 커서의 모양을 기본값인 화살표 모양으로 변경
            pygame.mouse.set_cursor(*pygame.cursors.arrow)

 

 

        # 마우스가 SCREEN안에서 움직일 때

        if event.type == pygame.MOUSEMOTION:
            # 이미지 위치 안에서 마우스가 클릭되고, 이후 왼쪽 마우스 버튼이 누른 상태에 있을 때 Image를 이동한다.
            if MOVE:
                # 마우스 버튼의 상태를 받아서 저장. x=왼쪽 버튼, y=가운데버튼(휠), z=오른쪽 버튼

                x, y, z = pygame.mouse.get_pressed()                 

                # 왼쪽 마우스버튼이 눌려있는 상태일 때
                if x:
                    # 마우스의 이동 양을 받음
                    mx, my = pygame.mouse.get_rel()
                    # 마우스의 이동량만큼 Image도 같이 이동 시킴
                    player_Rect.x += mx
                    player_Rect.y += my

 

 

        # 키가 눌렸을 때

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -5
            if event.key == pygame.K_RIGHT:
                dx = 5

            if event.key == pygame.K_UP:
                dy = -5
            if event.key == pygame.K_DOWN:
                dy = 5

 

        # 키가 떼졌을 때
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_RIGHT:
                dx = 0

            if event.key == pygame.K_UP:
                dy = 0
            if event.key == pygame.K_DOWN:
                dy = 0

 

    # 스크린 배경색 칠하기

    SCREEN.fill((255, 255, 255))

 

    # 키에 의해 증가된 값을 이미지의 좌표에 적용시킨다.

    player_Rect.x += dx

    player_Rect.y += dy

 

    # 왼쪽으로 벗어나는 것 방지

    if player_Rect.left < 0:
        player_Rect.left = 0

 

    # 오른쪽으로 벗어나는 것 방지

    if player_Rect.right > SCREEN_WIDTH:
        player_Rect.right = SCREEN_WIDTH

 

    # 위쪽으로 벗어나는 것 방지

    if player_Rect.top < 0:
        player_Rect.top = 0

 

    # 아래쪽으로 벗어나는 것 방지

    if player_Rect.bottom > SCREEN_HEIGHT:
        player_Rect.bottom = SCREEN_HEIGHT

 

    # 스크린의 원하는 좌표에 이미지 복사하기, 좌표값은 Rect를 이용

    SCREEN.blit(player, player_Rect)

 

    # 작업한 스크린의 내용을 갱신하기

    pygame.display.flip()

 

    # 1초에 60번의 빈도로 순환하기

    clock.tick(60)