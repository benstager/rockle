existing_bands = [
    "AC/DC", "Aerosmith", "Alice Cooper", "Allman Brothers Band", "Bad Company", "Black Sabbath", 
    "Blue Öyster Cult", "Boston", "Cheap Trick", "Creedence Clearwater Revival", "Deep Purple", 
    "Def Leppard", "Derek and the Dominos", "Eagles", "Fleetwood Mac", "Foreigner", "Genesis", 
    "Grateful Dead", "Heart", "Iron Maiden", "Jethro Tull", "Judas Priest", "Kansas", "KISS", 
    "Led Zeppelin", "Lynyrd Skynyrd", "Motörhead", "Nazareth", "Pink Floyd", "Queen", "Rainbow", 
    "REO Speedwagon", "Rush", "Santana", "Scorpions", "Steely Dan", "Styx", "Ted Nugent", "The Band", 
    "The Doors", "The Police", "The Rolling Stones", "The Who", "Thin Lizzy", "Tom Petty and the Heartbreakers", 
    "Triumph", "UFO", "Uriah Heep", "Van Halen", "Yes", "ZZ Top", "Bon Jovi", "Bruce Springsteen", 
    "Dire Straits", "Guns N' Roses", "INXS", "Journey", "Metallica", "Nirvana", "Pearl Jam", 
    "Poison", "R.E.M.", "Red Hot Chili Peppers", "Roxy Music", "Soundgarden", "The Cure", "The Smiths", 
    "U2", "Whitesnake", "Winger", "Warrant", "10cc", "Argent", "Asia", "Bachman-Turner Overdrive", 
    "Badfinger", "Big Star", "Blind Faith", "The Byrds", "Camel", "Can", "Caravan", "Cheap Trick", 
    "Chicago", "Colosseum", "Cream", "Crosby, Stills, Nash & Young", "David Bowie", "Devo", "Doobie Brothers", 
    "Electric Light Orchestra", "Emerson, Lake & Palmer", "Fairport Convention", "Focus", "Free", 
    "Gentle Giant", "Hawkwind", "Humble Pie", "King Crimson", "Little Feat", "Love", "Manfred Mann's Earth Band", 
    "MC5", "Mountain", "Mott the Hoople", "New York Dolls", "Nick Cave and the Bad Seeds", "Pavement", 
    "Pixies", "Procol Harum", "Public Image Ltd.", "Renaissance", "Roxy Music", "Slade", "Small Faces", 
    "Spinal Tap", "Steppenwolf", "The Animals", "The Beach Boys", "The Clash", "The Kinks", "The Monkees", 
    "The Move", "The Troggs", "Traffic", "Velvet Underground", "Wings", "XTC", "Yes", "Zombies", "ZZ Top", 
    "Anthrax", "Black Crowes", "Blondie", "Bush", "Counting Crows", "Dinosaur Jr.", "Faith No More", 
    "Fugazi", "Green Day", "Hole", "Jane's Addiction", "Live", "Meat Puppets", "Nine Inch Nails", "Oasis", 
    "Offspring", "Pixies", "Pulp", "Radiohead", "Rage Against the Machine", "Screaming Trees", 
    "Sex Pistols", "Smashing Pumpkins", "Stone Temple Pilots", "Suicidal Tendencies", "T. Rex", 
    "Talking Heads", "The B-52's", "The Breeders", "The Jam", "The Pretenders", "The Replacements", 
    "The Stranglers", "The Verve", "They Might Be Giants", "Tool", "Violent Femmes", "Weezer", "Wilco", 
    "Big Country", "Blue Cheer", "The Cars", "Clash", "Damn Yankees", "Dream Theater", "Extreme", 
    "Fastway", "Goo Goo Dolls", "Hanoi Rocks", "Helmet", "Hootie & the Blowfish", "Hüsker Dü", 
    "Iron Butterfly", "L.A. Guns", "Living Colour", "Love and Rockets", "Marillion", "Meat Loaf", 
    "Midnight Oil", "Ministry", "Mr. Big", "Night Ranger", "The Outlaws", "Pat Benatar", "Peter Frampton", 
    "Primus", "Queensrÿche", "Saga", "Savatage", "Sepultura", "Silverchair", "Skid Row", "Slayer", 
    "Sonic Youth", "Spandau Ballet", "Status Quo", "Stryper", "Sugar", "Tesla", "The Cult", 
    "The Fabulous Thunderbirds", "The Guess Who", "The Lemonheads", "The Meat Puppets", "The Moody Blues", 
    "The Outfield", "The Pogues", "The Scorpions", "The Stone Roses", "The Traveling Wilburys", 
    "The Tubes", "The Zombies", "Third Eye Blind", "Toto", "Tygers of Pan Tang", "Ugly Kid Joe", 
    "Van Der Graaf Generator", "W.A.S.P.", "War", "Ween", "White Lion", "Widespread Panic", "X", 
    "Yardbirds", "Yngwie Malmsteen", "Zebra", "Ziggy Marley and the Melody Makers"
]


additional_bands = [
    "38 Special", "A Flock of Seagulls", "Accept", "Adrian Belew", "Aldo Nova", "Alphaville", "Ambrosia", 
    "Angel", "April Wine", "Argent", "Atomic Rooster", "Babyshambles", "Bananarama", "Barclay James Harvest", 
    "Big Audio Dynamite", "Black Oak Arkansas", "Blodwyn Pig", "Bloodrock", "Bonzo Dog Doo-Dah Band", 
    "Booker T. & the M.G.'s", "Brownsville Station", "Budgie", "Captain Beefheart", "Canned Heat", 
    "Chicory Tip", "City Boy", "Climax Blues Band", "Conway Twitty", "Country Joe and the Fish", 
    "Crack the Sky", "Crazy Horse", "Cursive", "David Crosby", "Dennis DeYoung", "Devil Doll", 
    "Diesel", "Dr. Feelgood", "Electric Prunes", "Elvis Costello and the Attractions", "Eric Burdon", 
    "Family", "Fanny", "Focus", "Foghat", "Franz Ferdinand", "Giant Sand", "Golden Earring", 
    "Graham Parker", "Green On Red", "Gypsy", "Haircut One Hundred", "Hawkwind", "Head East", 
    "Heaven 17", "Herman's Hermits", "Ian Dury", "It Bites", "Jefferson Starship", "Jo Jo Gunne", 
    "Johnny Hates Jazz", "Johnny Winter", "Kayak", "Klaatu", "Krokus", "Lighthouse", "Little River Band", 
    "Long John Baldry", "Love Sculpture", "Magazine", "Mahogany Rush", "Man", "Manic Street Preachers", 
    "Marble Arch", "Max Webster", "MC5", "Moby Grape", "Morcheeba", "Mother Love Bone", 
    "Murray Head", "Nantucket", "Nash the Slash", "Nazareth", "Nektar", "Nils Lofgren", 
    "Norman Greenbaum", "Outlaws", "Ozzy Osbourne", "Pale Saints", "Paul Revere & the Raiders", 
    "Pentangle", "Peter Green", "Pigbag", "Player", "Point Blank", "Poco", "Porcupine Tree", 
    "Portishead", "Pretty Things", "Quicksilver Messenger Service", "Renaissance", "Riot", 
    "Riverside", "Ritchie Blackmore's Rainbow", "Robin Trower", "Roger Hodgson", "Rory Gallagher", 
    "Screaming Jets", "Sensational Alex Harvey Band", "Severed Heads", "Shooting Star", "Shriekback", 
    "Siren", "Soft Machine", "Southside Johnny & the Asbury Jukes", "Spiral Starecase", "Spirit", 
    "Spooky Tooth", "Stackridge", "Stan Ridgway", "Starcastle", "Starsailor", "Steeleye Span", 
    "Strawbs", "Streetheart", "Strife", "Suede", "Super Furry Animals", "Swervedriver", 
    "Sweet", "Tangerine Dream", "Tavares", "Taxxi", "Ten Years After", "The Alarm", "The Amboy Dukes", 
    "The Band", "The Big Dish", "The Cramps", "The Cryan' Shames", "The Dictators", 
    "The Fugs", "The Hollies", "The Incredible String Band", "The Jayhawks", "The Knack", 
    "The La's", "The Mars Volta", "The Nice", "The Psychedelic Furs", "The Saints", 
    "The Shadows", "The Spencer Davis Group", "The Stooges", "The Tea Party", "The The", 
    "The Turtles", "The Vapors", "The Yardbirds", "Thin White Rope", "Thunderclap Newman", 
    "Tommy Tutone", "Tony Joe White", "Traffic", "Triumph", "Trooper", "U.K.", "Ultimate Spinach", 
    "Vanilla Fudge", "Wall of Voodoo", "Wanda Jackson", "Wang Chung", "Wet Willie", "Wishbone Ash", 
    "Wolfmother", "X-Ray Spex", "Y&T", "Yellow Magic Orchestra", "Zebra", "Zero 7", 
    "Ziggy Marley", "Zounds", "Zwan", "Autograph", "Baltimora", "Barenaked Ladies", 
    "Be Bop Deluxe", "Bill Bruford", "Billy Thorpe", "Blitzen Trapper", "Blue Cheer", 
    "Blue Mink", "Boomtown Rats", "Brendan Benson", "Bruce Hornsby", "Calexico", "Chris Isaak", 
    "Clannad", "Commander Cody and His Lost Planet Airmen", "Coven", "Crack the Sky", 
    "Crosby & Nash", "Damnation of Adam Blessing", "Dan Hicks", "Danny Kirwan", "David Lindley", 
    "David Sylvian", "Delaney & Bonnie", "Dixie Dregs", "Donovan", "Doug Sahm", "Dr. Hook", 
    "Earth Opera", "Emitt Rhodes", "England Dan & John Ford Coley", "Fairport Convention", 
    "Flying Burrito Brothers", "Fotheringay", "Gabriel Bondage", "Gentle Giant", 
    "Gerry Rafferty", "Godley & Creme", "Gordon Lightfoot", "Grand Funk Railroad", 
    "Hedgehoppers Anonymous", "Horace Silver", "Ian Hunter", "Iggy Pop", "Jellyfish", 
    "John Cale", "John Mayall's Bluesbreakers", "Johnny Thunder", "Jon and Vangelis", 
    "Junior's Eyes", "Keef Hartley Band", "Kevin Ayers", "Laurie Anderson", "Leo Kottke", 
    "Leslie West", "Lindisfarne", "Loggins and Messina", "Marc Bolan", "Matching Mole", 
    "Michael Nesmith", "Mike Oldfield", "Minutemen", "Moby Grape", "Neil Innes", 
    "Nico", "Nick Drake", "NRBQ", "Os Mutantes", "Pavlov's Dog", "Pentangle", 
    "Peter Gabriel", "Peter, Paul and Mary", "Procol Harum", "Quintessence", 
    "Robin Williamson", "Roger Waters", "Sandy Denny", "Savoy Brown", "Seatrain", 
    "Shane MacGowan", "Sky", "Soft Boys", "Sons of Champlin", "Spirit", "Stackridge", 
    "Steeleye Span", "Steve Hackett", "Steve Hillage", "String Driven Thing", "T. Rex", 
    "Television", "The Band", "The Chambers Brothers", "The Dead Boys", "The Electric Flag"
]