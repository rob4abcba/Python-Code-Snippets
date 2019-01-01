message = '''There are many questions homeowners ask themselves during the selling process. 
"How much will my home sell for?"  "How much should I list my home for?"  
"Who should I select as a real estate agent to sell my home?"  "What if the real 
estate agent overprices my home?"  Last but not least, "Is this a good time to be 
selling a home?" is also a very common question that real estate agents are asked.'''

print(message)
print(len(message))
print(message.count("real estate"))
print(message.find("real estate"))
new_message = message.replace("real estate", "fake estate")
print(new_message)

print(message[3:9])
print(len(message[3:9]))

print(message[0:9])
print(len(message[0:9]))
print(message[0:9].lower())

message = message.replace("the", "da")
print(message)

greeting = 'Hello'
name = 'Michael'
message = "{} .... {}!!  You da man!".format(greeting, name)
print(message)
message = f"Really {greeting} .... {name}!!  You da man!"
print(message)
message = f"{greeting.upper()} .... {name.upper()}!!  You da man!"
print(message)

print(dir(message))
#print(help(str))
print(help(str.lower))

message = '''詞: 宋建彰
Ci: Song Jian Zhang
Lyrics: Song Jian Zhang

曲: 周杰倫
Qu: Zhou Jie Lun
Lyrics: Jay Chou

久未放晴的天空 依舊留著你的笑容
jiu wei fang qing de tian kong / yi jiu liu zhe ni de xiao rong
The sky which has long not been sunny still keeps your smile as before

哭過 卻無法掩埋歉疚
ku guo / que wu fa yan mai qian jiu
Have cried, but been unable to bury [my] guilt

風箏在陰天擱淺 想念還在等待救援
Feng zheng zai yin tian ge qian / xiang nian hai zai deng dai jiu yuan
The kite stranded in the gloomy sky, [my] longing is still awaiting to be rescued

我拉著線 複習你給的溫柔
wo la zhe xian / fu xi ni gei de wen rou
I'm pulling the kite string and reviewing the tenderness you gave


曝晒在一旁的寂寞
pu shai zai yi pang de ji mo 
The loneliness that has been isolated on the side

笑我給不起承諾
xiao wo gei bu qi cheng nuo
Laughing at the promises that I can't afford to give

怎麼會怎麼會 你竟原諒了我
zen me hui zen me hui ni jing yuan liang le wo
How come, how come, you've actually forgiven me


我只能永遠讀著對白 讀著我給你的傷害
wo zhi neng yong yuan du zhe dui bai / du zhe wo gei ni de shang hai
I can only forever read the dialogue, reading the pain that I've given you

我原諒不了我 就請你當作我已不在
wo yuan liang bu liao wo / jiu qing ni dang zuo wo yi bu zai
I cannot forgive myself, so please treat as if I'm not here anymore

我睜開雙眼看著空白 忘記你對我的期待
wo zheng kai shuang yan kan zhe kong bai / wang ji ni dui wo de qi dai
I looked on blankly with eyes wide open, [trying] to forget the expectations you had of me

讀完了依賴 我很快就離開
du wan le yi lai / wo hen kuai jiu li kai
After finish reading [my] dependence [on you], I'll leave very soon '''

print(message)
print(len(message))
print(message.count("我"))
print(message.find("我"))
new_message = message.replace("我", "Wo")
print(new_message)

print(message[3:9])
print(len(message[3:9]))

print(message[0:9])
print(len(message[0:9]))
print(message[0:9].lower())

message = message.replace("我", "Wo baby baby")
print(message)

greeting = '你好'
name = '哥哥'
message = "{} .... {}!!  You da man!".format(greeting, name)
print(message)
message = f"Really {greeting} .... {name}!!  You da man!"
print(message)
message = f"{greeting.upper()} .... {name.upper()}!!  You da man!"
print(message)