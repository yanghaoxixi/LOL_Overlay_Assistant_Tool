__author__ = 'Aaron Yang'
__email__ = 'byang971@usc.edu'
__date__ = '2/16/2020 2:39 PM'

BANNED_LABEL_NAME = ['Aatrox',
                     'Ahri',
                     'Akali',
                     'Alistar',
                     'Amumu',
                     'Anivia',
                     'Annie',
                     'Aphelios',
                     'Ashe',
                     'Aurelion Sol',
                     'Azir',
                     'Bard',
                     'Blitzcrank',
                     'Brand',
                     'Braum',
                     'Caitlyn',
                     'Camille',
                     'Cassiopeia',
                     "Cho'Gath",
                     'Corki',
                     'Darius',
                     'Diana',
                     'Dr. Mundo',
                     'Draven',
                     'Ekko',
                     'Elise',
                     'Evelynn',
                     'Ezreal',
                     'Fiddlesticks',
                     'Fiora',
                     'Fizz',
                     'Galio',
                     'Gangplank',
                     'Garen',
                     'Gnar',
                     'Gragas',
                     'Graves',
                     'Hecarim',
                     'Heimerdinger',
                     'Illaoi',
                     'Irelia',
                     'Ivern',
                     'Janna',
                     'Jarvan IV',
                     'Jax',
                     'Jayce',
                     'Jhin',
                     'Jinx',
                     "Kai'Sa",
                     'Kalista',
                     'Karma',
                     'Karthus',
                     'Kassadin',
                     'Katarina',
                     'Kayle',
                     'Kayn',
                     'Kennen',
                     "Kha'Zix",
                     'Kindred',
                     'Kled',
                     "Kog'Maw",
                     'LeBlanc',
                     'Lee Sin',
                     'Leona',
                     'Lissandra',
                     'Lucian',
                     'Lulu',
                     'Lux',
                     'Malphite',
                     'Malzahar',
                     'Maokai',
                     'Master Yi',
                     'Miss Fortune',
                     'Mordekaiser',
                     'Morgana',
                     'Nami',
                     'Nasus',
                     'Nautilus',
                     'Neeko',
                     'Nidalee',
                     'Nocturne',
                     'None',
                     'None2',
                     'Nothing',
                     'Nunu & Willump',
                     'Olaf',
                     'Orianna',
                     'Ornn',
                     'Pantheon',
                     'Poppy',
                     'Pyke',
                     'Qiyana',
                     'Quinn',
                     'Rakan',
                     'Rammus',
                     "Rek'Sai",
                     'Renekton',
                     'Rengar',
                     'Riven',
                     'Rumble',
                     'Ryze',
                     'Sejuani',
                     'Senna',
                     'Sett',
                     'Shaco',
                     'Shen',
                     'Shyvana',
                     'Singed',
                     'Sion',
                     'Sivir',
                     'Skarner',
                     'Sona',
                     'Soraka',
                     'Swain',
                     'Sylas',
                     'Syndra',
                     'Tahm Kench',
                     'Taliyah',
                     'Talon',
                     'Taric',
                     'Teemo',
                     'Thresh',
                     'Tristana',
                     'Trundle',
                     'Tryndamere',
                     'Twisted Fate',
                     'Twitch',
                     'Udyr',
                     'Urgot',
                     'Varus',
                     'Vayne',
                     'Veigar',
                     "Vel'Koz",
                     'Vi',
                     'Viktor',
                     'Vladimir',
                     'Volibear',
                     'Warwick',
                     'Wukong',
                     'Xayah',
                     'Xerath',
                     'Xin Zhao',
                     'Yasuo',
                     'Yorick',
                     'Yuumi',
                     'Zac',
                     'Zed',
                     'Ziggs',
                     'Zilean',
                     'Zoe',
                     'Zyra']

LABEL_NAME = ['Aatrox',
              'Ahri',
              'Akali',
              'Alistar',
              'Amumu',
              'Anivia',
              'Annie',
              'Aphelios',
              'Ashe',
              'Aurelion Sol',
              'Azir',
              'Bard',
              'Blitzcrank',
              'Brand',
              'Braum',
              'Caitlyn',
              'Camille',
              'Cassiopeia',
              "Cho'Gath",
              'Corki',
              'Darius',
              'Diana',
              'Dr. Mundo',
              'Draven',
              'Ekko',
              'Elise',
              'Evelynn',
              'Ezreal',
              'Fiddlesticks',
              'Fiora',
              'Fizz',
              'Galio',
              'Gangplank',
              'Garen',
              'Gnar',
              'Gragas',
              'Graves',
              'Hecarim',
              'Heimerdinger',
              'Illaoi',
              'Irelia',
              'Ivern',
              'Janna',
              'Jarvan IV',
              'Jax',
              'Jayce',
              'Jhin',
              'Jinx',
              "Kai'Sa",
              'Kalista',
              'Karma',
              'Karthus',
              'Kassadin',
              'Katarina',
              'Kayle',
              'Kayn',
              'Kennen',
              "Kha'Zix",
              'Kindred',
              'Kled',
              "Kog'Maw",
              'LeBlanc',
              'Lee Sin',
              'Leona',
              'Lissandra',
              'Lucian',
              'Lulu',
              'Lux',
              'Malphite',
              'Malzahar',
              'Maokai',
              'Master Yi',
              'Miss Fortune',
              'Mordekaiser',
              'Morgana',
              'Nami',
              'Nasus',
              'Nautilus',
              'Neeko',
              'Nidalee',
              'Nocturne',
              'Nunu & Willump',
              'Olaf',
              'Orianna',
              'Ornn',
              'Pantheon',
              'Poppy',
              'Pyke',
              'Qiyana',
              'Quinn',
              'Rakan',
              'Rammus',
              "Rek'Sai",
              'Renekton',
              'Rengar',
              'Riven',
              'Rumble',
              'Ryze',
              'Sejuani',
              'Senna',
              'Sett',
              'Shaco',
              'Shen',
              'Shyvana',
              'Singed',
              'Sion',
              'Sivir',
              'Skarner',
              'Sona',
              'Soraka',
              'Swain',
              'Sylas',
              'Syndra',
              'Tahm Kench',
              'Taliyah',
              'Talon',
              'Taric',
              'Teemo',
              'Thresh',
              'Tristana',
              'Trundle',
              'Tryndamere',
              'Twisted Fate',
              'Twitch',
              'Udyr',
              'Urgot',
              'Unselected',
              'Varus',
              'Vayne',
              'Veigar',
              "Vel'Koz",
              'Vi',
              'Viktor',
              'Vladimir',
              'Volibear',
              'Warwick',
              'Wukong',
              'Xayah',
              'Xerath',
              'Xin Zhao',
              'Yasuo',
              'Yorick',
              'Yuumi',
              'Zac',
              'Zed',
              'Ziggs',
              'Zilean',
              'Zoe',
              'Zyra']

MINI_MAP_CHAMP_LIST = ['Aatrox',
                       'Ahri',
                       'Akali',
                       'Alistar',
                       'Amumu',
                       'Anivia',
                       'Annie',
                       'Aphelios',
                       'Ashe',
                       'Aurelion Sol',
                       'Azir',
                       'Bard',
                       'Blitzcrank',
                       'Brand',
                       'Braum',
                       'Caitlyn',
                       'Camille',
                       'Cassiopeia',
                       "Cho'Gath",
                       'Corki',
                       'Darius',
                       'Diana',
                       'Dr. Mundo',
                       'Draven',
                       'Ekko',
                       'Elise',
                       'Evelynn',
                       'Ezreal',
                       'Fiddlesticks',
                       'Fiora',
                       'Fizz',
                       'Galio',
                       'Gangplank',
                       'Garen',
                       'Gnar',
                       'Gragas',
                       'Graves',
                       'Hecarim',
                       'Heimerdinger',
                       'Illaoi',
                       'Irelia',
                       'Ivern',
                       'Janna',
                       'Jarvan IV',
                       'Jax',
                       'Jayce',
                       'Jhin',
                       'Jinx',
                       "Kai'Sa",
                       'Kalista',
                       'Karma',
                       'Karthus',
                       'Kassadin',
                       'Katarina',
                       'Kayle',
                       'Kayn',
                       'Kayn-Blue',
                       'Kayn-Red',
                       'Kennen',
                       "Kha'Zix",
                       'Kindred',
                       'Kled',
                       "Kog'Maw",
                       'LeBlanc',
                       'Lee Sin',
                       'Leona',
                       'Lissandra',
                       'Lucian',
                       'Lulu',
                       'Lux',
                       'Malphite',
                       'Malzahar',
                       'Maokai',
                       'Master Yi',
                       'Miss Fortune',
                       'Mordekaiser',
                       'Morgana',
                       'Nami',
                       'Nasus',
                       'Nautilus',
                       'Neeko',
                       'Nidalee',
                       'Noctourne',
                       'Nunu & Willump',
                       'Olaf',
                       'Orianna',
                       'Ornn',
                       'Pantheon',
                       'Poppy',
                       'Pyke',
                       'Qiyana',
                       'Quinn',
                       'Rakan',
                       'Rammus',
                       "Rek'Sai",
                       'Renekton',
                       'Rengar',
                       'Riven',
                       'Rumble',
                       'Ryze',
                       'Sejuani',
                       'Senna',
                       'Sett',
                       'Shaco',
                       'Shen',
                       'Shyvana',
                       'Singed',
                       'Sion',
                       'Sivir',
                       'Skarner',
                       'Sona',
                       'Soraka',
                       'Swain',
                       'Sylas',
                       'Syndra',
                       'Tahm Kench',
                       'Taliyah',
                       'Talon',
                       'Taric',
                       'Teemo',
                       'Thresh',
                       'Tristana',
                       'Trundle',
                       'Tryndamere',
                       'Twisted Fate',
                       'Twitch',
                       'Udyr',
                       'Urgot',
                       'Varus',
                       'Vayne',
                       'Veigar',
                       "Vel'Koz",
                       'Vi',
                       'Viktor',
                       'Vladimir',
                       'Volibear',
                       'Warwick',
                       'Wukong',
                       'Xayah',
                       'Xerath',
                       'Xin Zhao',
                       'Yasuo',
                       'Yorick',
                       'Yuumi',
                       'Zac',
                       'Zed',
                       'Ziggs',
                       'Zilean',
                       'Zoe',
                       'Zyra']

NONE_LIST = ['Nothing', 'None', 'None2', 'Unselected', 'none']
