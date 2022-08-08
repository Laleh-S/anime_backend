from models.anime import animeModel
from models.comment import CommentModel
from models.genre import GenreModel


family_genre = GenreModel(name="family")
adventure_genre = GenreModel(name="adventure")
fantasy_genre = GenreModel(name="fantasy")
romance_genre = GenreModel(name="romance")
scifi_genre = GenreModel(name="sci-fi")



animes_list = [

  animeModel(
    title="Princess Mononoke", 
    original_title= "もののけ姫", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/jHWmNr7m544fJ8eItsfNk8fs2Ed.jpg",
    director= "Hayao Miyazaki",  
    producer= "Toshio Suzuki", 
    release_date= "1997", 
    description="Ashitaka, a prince of the disappearing Ainu tribe, is cursed by a demonized boar god and must journey to the west to find a cure. Along the way, he encounters San, a young human woman fighting to protect the forest, and Lady Eboshi, who is trying to destroy it. Ashitaka must find a way to bring balance to this conflict.", 
    genres=[fantasy_genre, adventure_genre],
    user_id=1
  ),

    animeModel(
    title= "Spirited Away", 
    original_title= "千と千尋の神隠し", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
    director= "Hayao Miyazaki", 
    producer= "Toshio Suzuki",
    release_date= "2001", 
    description= "Spirited Away is an Oscar winning Japanese animated film about a ten year old girl who wanders away from her parents along a path that leads to a world ruled by strange and unusual monster-like animals. Her parents have been changed into pigs along with others inside a bathhouse full of these creatures. Will she ever see the world how it once was?",
    genres=[fantasy_genre, adventure_genre],
    user_id=1
  ),

  animeModel(
    title= "A Letter to Momo", 
    original_title= "ももへの手紙", 
    image= "https://flxt.tmsimg.com/assets/p9288437_v_v13_ac.jpg",
    director= "Hiroyuki Okiura", 
    producer= "Arimasa Okada, Keiko Matsushita, Mariko Noguchi, Motoki Mukaichi",
    release_date= "2012", 
    description= "After the unexpected death of her father, 11-year-old Momo Miyaura leaves Tokyo with her mother and moves to an old remote island in Seto Inland Sea. The only memento she has from her father is an unfinished letter with only two words inside: ‘Dear Momo’ along with her heart's unrest from it. In the new and unfamiliar small town, Momo reluctantly tries to adjust to the outmoded wooden buildings, silent crop fields, and mysterious isolated shrines. One day, while exploring the attic of her new home, she finds a worn out picture book about youkai. Following this discovery, strange things begin to happen around town, and Momo is greeted by the arrival of three troublesome youkai.",
    genres=[fantasy_genre, adventure_genre],
    user_id=1
    ),


    animeModel(
    title="Howl's Moving Castle", 
    original_title= "もののけ姫", 
    image= "https://flxt.tmsimg.com/assets/p36095_p_v10_ac.jpg",
    director= "Hayao Miyazaki",  
    producer= "Toshio Suzuki", 
    release_date= "1997", 
    description="Ashitaka, a prince of the disappearing Ainu tribe, is cursed by a demonized boar god and must journey to the west to find a cure. Along the way, he encounters San, a young human woman fighting to protect the forest, and Lady Eboshi, who is trying to destroy it. Ashitaka must find a way to bring balance to this conflict.", 
    genres=[fantasy_genre, adventure_genre],
    user_id=1
  ),
    animeModel(
    title= "The Garden of Words", 
    original_title= "言の葉の庭", 
    image= "https://flxt.tmsimg.com/assets/p10191455_p_v10_af.jpg",
    director= "Makoto Shinkai", 
    producer= "Noritaka Kawaguchi",
    release_date= "2013", 
    description= "On a rainy morning in Tokyo, Takao Akizuki, an aspiring shoemaker, decides to skip class to sketch designs in a beautiful garden. This is where he meets Yukari Yukino, a beautiful yet mysterious woman, for the very first time. Offering to make her new shoes, Takao continues to meet with Yukari throughout the rainy season, and without even realizing it, the two are able to alleviate the worries hidden in their hearts just by being with each other. However, their personal struggles have not disappeared completely, and as the end of the rainy season approaches, their relationship will be put to the test.",
    genres=[fantasy_genre, adventure_genre],
    user_id=1
  ),

    animeModel(
    title= "The Girl Who Leaped Throught Time", 
    original_title= "時をかける少女", 
    image= "https://flxt.tmsimg.com/assets/p8471376_p_v8_ab.jpg",
    director= "Mamoru Hosoda", 
    producer= "Takashi Watanabe, Yuichiro Saito",
    release_date= "2010", 
    description= "Makoto Konno is in her last year of high school, but is having a hard time deciding what to do with her future. In between enduring the pressure of her teachers and killing time with her best friends, Makoto's life suddenly changes when she accidentally discovers that she is capable of literally leaping through time. Toki wo Kakeru Shoujo follows Makoto as she plays around with her newfound power. However, she soon learns the hard way that every choice has a consequence, and time is a lot more complicated than it may seem.",
    genres=[romance_genre, scifi_genre],
    user_id=1
    ),

    animeModel(
    title= "Your Name", 
    original_title= "	君の名は。", 
    image= "https://flxt.tmsimg.com/assets/p13514865_v_v10_aa.jpg",
    director= "	Makoto Shinkai", 
    producer= "Koichiro Ito, Katsuhiro Takei",
    release_date= "2016", 
    description= "Mitsuha, a high school girl living in a rural town deep in the mountains, has a dream that she is a boy living an unfamiliar life in Tokyo. Taki, a high school boy living in Tokyo, dreams that he is a girl living in the mountains. As they realize they are changing places, their encounter sets the cogs of fate into motion.",
    genres=[fantasy_genre, adventure_genre],
    user_id=1
    ),

  
    animeModel(
    title= "Mirai", 
    original_title= "未来のミライ", 
    image= "https://flxt.tmsimg.com/assets/p16293880_v_v13_aa.jpg",
    director= "	Mamoru Hosoda", 
    producer= "Yuichiro Saito, Takuya Itō, Yūichi Adachi, Genki Kawamura",
    release_date= "2018", 
    description= "In a quiet corner of the city, four-year-old Kun Oota has lived a spoiled life as an only child with his parents and the family dog, Yukko. But when his new baby sister Mirai is brought home, his simple life is thrown upside-down; suddenly, it isn't all about him anymore. Despite his tantrums and nagging, Mirai is seemingly now the subject of all his parents' love. To help him adapt to this drastic change, Kun is taken on an extraordinary journey through time, meeting his family's past, present, and future selves, as he learns not only what it means to be a part of a family, but also what it means to be an older brother.",
    genres=[fantasy_genre, adventure_genre],
    user_id=1
    ),

    animeModel(
    title= "My Neighbor Totoro", 
    original_title= "となりのトトロ", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/rtGDOeG9LzoerkDGZF9dnVeLppL.jpg",
    director= "Hayao Miyazaki", 
    producer= "Hayao Miyazaki",
    release_date= "1988", 
    description= "Two sisters move to the country with their father in order to be closer to their hospitalized mother, and discover the surrounding trees are inhabited by Totoros, magical spirits of the forest. When the youngest runs away from home, the older sister seeks help from the spirits to find her.",
    genres=[fantasy_genre, family_genre],
    user_id=1
    ),

    animeModel(
    title= "Castle In The Sky", 
    original_title= "天空の城ラピュタ", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/npOnzAbLh6VOIu3naU5QaEcTepo.jpg",
    director= "Hayao Miyazaki", 
    producer= "Isao Takahata",
    release_date= "1986", 
    description= "The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
    genres=[fantasy_genre, adventure_genre],
    user_id=1
    ),

    

]


comments_list = [
  CommentModel(content="This is a great anime", anime_id=1, user_id=1)
]

