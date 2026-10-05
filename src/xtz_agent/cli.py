import argparse
import json
from .kb import KnowledgeBase
from .router import route

def main():
    parser = argparse.ArgumentParser(prog="xtz-agent")
    sub = parser.add_subparsers(dest="cmd")
    p_route = sub.add_parser("route")
    p_route.add_argument("text", nargs="+")
    p_search = sub.add_parser("search")
    p_search.add_argument("text", nargs="+")
    p_part = sub.add_parser("part")
    p_part.add_argument("part_number")
    args = parser.parse_args()
    kb = KnowledgeBase()

    if args.cmd == "route":
        print(route(" ".join(args.text)))
    elif args.cmd == "search":
        print(json.dumps(kb.search(" ".join(args.text)), ensure_ascii=False, indent=2))
    elif args.cmd == "part":
        print(json.dumps(kb.part(args.part_number), ensure_ascii=False, indent=2))
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
