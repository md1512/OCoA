import pygame

def whatchar(key):
        result=""
	if key[pygame.K_a]:
                result="A"
        if key[pygame.K_b]:
                result="B"
        if key[pygame.K_c]:
                result="C"
        if key[pygame.K_d]:
                result="D"
        if key[pygame.K_e]:
                result="E"
        if key[pygame.K_f]:
                result="F"
        if key[pygame.K_g]:
                result="G"
        if key[pygame.K_h]:
                result="H"
        if key[pygame.K_i]:
                result="I"
        if key[pygame.K_j]:
                result="J"
        if key[pygame.K_k]:
                result="K"
        if key[pygame.K_l]:
                result="L"
        if key[pygame.K_m]:
                result="M"
        if key[pygame.K_n]:
                result="N"
        if key[pygame.K_o]:
                result="O"
        if key[pygame.K_p]:
                result="P"
        if key[pygame.K_q]:
                result="Q"
        if key[pygame.K_r]:
                result="R"
        if key[pygame.K_s]:
                result="S"
        if key[pygame.K_t]:
                result="T"
        if key[pygame.K_u]:
                result="U"
        if key[pygame.K_v]:
                result="V"
        if key[pygame.K_w]:
                result="W"
        if key[pygame.K_x]:
                result="X"
        if key[pygame.K_y]:
                result="Y"
        if key[pygame.K_z]:
                result="Z"
        if key[pygame.K_0]:
                result="0"
        if key[pygame.K_1]:
                result="1"
        if key[pygame.K_2]:
                result="2"
        if key[pygame.K_3]:
                result="3"
        if key[pygame.K_4]:
                result="4"
        if key[pygame.K_5]:
                result="5"
        if key[pygame.K_6]:
                result="6"
        if key[pygame.K_7]:
                result="7"
        if key[pygame.K_8]:
                result="8"
        if key[pygame.K_9]:
                result="9"
        return result
