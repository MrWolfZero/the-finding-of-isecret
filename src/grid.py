from src.constants import WIDTH, HEIGHT, special_rooms

def GridMaker():
    with open("map.txt", "w") as mapfile:
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if j not in range(WIDTH-1, WIDTH*HEIGHT, WIDTH):
                    mapfile.write("0 | ")
                else:
                    mapfile.write("0\n")

def MapToStr(map_path):
    with open(map_path, "r") as format_map:
        mapstr = format_map.read()
        mapstr = mapstr.split(" | ")
        for idx, i in enumerate(mapstr):    
            i = i.replace(" | ", "")
            i = i.replace("\n", "")
            mapstr[idx] = i
        mapstr = "".join(mapstr)
    return mapstr

def StrToMap(map_sol, path_output):
    with open(path_output, "w+") as solution:
        for idx, i in enumerate(map_sol):
            if idx not in range(WIDTH-1, WIDTH*HEIGHT, WIDTH):
                solution.write(f"{i} | ")
            else:
                solution.write(f"{i}\n")