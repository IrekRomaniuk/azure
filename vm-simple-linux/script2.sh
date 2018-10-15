#!/bin/bash
echo "* * * * * /bin/ping 10.34.1.1 -c 3" | crontab -
python $1