# -*- coding: utf-8 -*-
import argparse
import re
import pdb
import os
import threading
import logging
import time
import commands

#A logging is created for display messages about server, if exists
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] - %(threadName)-10s: \
%(message)s')

def arguments():
    """
    arguments method is responsible for extracting arguments required by the user
    """
    parser = argparse.ArgumentParser() 
    parser.add_argument("-lf", "--logfile", help="Path log file", required=True)
    parser.add_argument("-o", "--outfile", help="Path HTML out", default='./')
    parser.add_argument("-r", "--runserver", type=bool, help="Run Server Localhost", default=False)
    parser.add_argument("-p", "--port", help="Server Port", default='4444')
    args = parser.parse_args()

    if( args.logfile is None):
        print "Must be specified a path with log file"
        quit()

    if( args.runserver not in (True, False) ):
        print "The argument runserver must be True or False"
        quit()

    if(args.runserver):
        outfile = './'
        if( args.outfile != './' or args.outfile != '.'):
            print "The outfile argument is ignored when runserver argument is True"
    else:
        outfile = args.outfile

    infile = args.logfile
    port = args.port
    runserver = args.runserver
    return infile, outfile, runserver, port

def open_logfile(infile):
    dircurrent = commands.getoutput('pwd')
    dircurrent = dircurrent + '/' + infile
    with open(infile, 'r') as f:
        logfile_str = f.read()
        f.close()
    return logfile_str

def logstr_to_loghtml(logfile_str):

    logfile_html = logfile_str

    search_info = re.compile(r" INFO ")
    logfile_html = re.sub(search_info," <b class='info'>INFO</b> ",logfile_html)

    search_warning = re.compile(r" WARNING ")
    logfile_html = re.sub(search_warning," <b class='warning'>WARNING</b> ",logfile_html)

    search_error = re.compile(r" ERROR ")
    logfile_html = re.sub(search_error," <b class='error'>ERROR</b> ",logfile_html)

    search_test = re.compile(r" TEST ")
    logfile_html = re.sub(search_test," <b class='test'>TEST</b> ",logfile_html)

    search_critical = re.compile(r" CRITICAL ")
    logfile_html = re.sub(search_critical," <b class='critical'>CRITICAL</b> ",logfile_html)

    search_debug = re.compile(r" DEBUG ")
    logfile_debug = re.sub(search_debug," <b class='debug'>DEBUG</b> ",logfile_html)

    return logfile_html

def get_html_header(runserver):

    if runserver: 
        return '<html> <head> <link rel="stylesheet" media="screen" \
        href="openerp_log.css"><meta http-equiv="content-Type" content="text/html; charset=utf-8" /> <META HTTP-EQUIV="REFRESH" CONTENT="5;URL=log.html"></head> \
        <body> <pre>'
    else:
        return '<html> <head> <link rel="stylesheet" media="all" \
        href="/usr/local/lib/python2.7/dist-packages/oerplog/openerp_log.css"> <META HTTP-EQUIV="REFRESH" \
        CONTENT="1;URL=log.html"></head> \
        <body> <pre>'


def get_html_footer():
    return '</pre> </body> </html>'

def save_loghtml(logfile_html, outfile, runserver):
    dircurrent = commands.getoutput('pwd')
    outfile = dircurrent + '/' + outfile
    outfile += 'log.html'

    head = get_html_header(runserver)
    foot = get_html_footer()
    with open(outfile, 'w') as f:
        f.write(head + logfile_html + foot)
        f.close()

def get_openerp_log_css(outfile):
    dircurrent = commands.getoutput('pwd')
    outfile = dircurrent + '/' + outfile
    os.system('cp /usr/local/lib/python2.7/dist-packages/oerplog/openerp_log.css %s' % outfile)
    pass

def main(infile, outfile, runserver, num):
    if num != 0:
        time.sleep(3)
    logfile_str = open_logfile(infile)
    logfile_html = logstr_to_loghtml(logfile_str)
    res = save_loghtml(logfile_html, outfile, runserver)
    if num == 0 and runserver:
        get_openerp_log_css(outfile)
    return num + 1

def run_server(port):
    os.system('python -m SimpleHTTPServer %s' % (port))

def run():

    infile, outfile, runserver, port = arguments()
    w = threading.Thread(target=run_server, name='Server', args=(port, ) )
    num = 0
    print "Loading log.html..."
    while(True):
        num = main(infile, outfile, runserver, num)
        if num == 1:
            if runserver:
                logging.info('Running Server locahost:%s/log.html...' % (port))
                w.start()
                os.system('xdg-open http://localhost:%s/log.html' % (port))
            else:
                logging.info('Running log.html...')
                os.system('xdg-open log.html &')

if __name__ == '__main__':
    run()
