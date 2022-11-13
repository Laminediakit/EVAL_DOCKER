echo $(date '+%Y-%m-%d %H:%M:%S') >> log.txt
sleep 2
docker-compose up  >> log.txt
