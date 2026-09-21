from src.constants import WIDTH, HEIGHT, special_rooms

def AdjChecker(map, room_num):
    row, col = divmod(room_num, WIDTH)
    bounds_type = [None,None,None,None]
    if col < WIDTH-1:
        bounds_type[0] = map[room_num+1]
    if row > 0:
        bounds_type[1] = map[room_num-WIDTH]
    if col > 0:
        bounds_type[2] = map[room_num-1]
    if row < HEIGHT-1:
        bounds_type[3] = map[room_num+WIDTH]
    return bounds_type

def SRoomFinder(maptxt):
    map_sol_secret = []
    for room in range(len(maptxt)):
        if maptxt[room] == "0":
            num = 0
            bounds_info = AdjChecker(maptxt,room)
            if "B" not in bounds_info:
                for adj in bounds_info:   
                    if adj in special_rooms or adj == "X":
                        num += 1
            map_sol_secret.append(num)
        else:
            map_sol_secret.append(maptxt[room])
    return map_sol_secret

def SupSRoomFinder(maptxt):
    map_sol_sup_secret = []
    for room in range(len(maptxt)):
        if maptxt[room] == "0":
            bounds_info = AdjChecker(maptxt,room)
            if not any(adj in special_rooms for adj in bounds_info) and bounds_info.count("X") == 1:
                map_sol_sup_secret.append("1")
            else:
                map_sol_sup_secret.append("0")
        else:
            map_sol_sup_secret.append(maptxt[room])
    return map_sol_sup_secret
