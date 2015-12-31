import argparse



def parse_args():
    parser = argparse.ArgumentParser(
        description='hello world')
    parser.add_argument('strings', metavar='8.8.8.8', type=str, nargs='+',
    	help='print ip in here')
    parser.add_argument('-i',dest='findip',
    	help='want to find ip')
    
    args = parser.parse_args()
    if args.strings:
    	print args.strings





parse_args()