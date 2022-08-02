from models.animeFilm import AnimeFilmModel
from models.comment import CommentModel

animeFilms_list = [

  AnimeFilmModel(
    title="Princess Mononoke", 
    original_title= "もののけ姫", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/jHWmNr7m544fJ8eItsfNk8fs2Ed.jpg",
    director= "Hayao Miyazaki",  
    producer= "Toshio Suzuki", 
    release_date= "1997", 
    description="Ashitaka, a prince of the disappearing Ainu tribe, is cursed by a demonized boar god and must journey to the west to find a cure. Along the way, he encounters San, a young human woman fighting to protect the forest, and Lady Eboshi, who is trying to destroy it. Ashitaka must find a way to bring balance to this conflict.", 
  ),

  AnimeFilmModel(
    title= "Spirited Away", 
    original_title= "千と千尋の神隠し", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
    director= "Hayao Miyazaki", 
    producer= "Toshio Suzuki",
    release_date= "2001", 
    description= "Spirited Away is an Oscar winning Japanese animated film about a ten year old girl who wanders away from her parents along a path that leads to a world ruled by strange and unusual monster-like animals. Her parents have been changed into pigs along with others inside a bathhouse full of these creatures. Will she ever see the world how it once was?",
  ),

    AnimeFilmModel(
    title= "Howl's Moving Castle", 
    original_title= "ハウルの動く城", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/TkTPELv4kC3u1lkloush8skOjE.jpg",
    director= "Hayao Miyazaki", 
    producer= "Toshio Suzuki",
    release_date= "2004", 
    description= "When Sophie, a shy young woman, is cursed with an old body by a spiteful witch, her only chance of breaking the spell lies with a self-indulgent yet insecure young wizard and his companions in his legged, walking home.",
    ),

    AnimeFilmModel(
    title= "My Neighbor Totoro", 
    original_title= "となりのトトロ", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/rtGDOeG9LzoerkDGZF9dnVeLppL.jpg",
    director= "Hayao Miyazaki", 
    producer= "Hayao Miyazaki",
    release_date= "1988", 
    description= "Two sisters move to the country with their father in order to be closer to their hospitalized mother, and discover the surrounding trees are inhabited by Totoros, magical spirits of the forest. When the youngest runs away from home, the older sister seeks help from the spirits to find her.",
    ),

    AnimeFilmModel(
    title= "Castle In The Sky", 
    original_title= "天空の城ラピュタ", 
    image= "https://image.tmdb.org/t/p/w600_and_h900_bestv2/npOnzAbLh6VOIu3naU5QaEcTepo.jpg",
    director= "Hayao Miyazaki", 
    producer= "Isao Takahata",
    release_date= "1986", 
    description= "The orphan Sheeta inherited a mysterious crystal that links her to the mythical sky-kingdom of Laputa. With the help of resourceful Pazu and a rollicking band of sky pirates, she makes her way to the ruins of the once-great civilization. Sheeta and Pazu must outwit the evil Muska, who plans to use Laputa's science to make himself ruler of the world.",
    ),

    AnimeFilmModel(
    title= "The Girl Who Leaped Throught Time", 
    original_title= "時をかける少女", 
    image= "https://flxt.tmsimg.com/assets/p8471376_p_v8_ab.jpg",
    director= "Mamoru Hosoda", 
    producer= "Takashi Watanabe, Yuichiro Saito",
    release_date= "2010", 
    description= "Makoto Konno is in her last year of high school, but is having a hard time deciding what to do with her future. In between enduring the pressure of her teachers and killing time with her best friends, Makoto's life suddenly changes when she accidentally discovers that she is capable of literally leaping through time. Toki wo Kakeru Shoujo follows Makoto as she plays around with her newfound power. However, she soon learns the hard way that every choice has a consequence, and time is a lot more complicated than it may seem.",
    ),

]


comments_list = [
  CommentModel(content="This is a great anime", animeFilm_id=1)
]

