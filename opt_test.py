from optparse import OptionParser
import sys


def test(fuck):
    parser = OptionParser()
    parser.add_option("-i", dest="ip", help="Do something fuck ip", metavar="FILE")
    parser.add_option("-s", "--scan", dest="sc", help="Scan VxWorks devices", default=False, action="store_true")

    (options, args) = parser.parse_args(fuck)

    if options.ip:
    	print 1
    	print options.ip

    if options.sc:
    	print 2
    	print options.sc
    	print fuck


sys.argv
print sys.argv
test(sys.argv[1:])