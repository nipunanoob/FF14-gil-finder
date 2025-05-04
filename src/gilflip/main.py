import argparse
import os
import sys
import json
from scanner import find_flippable_item

# CONFIG_PATH = os.path.expanduser("~/.gilflippa/config.json")
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return json.load(f)
    else:
        return {}

DEFAULTS = {
    "preferred_roi": 10,
    "min_profit_amount": 10000,
    "min_desired_avg_ppu": 10000,
    "min_stack_size": 1,
    "hours_ago": 48,
    "min_sales": 2,
    "hq": False,
    "home_server": "Spriggan",
    "region_wide": False,
    "include_vendor": True,
    "show_out_stock": True,
}

def resolve_arg(key, cli_val, config, default):
    return cli_val if cli_val is not None else config.get(key, default)

def main():
    config = load_config()
    parser = argparse.ArgumentParser(prog="gil-flipper")

    parser.add_argument("--roi", type=int, help="Preferred ROI percentage")
    parser.add_argument("--mprof", type=int, help="Minimum profit amount in gil per item")
    parser.add_argument("--mappu", type=int, help="Minimum desired average price per unit")
    parser.add_argument("-s", type=int, help="Minimum item stack size")
    parser.add_argument("-t", type=int, help="Sales Time period in hours")
    parser.add_argument("--min-sales", type=int,help="Minimum number of sales in the time period")
    parser.add_argument("--hq", action="store_true", help="Show hq items only")
    parser.add_argument("--home", help="Select home server")
    parser.add_argument("-d", action="store_true",help="Show items from other datacenters in your region")
    parser.add_argument("-v", action="store_true", help="Show vendor items to flip")
    parser.add_argument("--out-of-stock", action="store_true",help="Show items out of stock in your server")

    if "-h" in sys.argv or "--help" in sys.argv:
        parser.print_help()
    else:
        try:
            args = parser.parse_args()
            payload = {
                "preferred_roi": resolve_arg("preferred_roi", args.roi, config, DEFAULTS["preferred_roi"]),
                "min_profit_amount": resolve_arg("min_profit_amount", args.mprof, config, DEFAULTS["min_profit_amount"]),
                "min_desired_avg_ppu": resolve_arg("min_desired_avg_ppu", args.mappu, config, DEFAULTS["min_desired_avg_ppu"]),
                "min_stack_size": resolve_arg("min_stack_size", args.s, config, DEFAULTS["min_stack_size"]),
                "hours_ago": resolve_arg("hours_ago", args.t, config, DEFAULTS["hours_ago"]),
                "min_sales": resolve_arg("min_sales", args.min_sales, config, DEFAULTS["min_sales"]),
                "hq": resolve_arg("hq", args.hq, config, DEFAULTS["hq"]),
                "home_server": resolve_arg("home_server", args.home, config, DEFAULTS["home_server"]),
                "region_wide": resolve_arg("region_wide", args.d, config, DEFAULTS["region_wide"]),
                "include_vendor": resolve_arg("include_vendor", args.v, config, DEFAULTS["include_vendor"]),
                "show_out_stock": resolve_arg("show_out_stock", args.out_of_stock, config, DEFAULTS["show_out_stock"]),
            }
        except SystemExit:
            print("Invalid arguments! Use -h or --help to see available options")
            sys.exit(1)



if __name__ == '__main__':
    main()