#!/bin/bash
echo url="https://www.duckdns.org/update?domains=rpi0&token=41a8929a-f39d-4ef1-9439-b8c0d20ed5f2&ip=" | curl -k -o /var/log/duckdns/duck.log -K -
