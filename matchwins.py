#!/usr/bin/python3

fileread = "/home/deso/armagetronad/servers/sumobar/var/won_matches.txt";

color_border = "0x4444cc";
color_header = "0xaa4444";
color_text = "0xffffff";
border_text = "=";
border_length = 54;

import re;
from math import floor,ceil;

def msg(msg):
	print("CONSOLE_MESSAGE",msg);

while True:
	event = input();
	split = event.split(" ");
	if split[0] == "NEW_MATCH":
		with open(fileread) as f:
			board = color_border+"|"+(border_text*(border_length-2))+"|"+'\\n';
			#board += color_border+"|"+(" "*(border_length-2))+"|"+'\\n';
			board += color_border+"|"+color_header+"              HIGHSCORES / MATCHES WON              "+color_border+"|"+'\\n';
			#board += color_border+"|"+(" "*(border_length-2))+"|"+'\\n';
			board += color_border+"|"+(border_text*(border_length-2))+"|"+'\\n';
			board += color_border+"|   "+color_header+"RANK   "+color_border+"|             "+color_header+"PLAYER            "+color_border+"|"+color_header+"   WINS  "+color_border+"|"+'\\n';
			board += color_border+"|"+(border_text*(border_length-2))+"|"+'\\n'; 
			#board += color_border+"|          |                               |         |"+'\\n';
			for i in range(10):
				line = f.readline();
				exp = re.split('\s+',line.strip());
				if len(exp) < 2:
					break;
				wins = exp[0];
				player = exp[1];
				
				rank = i+1;
				space_rank = 5 - len(str(rank));
				space_wins = 5 - len(wins);
				space_player = (29 - len(player))/2;

				board += color_border+"|    "+color_text+str(rank)+(" "*space_rank)+" "+color_border+"|"+color_text+" "+(" "*floor(space_player))+(player.replace("\\","\\\\"))+(" "*ceil(space_player))+" "+color_border+"|"+(" "*space_wins)+" "+color_text+wins+"   "+color_border+"|"+'\\n';

			#board += color_border+"|"+(" "*(border_length-2))+"|"+'\\n';
			board += color_border+"|"+(border_text*(border_length-2))+"|"+'\\n';

			msg(board);

