all: unicast-sender unicast-receiver
CONTIKI_SOURCEFILES += sht11.c
APPS=servreg-hack serial-shell
CONTIKI=../../..

WITH_UIP6=1
UIP_CONF_IPV6=1
CFLAGS+= -DUIP_CONF_IPV6_RPL

include $(CONTIKI)/Makefile.include
