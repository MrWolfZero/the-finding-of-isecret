import argparse
from pathlib import Path
from src.app import SRoomFinder, SupSRoomFinder
from src.grid import MapToStr, StrToMap

def ParseArgs():
    parser = argparse.ArgumentParser(
        prog="TBOI Secret Room Finder",
        description="Your reliable and quite slow to use Secret Room Finder!"
        )
    parser.add_argument(
        "map_path",
        type=Path,
        default=Path("map.txt"),
        help="Path to the input map.txt file"
    )
    parser.add_argument(
        "room_type", 
        help="Room type to search for: S=Secret, D=Super Secret, U=Ultra Secret",
        type=str,
        choices=["S", "D", "U"]
        )
    parser.add_argument(
            "-d", "--destination",
            type=Path,
            default=Path("mapsolved.txt"),
            help="Path to write the solved map (default: mapsolved.txt)"
        )
    return parser.parse_args()

def Main():
    args = ParseArgs()
    if not args.map_path.exists():
        raise SystemExit(f"Error: {args.map_path} does not exist")
    
    finders = {
        "S": SRoomFinder,
        "D": SupSRoomFinder,
        "U": None,  #UltraRoomFinder (not built yet)
    }
    finder_fn = finders[args.room_type]
    if finder_fn is None:
        raise SystemExit(f"{args.room_type} finder not found. Type -h for options")

    mapstr = MapToStr(args.map_path)
    solved = finder_fn(mapstr)
    StrToMap(solved, args.destination)

    print("Beep boop beep boop, finding secret rooms, please wait\nJust kidding this is just a print()... Found!")

Main()