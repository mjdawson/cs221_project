import json
import collections
import codecs
import pickle
from pprint import pprint

tracks = track_map = {'The Black Eyed Peas': 'I Got A Feelin', 'Capital Cities': 'Safe and Sound', \
        'Zara Larsson & Mnek': 'Never Forget You', 'Jeremih ft. 50 Cent': 'Down On Me', 'Future Feat. The Weeknd': 'Low Life',\
        'Nicki Minaj': 'Super Bass', 'Beyonce': 'Drunk In Love', 'American Authors': 'Best Day of My Life',\
        'Rihanna': 'Rude Boy', 'Flo Rida': 'Whistle', 'Macklemore & Ryan Lewis ft. Wanz': 'Thrift Shop',\
        'The Weeknd': "Can't Feel My Face", 'Ke$ha': 'Tik Tok', 'Desiigner': 'Panda', 'G-Eazy X Bebe Rexha': 'Me, Myself & I',\
        'Silento': 'Watch Me', 'Daft Punk ft. Pharrell Williams': 'Get Lucky', 'DJ Snake & Lil Jon': 'Turn Down For What',\
        'Dnce': 'Cake By The Ocean', 'Eminem': 'Not Afraid', 'Fat Joe & Remy Ma Feat. French Montana': 'All The Way Up', \
        'Kent Jones': "Don't Mind", 'Idina Menzel': 'Let It Go', 'Ariana Grande ft. Mac Miller': 'The Way', \
        'Lady Gaga Feat Beyonce': 'Telephone', 'Katy Perry Featuring Snoop Dogg': 'California Gurls', \
        'Fall Out Boy': 'My Songs Know What You Did In The Dark', 'Kelly Clarkson': 'Stronger', 'Anna Kendrick': 'Cups', \
        'Pitbull ft. T-Pain': 'Hey Baby (Drop It to the Floor)', 'Chris Brown': 'Loyal', 'Mike Posner': 'Cooler Than Me',\
        'James Bay': 'Let It Go', 'Hot Chelle Rae': 'Tonight Tonight', 'Ariana Grande': 'Break Free', 'Rihanna ft. Drake': 'Whats My Name',\
        'P!Nk': 'Just Like Fire', 'Nelly': 'Just A Dream', 'Lukas Graham': '7 Years', 'Snoop Dogg & Wiz Khalifa': 'Young, Wild & Free',\
        'Passenger': 'Let Her Go', 'Avicii': 'Wake Me Up', 'Robin Thicke': 'Blurred Lines', 'Rihanna ft. Mikky Ekko': 'Stay',\
        'Lady GaGa': 'The Edge of Glory', 'Andy Grammer': "Honey, I'm Good", 'Lorde': 'Royals', 'Ke$sha': 'Your Love Is My Drug',\
        'Bad Meets Evil ft. Bruno Mars': 'Lighters', 'Lil Wayne': 'How to Love', 'David Guetta': 'Turn Me On', \
        'The Chainsmokers Feat. Daya': "Don't Let Me Down", 'Jay-Z ft. Justin Timberlake': 'Holy Grail', 'Omarion': 'Post To Be',\
        'Taio Cruz': 'Dynamite', 'Florida Georgia Line ft. Nelly': 'Cruise', 'Gym Class Heroes ft. Adam Levine': 'Stereo Hearts',\
        'Lyaz': 'Replay', 'Zedd ft. Foxes': 'Clarity', 'Rachel Platten': 'Fight Song', 'Usher Feat will.i.am': 'OMG',\
        'Fifth Harmony Feat. Ty Dolla $Ign': 'Work From Home', 'Omi': 'Cheerleader', 'The Wanted': 'Glad You Came', \
        'Nick Jonas Feat. Tove Lo': 'Close', 'Jennifer Lopez ft. Pitbull': 'On the Floor', 'Ruth B': 'Lost Boy', \
        'Swedish House Mafia Feat John Martin': "Don't You Worry Child", 'Bastille': 'Pompeii', 'Ellie Goulding': 'Lights', \
        'Jason Mraz': 'I Won\'t Give Up', 'Meghan Trainor': 'All About That Bass', 'P!nk ft. Nate Ruess': 'Just Give Me A Reason',\
        'Ed Sheeran': 'Photograph', 'Eminem Featuring Rihanna': 'Love The Way You Lie', 'Pitbull': 'Timber', 'Fifth Harmony': 'Worth It',\
        'Neon Trees': 'Everybody Talks', 'Lupe Fiasco': 'The Show Goes On', 'Enrique Iglesias': 'Bailando',\
        'Pitbull ft. Ne-Yo, Afrojack & Nayer': 'Give Me Everything', 'Jason Derulo': 'In My Head', 'Walk The Moon': 'Shut Up And Dance',\
        'Wiz Khalifa': 'Black and Yellow', 'The Script': 'Breakeven', 'Sam Smith': 'Stay With Me', 'Diddy': 'Dirty Money ft. Skylar Grey - Coming Home',\
        'Maroon 5': 'Moves Like Jagger', 'Fun.': 'Some Nights', 'One Republic': 'Good Life', 'Gotye': 'Somebody That I Used to Know',\
        'Chris Brown ft. Lil Wayne & Busta Rhymes': 'Look At Me Now', 'Twenty One Pilots': 'Ride', 'Mark Ronson': 'Uptown Funk',\
        'Carly Rae Jepsen & Owl City': 'Good Time', 'Justin Timberlake': 'Mirrors', 'Timbaland Featuring Justin Timberlake': 'Carry Out',\
        'Hozier': 'Take Me To Church', 'MAGIC!': 'Rude', 'LMFAO': 'Party Rock Anthem', 'Alex Clare': 'Too Close', 'Train': 'Hey Soul Sister',\
        'Major Lazer': 'Lean On', 'Far*East Movement Featuring Cataracs & Dev': 'Like A G6', 'Tove Lo': 'Habits',\
        'Will.I.Am ft. Britney Spears': 'Scream & Shout', 'Fetty Wap': '679', 'Drake Feat. The Throne': 'Pop Style',\
        'Jessie J, Ariana Grande & Nicki Minaj': 'Bang Bang', 'O.T. Genasis Feat. Young Dolph': 'Cut It', 'Iggy Azalea': 'Black Widow ft. Rita Ora',\
        'Florida Georgia Line': 'H.O.L.Y.', 'Pharrell Williams': 'Happy', 'Disclosure': 'Latch', 'Kanye West': 'Mercy',\
        'Foster the People': 'Pumped Up Kicks', 'A Great Big World': 'Say Something', 'Ludacris': 'How Low',\
        'Jay-Z + Alicia Keys': 'Empire State Of Mind', 'Enrique Iglesias Featuring Pitbull': 'I Like It', 'AWOLNATION': 'Sail',\
        'B.o.B Featuring Bruno Mars': 'Nothin On You', 'Nick Jonas': 'Jealous', 'Icona Pop ft. Charli XCX': 'I Love It',\
        'Travie McCoy Featuring Bruno Mars': 'Billionaire', 'Britney Spears': 'Till the World Ends', 'Sia': 'Chandelier',\
        'Cee Lo Green': 'Fuck You', 'Usher Featuring Pitbull': 'DJ Got Us Fallin In Love', 'Young Money Featuring Lloyd': 'Bedrock',\
        'Jay-Z & Kanye West': 'Ni**as In Paris', 'Justin Timberlake feat. Jay Z': 'Suit & Tie', 'Bruno Mars': 'Just The Way You Are',\
        'Charli XCX': 'Boom Clap', 'Drake Feat. Rihanna': 'Too Good', 'Blake Shelton': 'Came Here To Forget', 'Calvin Harris': 'Summer',\
        'Justin Bieber': 'As Long As You Love Me', 'Miley Cyrus': 'Wrecking Ball', 'Zayn': 'Pillowtalk', 'P!nk': 'Fuckin Perfect',\
        'John Legend': 'All of Me', 'Owl City': 'Fire Flies', 'Kevin Gates': '2 Phones', 'B.o.B Featuring Hayley Williams': 'Airplanes',\
        'R. City': 'Locked Away', 'Baauer': 'Harlem Shake', 'Lady Gaga': 'Alejandro', 'Drake': 'Find Your Love',\
        'Macklemore & Ryan Lewis ft. Ray Dalton': "Can't Hold Us", 'Jeremih': 'Oui', 'David Guetta Featuring Akon': 'Sexy Chick',\
        'Pitbull ft. Christina Aguilera': 'Feel This Moment', 'Rihanna Feat. Drake': 'Work', 'The Lumineers': 'Ho Hey',\
        'Maroon 5 ft. Christina Aguilera': 'Moves Like Jagger', 'Taio Cruz Featuring Ludacris': 'Break Your Heart', \
        'Michael Buble': "Haven't Met You Yet", 'One Direction': 'What Makes You Beautiful', 'Lil Wayne ft. Drake & Future': 'Love me',\
        'Shawn Mendes': 'Stitches', 'Selena Gomez': 'Come & Get It', 'Carly Rae Jepsen': 'Call Me Maybe'}

#        Valence: how positive or negative sounding something is
#        Loudness
#        Danceability:
#        Energy:
#        Acousticness:
#        Speechiness:

def constructNamesToTuple():
    trackToFeatureTuples = collections.defaultdict()
    for key in tracks:
		# just open the file...
		input_file  = file('audioFeatures/' + tracks[key] + ".json", "r")
		# need to use codecs for output to avoid error in json.dump

		# read the file and decode possible UTF-8 signature at the beginning
		# which can be the case in some files.
		j = json.loads(input_file.read().decode("utf-8-sig"))
                #key, time signature, tempo, valence, loudness, danceability, energy, acousticness, speechiness
                trackToFeatureTuples[tracks[key]] = (j["key"], j["time_signature"],
                    j["tempo"], j["valence"], j["loudness"], j["danceability"], \
                    j["energy"], j["acousticness"], j["speechiness"])

    
    pickle.dump(trackToFeatureTuples, open("trackToFeatureTuples.p", "wb"))

def constructNamesToDict():
		tracksToFeatures = collections.defaultdict(lambda: collections.defaultdict(lambda: 0))
		for title in tracks:
				input_file = file('audioAnalysis/' + tracks[title] + '.json', 'r')

				j = json.loads(input_file.read().decode("utf-8-sig"))
				tracksToFeatures[tracks[title]] = j
#        for key in j:
#            print j[key]
#            tracksToFeatures[tracks[title]][key] = j[key]
#            break
#		pickle.dump(tracksToFeatures, open("trackToFeatures.p", "wb"))
		return tracksToFeatures

