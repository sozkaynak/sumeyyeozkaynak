[0;1;32m●[0m gunicorn.service - gunicorn daemon
   Loaded: loaded (/etc/systemd/system/gunicorn.service; enabled; vendor preset: enabled)
   Active: [0;1;32mactive (running)[0m since Tue 2018-07-24 10:18:08 UTC; 3 days ago
 Main PID: 1442 (gunicorn)
   CGroup: /system.slice/gunicorn.service
           ├─1442 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/python3 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak.sock sumeyyeozkaynak.wsgi:application
           ├─1598 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/python3 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak.sock sumeyyeozkaynak.wsgi:application
           ├─1599 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/python3 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak.sock sumeyyeozkaynak.wsgi:application
           └─1601 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/python3 /home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/sumeyyeozkaynak/dp-sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak/sumeyyeozkaynak.sock sumeyyeozkaynak.wsgi:application

Jul 27 01:52:17 try systemd[1]: Started gunicorn daemon.
Jul 27 01:52:47 try systemd[1]: Started gunicorn daemon.
Jul 27 01:56:34 try systemd[1]: Started gunicorn daemon.
Jul 27 01:59:42 try systemd[1]: Started gunicorn daemon.
Jul 27 22:51:31 try systemd[1]: Started gunicorn daemon.
Jul 27 22:52:24 try systemd[1]: Started gunicorn daemon.
Jul 27 22:54:17 try systemd[1]: Started gunicorn daemon.
Warning: Journal has been rotated since unit was started. Log output is incomplete or unavailable.
