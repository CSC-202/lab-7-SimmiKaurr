# huffman-analysis.py
## author - nick s.
### get huffman.py working first, then work on this file

import matplotlib.pyplot as plt

# DATA - lyrics
POKEMON_LYRICS = 'I wanna be the very best. Like no one ever was. To catch them is my real test. To train them is my cause. I will travel across the land. Searching far and wide. Each Pokemon to understand. The power that\'s inside. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny. (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon. (gotta catch \'em all.) Gotta catch \'em all. Yeah. Every challenge along the way. With courage I will face. I will battle every day. To claim my rightful place. Come with me, the time is right. There\'s no better team. Arm in arm we\'ll win the fight. It\'s always been our dream. (Pokemon, gotta catch \'em all.) Its you and me. I know it\'s my destiny (Pokemon.) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you. Pokemon (gotta catch \'em all.) Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Gotta catch \'em all. Yeah! (Pokemon, gotta catch \'em all). Its you and me. I know it\'s my destiny. (Pokemon) Oh, you\'re my best friend. In a world we must defend. (Pokemon, gotta catch \'em all.) A heart so true. Our courage will pull us through. You teach me and I\'ll teach you Pokemon. (gotta catch \'em all). Gotta catch \'em all. (Pokemon)'
JIGGLE_JIGGLE = 'You have to have something that sticks. You have to have something that\'s monumental. When you walk out on stage, that\'s been monumental. (Jiggle, jiggle) Can you remember any of the rap that you did? My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. I sip booze from chalices, holding my palaces. Crib is so crampy suckers suffer from paralysis. Rhymes, I write them in the castle. You try to diss me and pretty soon your ass. Will squat in a cell \'cause I can tell you it\'s illegal. Treason, that\'s the reason I\'m regal. You do the time for the crime of lèse-majesté. And **** the police \'cause they can\'t arrest me. (They can\'t arrest me, they can\'t arrest me). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). My money don\'t jiggle, jiggle, it folds. I like to see you wiggle, wiggle, for sure. It makes me want to dribble, dribble, you know. Riding in my Fiat, you really have to see it. Six feet two in a compact, no slack. But luckily the seats go back. I got a knack to relax in my mind. Sipping some red, red wine. (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?). (I like to see you wiggle, it makes me dribble, fancy a fiddle?)'
ALPHABET = 'Now it\'s time for our wrap up. Let\'s give it everything we\'ve got. Ready, begin. Artificial amateurs aren\'t at all amazing. Analytically, I assault, animate things. Broken barriers bounded by the bomb beat. Buildings are broken, basically I\'m bombarding. Casually create catastrophes, casualties. Canceling cats got their canopies collapsing. Detonate a dime of dank daily doin\' dough. Demonstrations, Don Dada on the down low. Eatin\' other editors with each and every energetic. Epileptic episode, elevated etiquette. Furious fat fabulous fantastic. Flurries of funk felt feeding the fanatics. Imitators idolize, I intimidate. In a instant, I\'ll rise in a irate state. Juiced on my jams like jheri curls, jockin\' joints. Justly, it\'s just me, writin\' my journals. Kindly I\'m kindling all kinds of ink on. Karate kick type Brits in my kingdom. Let me live a long life, lyrically lessons is. Learned lame louses just lose to my livery. My mind makes marvelous moves, masses. Marvel and move, many mock what I\'ve mastered.  Niggas nap knowin\' I\'m nice naturally. Knack, never lack, make noise nationally.  Operation, opposition, off, not optional. Out of sight, out of mind, wide beaming opticals. Perfected poem, powerful punchlines. Pummeling petty powder puffs in my prime. Quite quaint quotes keep quiet it\'s Quannum Quarrelers ain\'t got a quarter of what we got, uh. Really raw raps, risin\' up rapidly. Riding the rushing radioactivity. Super scientifical sound search sought. Silencing super fire saps that are soft. Tales ten times talented, they\'re too tough. Take that, challengers, get a tune up. Universal, unique untouched. Unadulterated, the raw uncut. Verb vice Lord victorious valid. Violate vibes that are vain make \'em vanished. Why I\'m all well, would a wise wordsmith. Just weaving up words weeded up, on my work shift. Xerox, my X-ray-diation holes extra large. X-height letters and xylophone tones.'

WINX_CLUB = 'Do you know the power you have? Can you feel the magic that is inside of you? Fly with us and you\'ll understand. You are magic if you just believe that it\'s true. It\'s amazing what you can do. Winx! Your magic now. Winx! We\'ll show you how. Fly with us and see. The amazing things you can be. Winx! Together, we\'re strong. Come and join our song. We are fast, and we are fierce. We are heroes, strong, and good, confident too. Anywhere you need us, we\'re there. And the world is better \'cause of what we do. It\'s amazing what you can do. Winx! Go get your wings. Winx! Come do it please. All that we can do. There\'s no magic without you. Join us now when we fly. Cause we own the sky. Winx! You\'re magic now. Winx! We\'ll show you how. We\'re gonna fly together. We\'re gonna soar forever. Winx! You\'re magic now. Winx! We\'ll show you how. Fly with us and see. The amazing things you can be. Join us now when we fly. Cause we own the sky. Your life is magic from now on. Yes, your life is magic from now...Winx!'
YOU_BELONG_WITH_ME = 'You\'re on the phone with your girlfriend, she\'s upset. She\'s going off about something that you said. \'Cause she doesn\'t get your humor like I do. I\'m in the room, it\'s a typical Tuesday night. I\'m listening to the kind of music she doesn\'t like. And she\'ll never know your story like I do. But she wears short skirts. I wear T-shirts. She\'s Cheer Captain, and I\'m on the bleachers. Dreaming about the day when you wake up and find. That what you\'re looking for has been here the whole time. If you could see that I\'m the one. Who understands you. Been here all along. So, why can\'t you see? You belong with me. You belong with me. Walk in the streets with you in your worn-out jeans. I can\'t help thinking this is how it ought to be. Laughing on a park bench thinking to myself. Hey, isn\'t this easy? And you\'ve got a smile. That can light up this whole townI haven\'t seen it in a while. Since she brought you down. You say you\'re fine, I know you better than that. Hey, what you doing with a girl like that?. She wears high heels. I wear sneakers. She\'s Cheer Captain, and I\'m on the bleachers. Dreaming about the day when you wake up and find. That what you\'re looking for has been here the whole time. If you could see that I\'m the one. Who understands you. Been here all alongSo, why can\'t you see?. You belong with me. Standing by and waiting at your backdoor. All this time how could you not know, baby? You belong with me. You belong with me. Oh, I remember you driving to my house. In the middle of the night. I\'m the one who makes you laugh. When you know you\'re \'bout to cry. And I know your favorite songs. And you tell me \'bout your dreams. Think I know where you belong. Think I know it\'s with me. Can\'t you see that I\'m the one. Who understands you? Been here all along. So, why can\'t you see?. You belong with me. Standing by and waiting at your backdoor. All this time how could you not know, baby?. You belong with me. You belong with me. You belong with me. Have you ever thought just maybe. You belong with me?. You belong with me'
ONE_DANCE = 'Baby, I like your style. Grips on your waist. Front way, back way. You know that I don\'t play. Streets not safe. But I never run away. Even when I\'m away. OT, OT, there\'s never much love when we go OT. I pray to make it back in one piece. I pray, I pray. That\'s why I need a one dance. Got a Hennessy in my hand. One more time \'fore I go. Higher powers taking a hold on me. I need a one dance. Got a Hennessy in my hand. One more time \'fore I go. Higher powers taking a hold on me. Baby, I like your style. Strength and guidance. All that I\'m wishin\' for my friends. Nobody makes it from my ends. I had to bust up the silence. You know you gotta stick by me. Soon as you see the text, reply me. I don\'t wanna spend time fighting. We\'ve got no time. And that\'s why I need a one dance. Got a Hennessy in my hand. One more time \'fore I go. Higher powers taking a hold on me. I need a one dance. Got a Hennessy in my hand. One more time \'fore I go. Higher powers taking a hold on me. Got a pretty girl and she love me long time. Wine it, wine it, and she love me long time. Ooh yeah, just steady and wine up. Back up, back up, back up and wine up. Back up, back up and wine it. Girl, just back up, back up, back up and wine down. Ooh yeah, just steady and wine up. Back, up, back up and wine it, girl. Ooh, tell me. I need to know, where do you wanna go?. \'Cause if you\'re down, I\'ll take it slow. Make you lose control. Where, where, where. Where, where, where, where (ooh yeah, very long time). (Back, up, back up and wine it, girl). \'Cause if you\'re down (back up, back up and). \'Cause if you\'re down (back up, back up and). \'Cause if you\'re down (back up, back up and). I need a one dance. Got a Hennessy in my hand. One more time \'fore I go. Higher powers taking a hold on me. I need a one dance. Got a Hennessy in my hand. One more time \'fore I go. Higher powers taking a hold on me'

# DATA - mantras
GREEN_LATTERN = 'In brightest day, in blackest night, No evil shall escape my sight. Let those who worship evil\'s might, Beware my power... Green Lantern\'s light!'
JEDI_CODE = 'Emotion, yet peace. Ignorance, yet knowledge. Passion, yet serenity. Chaos, yet harmony. Death, yet the Force.'
SITH_CODE = 'Peace is a lie. There is only Passion. Through Passion, I gain Strength. Through Strength, I gain Power. Through Power, I gain Victory. Through Victory my chains are Broken. The Force shall free me.'

SELF_LOVE = 'I choose to stop apologizing for being me. I deserve all that is good. I radiate confidence, self-respect and inner harmony. My voice is valuable and my opinion matters. I love my boud and all it does for me. I choose to be grateful for all that I have. I consciously release the past and live only in the present. I attract wonderful people into my life. I am creating a beautiful life. I am worthy of love and attention.'
ABUNDANCE = 'I trust and value my intuition. I manifest abundance by being grateful for everything I have. I am open to receiving abundace and propserity. All of my needs are met by the Universe\'s abundant supply. The things I want naturally find their way to me. I am a magnet for abundance. I have everything that I need'
MANIFESTING = 'Opportunities will consistently come my way! I attract happiness & love. I accept myself for who I am and what I stand for. All I need is within me! I am in the right place at the right time.'

# the input, what we want to encode
def huffman(message:str) -> float:
    message = message.upper()

    # the output, should be all 0's and 1s
    result: str = str()

    # for counting the letter frequencies
    freq: dict = dict() # key  -> a letter
                        # item -> num of occurences

    # for holding the nodes of the huffman tree
    nodes: list = list() 

    # for storing the code for each letter
    coding: dict = dict()   # key  -> a letter
                            # item -> a binary encoding


    # STEP 0
    ## defining our data structures
    ## defining operations
    class Node: # NOT given to students
        weight : int
        letters : str
        left: any
        right: any
    
        def __init__(self, letters = None, weight = None, left = None, right = None):
            self.weight = weight
            self.letters = letters
            self.left = left
            self.right = right
            
### recursively traverses the huffman tree to record the codes
    def retrieve_codes(v: Node, path: str=''):
        if v.letters != None: # if 'TODO': # TODO
            coding[v.letters] = path # TODO
        else:
            retrieve_codes(v.left, path + '0') # TODO
            retrieve_codes(v.right, path + '1') # TODO

    

    # STEP 1
    ## counting the frequencies
    for i in message:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    # STEP 2
    ## initialize the nodes
    for letters, count in freq.items():
        nodes.append(Node(letters, count))

    # STEP 3
    ## combine each nodes until there's only one item in the nodes list
    while len(nodes) > 1:
    ## sort based on weight
        nodes.sort(key=lambda x: x.weight, reverse=True)

    ## get the first min
        min_a: Node = nodes.pop()

    ## get the second min
        min_b: Node = nodes.pop()

    ## combine the two
        combined = Node(None, min_a.weight + min_b.weight, min_a, min_b) # TODO

    ## put the combined nodes back in the list of nodes
        nodes.append(combined)


    # STEP 4
    ## reconstruct the codes
    huff_root = nodes[0]
    retrieve_codes(huff_root)
    for i in message:
        result += str(coding[i]) # TODO (hint coding[letter] -> code)

    # STEP 5
    ## analyize compression performance
    n_original_bits: int = len(message) * 8
    n_encoded_bits: int = len(result)
    compression_ratio: float = 1 - (n_encoded_bits / n_original_bits)

    return result, coding, compression_ratio

# LYRICS

plt.suptitle('Lab 7 - Kaur Analyzing Huffman')
plt.ylabel("compression %")
plt.subplot(2, 1, 1)

MAX_N: int = int(128 * 3 / 2)

# PLOT 1
## WINX CLUB
data: str = WINX_CLUB
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'Winx_Club (n={len(coding)})', color ='red', linestyle='dashdot')


## YOU BELONG WITH ME
data: str = YOU_BELONG_WITH_ME
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'You_Belong_With_Me (n={len(coding)})', color ='green', linestyle='dashdot')

## ONE DANCE
data: str = ONE_DANCE
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'One_Dance(n={len(coding)})', color ='blue', linestyle='dashdot')
plt.legend()


# PLOT 2
plt.subplot(2, 1, 2)
plt.ylabel("compression %")

## SELF LOVE
data: str = SELF_LOVE
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'Self_Love (n={len(coding)})', color ='red', linestyle='dashdot')

## ABUNDANCE
data: str = ABUNDANCE
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'Abundance (n={len(coding)})', color ='green', linestyle='dashdot')

## MANIFESTING
data: str = MANIFESTING
ratios: list = list()
for i in range(1, len(data)):
    x = data[0: i]
    compressed, coding, ratio = huffman(x)
    ratios.append(ratio)
min_ratio = min(ratios)
min_idx = ratios.index(min_ratio)

plt.plot(ratios[:MAX_N], label=f'Manifesting (n={len(coding)})', color ='blue', linestyle='dashdot')

plt.xlabel("length of message")
plt.legend()
plt.show()
