clear
sleep 1
echo -e "

\033[33m▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓       \033[31m ██▓     ▒█████   ▒█████   ██ ▄█▀ █    ██  ██▓███  
\033[33m▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒       \033[31m▓██▒    ▒██▒  ██▒▒██▒  ██▒ ██▄█▒  ██  ▓██▒▓██░  ██▒
\033[33m▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░       \033[31m▒██░    ▒██░  ██▒▒██░  ██▒▓███▄░ ▓██  ▒██░▓██░ ██▓▒
\033[33m▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░       \033[31m▒██░    ▒██   ██░▒██   ██░▓██ █▄ ▓▓█  ░██░▒██▄█▓▒ ▒
\033[33m░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒   \033[31m░██████▒░ ████▓▒░░ ████▓▒░▒██▒ █▄▒▒█████▓ ▒██▒ ░  ░
\033[33m░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░   \033[31m░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░▒░▒░ ▒ ▒▒ ▓▒░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
\033[33m ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░   \033[31m░ ░ ▒  ░  ░ ▒ ▒░   ░ ▒ ▒░ ░ ░▒ ▒░░░▒░ ░ ░ ░▒ ░     
\033[33m   ░   ░      ░     ░   ▒    ▒ ░  ░ ░      \033[31m  ░ ░   ░ ░ ░ ▒  ░ ░ ░ ▒  ░ ░░ ░  ░░░ ░ ░ ░░       
\033[33m   ░  ░       ░         ░  ░ ░      ░  ░    \033[31m   ░  ░    ░ ░      ░ ░  ░  ░      ░           

"
echo -e "\e[32m Code by \033[33mBlackCage"
echo ""
echo -e -n "\e[32mIntroduzca la direccion de correo:\033[36m "
read -r correo
sleep 1
echo -e "\e[32mDatos de la direccion de correo:"
sleep 3

w3m -dump https://ipqualityscore.com/api/json/email/dTcf3CzoQ68QOMxSbGGAGXu3mRIlQVG0/$correo

sleep 5
echo ""
echo -e "\033[36mFinalizando Módulo"
sleep 1.5