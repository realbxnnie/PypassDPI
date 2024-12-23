import pyfiglet, colorama, os;
import socket , requests

from dns import resolver

res = resolver.Resolver()

class PYPASSDPI:
    SOCKET = socket.socket()
    IP_ADDRESS = "127.0.0.1";
    PORT = 8080;
    WHITELIST = [
        "youtube.com",
        "youtu.be",
        "yt.be",
        "googlevideo.com",
        "ytimg.com",
        "ggpht.com",
        "gvt1.com",
        "youtube-nocookie.com",
        "youtube-ui.l.google.com",
        "youtubeembeddedplayer.googleapis.com",
        "youtube.googleapis.com",
        "youtubei.googleapis.com",
        "yt-video-upload.l.google.com",
        "wide-youtube.l.google.com",
    ];
    DNS = "4.4.4.4";
    def MAIN():
        print(fr"""
{colorama.Fore.WHITE} ______   __{colorama.Fore.BLUE}____   _    ____ ____ {colorama.Fore.RED} ____  ____ ___ 
{colorama.Fore.WHITE}|  _ \ \ / /{colorama.Fore.BLUE}  _ \ / \  / ___/ ___|{colorama.Fore.RED}|  _ \|  _ \_ _|
{colorama.Fore.WHITE}| |_) \ V /{colorama.Fore.BLUE}| |_) / _ \ \___ \___ \{colorama.Fore.RED}| | | | |_) | | 
{colorama.Fore.WHITE}|  __/ | | {colorama.Fore.BLUE}|  __/ ___ \ ___) |__) {colorama.Fore.RED}| |_| |  __/| | 
|{colorama.Fore.WHITE}_|    |_| {colorama.Fore.BLUE}|_| /_/   \_\____/____/{colorama.Fore.RED}|____/|_|  |___|
""");
        print(colorama.Fore.WHITE);
        print(f"{"\033[1m"} A simple program which is written on Python to bypass Deep Packet Inspection.\n");
        print(f"{"\033[0m"}{colorama.Fore.WHITE}* IP Address:{colorama.Fore.YELLOW} {PYPASSDPI.IP_ADDRESS}");
        print(f"{"\033[0m"}{colorama.Fore.WHITE}* Port:{colorama.Fore.YELLOW} {PYPASSDPI.PORT}");
        print(f"{"\033[0m"}{colorama.Fore.WHITE}* DNS:{colorama.Fore.YELLOW} {PYPASSDPI.DNS}");
        print(f"{"\033[0m"}{colorama.Fore.WHITE}* Whitelist:{colorama.Fore.YELLOW} {PYPASSDPI.WHITELIST}");
        print(colorama.Fore.WHITE);
        os.system("python3 .venv/lib64/python3.12/site-packages/SERVER.py")
        res.nameservers = [PYPASSDPI.DNS]

        
        print(f"{colorama.Fore.WHITE}* INFO: Changed Port to {colorama.Fore.YELLOW}{PYPASSDPI.PORT}");
        print(f"{colorama.Fore.WHITE}* INFO: Changed IP Address to {colorama.Fore.YELLOW}{PYPASSDPI.IP_ADDRESS}");
        print(f"{colorama.Fore.WHITE}* INFO: Changed DNS to {colorama.Fore.YELLOW}{PYPASSDPI.DNS}");

        for WHITELIST_WEBSITE in PYPASSDPI.WHITELIST:
            CONNECTED_WEBSITE = PYPASSDPI.SOCKET.connect((WHITELIST_WEBSITE, PYPASSDPI.PORT));
            print(CONNECTED_WEBSITE);
        
        while True:
            if input() == "exit":
                exit();
                break;


if __name__ == "__main__":
    PYPASSDPI.MAIN();
