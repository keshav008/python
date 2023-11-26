from logging import*
log_format='{lineno}***{name}***{asctime}***{message}'
basicConfig(filename='logfile.log',level=DEBUG,filemode='w',style='{',format=log_format)
debug("this is dubug in w mode")
info("this is info")
warning("this is warning")
error("this is error")
critical("this is critical")
exception("this is exception")
