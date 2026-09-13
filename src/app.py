from src.constants import WIDTH, HEIGHT, special_rooms

def SRoomFinder(maptxt):
    map_sol_secret = []
    for room in range(len(maptxt)):
        if maptxt[room] == "0": 
            num = 0
            if room not in range(WIDTH-1, WIDTH*HEIGHT, WIDTH) and (maptxt[room+1] == "X" or maptxt[room+1] in special_rooms) and maptxt[room+1] != "B":
                num += 1
            if room not in range(0, WIDTH*HEIGHT, WIDTH) and (maptxt[room-1] == "X" or maptxt[room-1] in special_rooms) and maptxt[room-1] != "B":
                num += 1
            if room not in range(WIDTH*(HEIGHT-1), WIDTH*HEIGHT) and (maptxt[room+WIDTH] == "X" or maptxt[room+WIDTH] in special_rooms) and maptxt[room+WIDTH] != "B":
                num += 1
            if room not in range(0, WIDTH) and (maptxt[room-WIDTH] == "X" or maptxt[room-WIDTH] in special_rooms) and maptxt[room-WIDTH] != "B":
                num += 1
            if num == 1:
                map_sol_secret.append("0")
            else:
                map_sol_secret.append(num)
        else:
            map_sol_secret.append(maptxt[room])
    return map_sol_secret

def SupSRoomFinder(maptxt):
    map_sol_sup_secret = []
    for room in range(len(maptxt)):
        if maptxt[room] == "0": 
            x_num = 0
            s_num = 0
            if room != (WIDTH*HEIGHT)-1 and room not in range(WIDTH-1, WIDTH*HEIGHT, WIDTH):
                if maptxt[room+1] == "X":
                    x_num += 1
                elif maptxt[room+1] in special_rooms:
                    s_num += 1
            if room not in range(0, WIDTH*HEIGHT, WIDTH):
                if maptxt[room-1] == "X":
                    x_num += 1
                elif maptxt[room-1] in special_rooms:
                    s_num += 1
            if room not in range(WIDTH*(HEIGHT-1), WIDTH*HEIGHT):
                if maptxt[room+WIDTH] == "X":
                    x_num += 1
                elif maptxt[room+WIDTH] in special_rooms:
                    s_num += 1
            if room not in range(0, WIDTH): 
                if maptxt[room-WIDTH] == "X":
                    x_num += 1
                elif maptxt[room-WIDTH] in special_rooms:
                    s_num += 1
            if x_num > 1 or s_num > 0:
                map_sol_sup_secret.append("0")
            else:
                map_sol_sup_secret.append(x_num)
        else:
            map_sol_sup_secret.append(maptxt[room])
    return map_sol_sup_secret