Simple execution:
-----------------

    oerplog -lf <PATH-LOG>

Example:
    oerplog -lf openerp-server.log

openerp-server.log is a file generates by openerp server.
you can add to openerp server command the argument:
--logfile=<PATH-LOG>

Example for OpenERP server logfile argument:
--logfile=/home/openerp/logs/openerp-server.log

.. note ::

WARNING!

If outfile argument is not especified, the out files will be saved in ./ folder.
Out files can be index.html and/or openerp_log.css (This last is created when runserver
argument is True, by default is False)

Complicate Execution 1:
-----------------------

    oerplog -lf <PATH-LOG> -o <PATH-OUT-FOLDER>

Example:
    oerplog -lf openerp-server.log -o out_folder/

the out files (index.html) will be stored in out_folder.
When runserver is True (outfile are index.html and openerp_log.css), oerplog ignores outfile
argument and uses by default ./

Complicate Execution 2:
-----------------------

    oerplog -lf <PATH-LOG> -r True -p 8000

Example:

    oerplog -lf openerp-server.log -r True -p 8000

Will be runed a simple http server in port 8000. The out files will be stored in './' ever.
When runserver is True, oerplog ignores outfile argument.
