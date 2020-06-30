# BOT made by IRONKAGE. You can used, but don't delete this string. Enjoy!
import requests
import random
import datetime

from bot_config import TOKEN as bot_token
from bot_config import *

dayOfWeekUA = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
todayWeekDay = datetime.datetime.today().weekday()
tranformWeekDayFromNumberToString = dayOfWeekUA[todayWeekDay]
currentTimeOfDay = datetime.datetime.now().strftime("%H:%M")

def telegram_bot_send_text(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

VerbsForWeekDay = ["Today is", "WoW", "Finally it's", "Now arrived"]
VerbsForCall = ["Are You ready?", "How do you feel?", "How are things?", "How's life treating you?", "What's going on?", "What's happening?", "What's new with you?", "What's poppin?", "What's shaking?", "What's sizzlin?", "What are you doing?", "What are you up to?", "What's up buttercup?", "Anything new with you?", "Whatcha doing?", "What's new?", "What's cookin'?", "How is it going?", "Well, hello there?", "Yo!", "Wazzap?", "Wagvan?", "Hello!" , "Hi!", "Hey there!", "How are you?", "Howdy?", "Sup?"]
VerbsForCitata = ['"Success consists of going from failure to failure without loss of enthusiasm. (Winston Churchill)"', '"You miss 100%/ of the shots you do not take. (Wayne Gretzky)"', '"There are no shortcuts to any place worth going. (Helen Keller)"', '"There are people who have money and people who are rich. (Coco Chanel)"', '"You only live once, but if you do it right, once is enough. (May West)"', '"Happiness lies in good health and a bad memory. (Ingrid Bergman)"', '"Your time is limited, so do not waste it living someone else’s life. (Steve Jobs)"', '"Life is 10% what happens to me and 90%/ of how I react to it. (Charles Swindoll)"', '"The limits of my language are the limits of my world. (Ludwig Wittgenstein)"', '"Learning is a treasure that will follow its owner everywhere. (Chinese Proverb)"', '"You can never understand one language until you understand at least two. (Geoffrey Willans)"', '"Knowledge is power. (Sir Francis Bacon)"', '"The pain of studying is only temporary. But the pain of not knowing – ignorance – is forever."', '"Studying is not about time. It’s about effort."', '"Life is not all about studying. But if you can not even conquer this little part of life, then what else can you possibly do?"', '"Not everyone can truly succeed in everything. But success only comes with self-management and determination."', '"If you do not walk today, you’ll have to run tomorrow."', '"When today is over, it will never come back."', '"No pain, no gain."', '"Accept responsibility for your life. Know that it is you who will get you where you want to go, no one else. (Les Brown)"', '"Nobody ever wrote down a plan to be broke, fat, lazy, or stupid. Those things are what happen when you do not have a plan. (Larry Winget)"', '"In order to succeed, we must first believe that we can. (Nikos Kazantzakis)"', '"Build your own dreams, or someone else will hire you to build theirs», - Farrah Gray"', '"Do not wait, the time will never be «just right». Start where you stand, and work with whatever tools you may have at your command, and better tools will be found as you go along. (George Herbert)"', '"If you fall asleep now, you will dream. If you study now, you will live your dream."', '"Challenges are what make life interesting and overcoming them is what makes life meaningful. (Joshua J. Marine)"', '"Opportunity does not knock, it presents itself when you beat down the door. (Kyle Chandler)"', '"Small deeds done are better than great deeds planned. (Peter Marshall)"', '"An investment in knowledge always pays the best interest. (Benjamin Franklin)"', '"Formal education will make you a living. Self-education will make you a fortune. (Jim Rohn)"', '"Success is not in what you have, but who you are. (Bo Bennett)"', '"To have another language is to possess a second soul."', '"Man invented language to satisfy his deep need to complain. (Lily Tomlin)"', '"Money speaks sense in a language all nations understand. (Aphra Behn)"', '"It does not matter how slowly you go so long as you do not stop."', '"Those who can not change their minds can not change anything. (Bernard Shaw)"']

def FormatForSend(users, time, link):
    telegram_bot_send_text("{} {}\n\n{}\n{}\nSee you at {}\n\n*{}*\n\n_Waiting for you:_\n{}".format(
                                                    random.choice(VerbsForWeekDay),
                                                    tranformWeekDayFromNumberToString,
                                                    random.choice(VerbsForCall),
                                                    str(users),
                                                    str(time),
                                                    random.choice(VerbsForCitata),
                                                    str(link),
                                                    parse_mode='MARKDOWN_V2'))

# You need write time for per day (See example)
if todayWeekDay == 0: # Понеділок - Monday
    if currentTimeOfDay == "15:00":
        bot_chatID = ID2_Name_Group
        FormatForSend(Users_Name_Group, '16:00', Link_Name_Group)
    
    elif currentTimeOfDay == "16:00":
        bot_chatID = ID3_Test
        FormatForSend(Users_Test, '17:00', Link_Test)

    else:
        pass


elif todayWeekDay == 1: # Вівторок - Tuesday
    pass


elif todayWeekDay == 2: # Середа - Wednesday
    pass


elif todayWeekDay == 3: # Четвер - Thursday
    if currentTimeOfDay == "08:00":
        bot_chatID = ID1_Name_Team
        FormatForSend(Users_Name_Team, '09:00', Link_Name_Team)

    elif currentTimeOfDay == "18:00":
        bot_chatID = ID2_Name_Group
        FormatForSend(Users_Name_Group, '19:00', Link_Name_Group)

    else:
        pass


elif todayWeekDay == 4: # П'ятниця - Friday
    pass

else:
    pass