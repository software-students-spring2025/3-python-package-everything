import random

def ask_user_feeling(feeling: str) -> str:
    feelings = {
        "happy": [
            ("(* ^ ω ^)", "You're looking cheerful today! 😊"),
            ("(´ ∀ ` *)", "Happiness suits you!"),
            ("٩(◕‿◕｡)۶", "Keep spreading the joy!"),
            ("☆*:.｡.o(≧▽≦)o.｡.:*☆", "You're glowing with happiness!"),
            ("(o^▽^o)", "Stay positive and keep smiling!"),
        ],
        "sad": [
            ("(ノ_<。)", "It's okay to feel down sometimes."),
            ("(-_-)", "Sending you virtual hugs! 🤗"),
            ("(´-ω-`)", "Hope things get better soon."),
            ("(ﾉД`)", "Take your time and heal."),
            ("(｡╯︵╰｡)", "You're not alone, I'm here for you. 💜"),
        ],
        "mad": [
            ("(＃`Д´)", "Take a deep breath! 🧘"),
            ("(`皿´＃)", "It's okay to feel angry, just don't let it control you."),
            ("( ` ω ´ )", "Let's find a way to cool down."),
            ("ψ( ` ∇ ´ )ψ", "Channel your energy into something productive!"),
            ("ヾ(`ヘ´)ﾉﾞ", "Let’s vent it out and move on."),
        ],
        "soso": [
            ("ヽ(ー_ー )ノ", "Feeling neutral today, huh?"),
            ("ヽ(´ー` )┌", "Sometimes, 'meh' days happen."),
            ("¯\\_(ツ)_/¯", "A chill day is good too!"),
            ("┐(￣～￣)┌", "Not great, not bad—just existing!"),
            ("╮(￣～￣)╭", "Hope your day picks up!"),
        ],
        "excited": [
            ("(ﾉ´ヮ`)ﾉ*: ･ﾟ", "You're radiating energy! 🔥"),
            ("o(≧▽≦)o", "So much excitement!"),
            ("(★ω★)", "You're hyped up!"),
            ("╰(°▽°)╯", "Your energy is contagious!"),
            ("ヽ(o＾▽＾o)ノ", "You must be looking forward to something!"),
        ],
        "tired": [
            ("(×_×)", "You need some rest. 😴"),
            ("(－_－) zzZ", "Sleep is calling!"),
            ("(￣o￣) zzZZzzZZ", "Maybe take a quick nap?"),
            ("(＿ ＿*) Z z z", "Your body needs a break!"),
            ("(︶︹︺)", "Hang in there, you got this."),
        ],
        "nervous": [
            ("(・・;)", "Breathe, you got this!"),
            ("(￣ω￣;)", "Feeling a little anxious?"),
            ("(＠_＠)", "It’s okay to be nervous."),
            ("(•ิ_•ิ)?", "Take it step by step."),
            ("(・・;)ゞ", "You're stronger than your nerves!"),
        ],
        "love": [
            ("(♡-_-♡)", "Love is in the air!"),
            ("(ﾉ´ з `)ノ", "Sending virtual hugs!"),
            ("Σ>―(〃°ω°〃)♡→", "You're glowing with affection!"),
            ("( ˘⌣˘)♡(˘⌣˘ )", "Someone's feeling the love!"),
            ("♡＼(￣▽￣)／♡", "A heart full of love!"),
        ],
        "surprised": [
            ("w(°ｏ°)w", "Whoa! Didn't expect that, huh?"),
            ("(⊙_⊙)", "Something unexpected happened?"),
            ("(°ロ°) !", "What a shock!"),
            ("∑(O_O;)", "Caught off guard?"),
            ("ヽ(°〇°)ﾉ", "That was unexpected!"),
        ],
        "confused": [
            ("(￣ω￣;)", "A little lost?"),
            ("┐('～`;)┌", "Not sure what's happening?"),
            ("(＠_＠)", "Trying to figure things out?"),
            ("σ(￣、￣〃)", "Hmm, something doesn't add up."),
            ("(￣_￣)・・・", "Processing information..."),
        ],
        "scared": [
            ("(ノωヽ)", "It's okay, you're safe!"),
            ("(″ロ゛)", "Something spooky happened?"),
            ("(((＞＜)))", "Deep breaths, you got this."),
            ("＼(º □ º l|l)/", "Stay strong!"),
            ("＼(〇_ｏ)／", "That was unexpected!"),
        ],
        "bored": [
            ("(¬_¬)", "Need something fun to do?"),
            ("(￣～￣)", "Not feeling entertained?"),
            ("(¬‿¬)", "Let's find something exciting!"),
            ("(￣︶￣)", "Maybe try something new?"),
            ("╮(︶▽︶)╭", "Time for a change of pace?"),
        ]
    }

    feeling_lower = feeling.lower()
    if feeling_lower in feelings:
        emoji, message = random.choice(feelings[feeling_lower])
        return f"{emoji} {message}"
    
    return "error: feeling cannot be found"
