# -*- coding: utf-8 -*-

cities = [
    'Tokyo',
    'Jakarta',
    'New',
    'Seoul',
    'Manila',
    'Mumbai',
    'Sao',
    'Mexico',
    'Delhi',
    'Osaka',
    'Cairo',
    'Kolkata',
    'Los',
    'Shanghai',
    'Moscow',
    'Beijing',
    'Buenos',
    'Guangzhou',
    'Shenzhen',
    'Istanbul',
    'Rio',
    'Paris',
    'Karachi',
    'Nagoya',
    'Chicago',
    'Lagos',
    'London',
    'Bangkok',
    'Kinshasa',
    'Tehran',
    'Lima',
    'Dongguan',
    'Bogota',
    'Chennai',
    'Dhaka',
    'Essen',
    'Tianjin',
    'Hong',
    'Taipei',
    'Lahore',
    'Ho',
    'Bangalore',
    'Hyderabad',
    'Johannesburg',
    'Baghdad',
    'Toronto',
    'Santiago',
    'Kuala',
    'San',
    'Philadelphia',
    'Wuhan',
    'Miami',
    'Dallas',
    'Madrid',
    'Ahmedabad',
    'Boston',
    'Belo',
    'Khartoum',
    'Saint',
    'Shenyang',
    'Houston',
    'Pune',
    'Riyadh',
    'Singapore',
    'Washington',
    'Yangon',
    'Milan',
    'Atlanta',
    'Chongqing',
    'Alexandria',
    'Nanjing',
    'Guadalajara',
    'Barcelona',
    'Chengdu',
    'Detroit',
    'Ankara',
    'Abidjan',
    'Athens',
    'Berlin',
    'Sydney',
    'Monterrey',
    'Phoenix',
    'Busan',
    'Recife',
    'Bandung',
    'Porto',
    'Melbourne',
    'Luanda',
    'Hangzhou',
    'Algiers',
    'H\xc3\xa0',
    'Montr\xc3\xa9Al',
    "Xi'An",
    'Pyongyang',
    'Qingdao',
    'Surat',
    'Fortaleza',
    'Medell\xc3\xadN',
    'Durban',
    'Kanpur',
    'Addis',
    'Nairobi',
    'Jeddah',
    'Naples',
    'Kabul',
    'Salvador',
    'Harbin',
    'Kano',
    'Casablanca',
    'Cape',
    'Curitiba',
    'Surabaya',
    'San',
    'Seattle',
    'Rome',
    'Dar',
    'Taichung',
    'Jaipur',
    'Caracas',
    'Dakar',
    'Kaohsiung',
    'Minneapolis',
    'Lucknow',
    'Amman',
    'Tel',
    'Guayaquil',
    'Kyiv',
    'Faisalabad',
    'Mashhad',
    'Izmir',
    'Rawalpindi',
    'Tashkent',
    'Katowice',
    'Changchun',
    'Campinas',
    'Daegu',
    'Changsha',
    'Nagpur',
    'San',
    'Aleppo',
    'Lisbon',
    'Frankfurt',
    'Nanchang',
    'Birmingham[]',
    'Tampa',
    'Medan',
    'Dalian',
    'Tunis',
    'Shijiazhuang',
    'Manchester',
    'Port-Au-Prince',
    'Damascus',
    "Ji'Nan",
    'Fukuoka',
    'Santo',
    'Havana',
    'Cali',
    'Denver',
    'St.',
    'Colombo',
    'Dubai',
    'Baltimore',
    'Sapporo',
    'Rotterdam',
    'Vancouver',
    'Preston',
    'Patna',
    "Sana'A",
    'Warsaw',
    'Bonn',
    'Accra',
    'Bucharest',
    'Yokohama',
    'Kunming',
    'Guiyang',
    'Zibo',
    'Incheon',
    'Zhengzhou',
    'Taiyuan',
    'Chaoyang',
    'Brasilia',
    'Zhongshan',
    'West',
    'Giza',
    'Quezon',
    'Nanhai',
    'Fuzhou',
    'Lanzhou',
    'Xiamen',
    'Chittagong',
    'Zaozhuang',
    'Jilin',
    'Linyi',
    'Wenzhou',
    'Stockholm',
    'Puebla',
    'Puning',
    'Baku',
    'Ibadan',
    'Brisbane',
    'Minsk',
    'Sikasso',
    'Nanchong',
    'Nanning',
    'Urumqi',
    'Yantai',
    'Fuyang',
    'Tangshan',
    'Maracaibo',
    'Hamburg',
    'Budapest',
    'Shunde',
    'Manaus',
    'Xuzhou',
    'S\xc3\xa9Gou',
    'Baotou',
    'Hefei',
    'Vienna',
    'Indore',
    'Asuncion',
    'Tianmen',
    'Belgrade',
    'Suzhou',
    'Suizhou',
    'Nanyang',
    'Nakuru',
    'Koulikoro',
    'Ningbo',
    'Liuan',
    'Anshan',
    'Tengzhou',
    'Qiqihaer',
    'Pizhou',
    'Taian',
    'Datong',
    'Kobe',
    'Hama',
    'Esfahan',
    'Tripoli',
    'West',
    'Vadodara',
    'Taizhou',
    'Luoyang',
    'Quito',
    'Jinjiang',
    'Mopti',
    'Perth',
    'Daejeon',
    'Kyoto',
    'Xiantao',
    'Tangerang',
    'Bhopal',
    'Coimbatore',
    'Kharkiv',
    'Gwangju',
    'Xinghua',
    'Harare',
    'Fushun',
    'Shangqiu',
    'Bel\xc3\xa9M',
    'Wuxi',
    'Hechuan',
    'Wujin',
    'Guigang',
    'Jianyang',
    'Huhehaote',
    'Santa',
    'Semarang',
    'Ludhiana',
    'Novosibirsk',
    'Neijiang',
    'Maputo',
    "Nan'An",
    'Douala',
    'Weifang',
    'Daqing',
    'Kayes',
    'Tongzhou',
    'Tabriz',
    'Homs',
    'Rugao',
    'Guiping',
    'Huainan',
    'Kochi',
    'Suining',
    'Bozhou',
    'Zhanjiang',
    'Changde',
    'Montevideo',
    'Suzhou',
    'Xintai',
    'Ekaterinoburg',
    'Ju\xc3\xa1Rez',
    'Handan',
    'Visakhapatnam',
    'Kawasaki',
    'Jiangjin',
    'Pingdu',
    'Agra',
    'Jiangyin',
    'Tijuana',
    'Liuyang',
    'Bursa',
    'Al-Hasakeh',
    'Makkah',
    'Yaounde',
    'Xuanwei',
    'Dengzhou',
    'Palembang',
    'Nizhny',
    'Le\xc3\xb3N',
    'Guarulhos',
    'Heze',
    'Auckland',
    'Omdurman',
    'Shantou',
    'Leizhou',
    'Yongcheng',
    'Valencia',
    'Thane',
    'San',
    'Xinyang',
    'Luzhou',
    'Almaty',
    'Changshu',
    'Taixing',
    'Phnom',
    'Laiwu',
    'Xiaoshan',
    'Yiyang',
    'Goi\xc3\xa2Nia',
    'Liuzhou',
    'Gaozhou',
    'Fengcheng',
    'Cixi',
    'Karaj',
    'Mogadishu',
    'Varanasi',
    'C\xc3\xb3Rdoba',
    'Kampala',
    'Ruian',
    'Lianjiang',
    'Huaian',
    'Shiraz',
    'Multan',
    'Madurai',
    'M\xc3\xbcNchen',
    'Kalyan',
    'Quanzhou',
    'Adana',
    'Bazhong',
    'F\xc3\xa8S',
    'Ouagadougou',
    'Haicheng',
    'Xishan',
    'Leiyang',
    'Caloocan',
    'Kalookan',
    'Jingzhou',
    'Saitama',
    'Prague',
    'Fuqing',
    'Kumasi',
    'Meerut',
    'Hyderabad',
    'Lufeng',
    'Dongtai',
    'Yixing',
    'Mianyang',
    'Wenling',
    'Leqing',
    'Ottawa',
    'Yushu',
    'Barranquilla',
    'Hiroshima',
    'Chifeng',
    'Nashik',
    'Makasar',
    'Sofia',
    'Rizhao',
    'Davao',
    'Tianshui',
    'Huzhou',
    'Samara',
    'Omsk',
    'Gujranwala',
    'Adelaide',
    'Macheng',
    'Wuxian',
    'Bijie',
    'Yuzhou',
    'Leshan',
    'La',
    'Rosario',
    'Jabalpur',
    'Kazan',
    'Jimo',
    'Dingzhou',
    'Calgary',
    'Yerevan',
    'El-Jadida',
    'Jamshedpur',
    'Z\xc3\xbcRich',
    'Zoucheng',
    'Pikine-Guediawaye',
    'Anqiu',
    "Guang'An",
    'Chelyabinsk',
    'Conakry',
    'Asansol',
    'Shouguang',
    'Changzhou',
    'Ulsan',
    'Zhuji',
    'Toluca',
    'Marrakech',
    'Dhanbad',
    'Tbilisi',
    'Hanchuan',
    'Lusaka',
    'Qidong',
    'Faridabad',
    'Zaoyang',
    'Zhucheng',
    'Rostov-Na-Donu',
    'Jiangdu',
    'Xiangcheng',
    'Zigong',
    'Jining',
    'Edmonton',
    'Allahabad',
    'Beiliu',
    'Dnipropetrovsk',
    'Gongzhuling',
    'Qinzhou',
    'Ufa',
    'Sendai',
    'Volgograd',
    'Ezhou',
    'Guatemala',
    'Zhongxiang',
    'Amsterdam',
    'Brussels',
    'Bamako',
    'Ziyang',
    'Antananarivo',
    'Mudanjiang',
    'Amritsar',
    'Vijayawada',
    'Haora',
    'Donetsk',
    'Huazhou',
    'Fuzhou',
    'Pimpri',
    'Dublin',
    'Rajkot',
    'Sao',
    'B\xc3\xa9Ni-Mellal',
    'Lianyuan',
    'Liupanshui',
    'Kaduna',
    'Kitakyushu',
    'Qianjiang',
    'Perm',
    'Odessa',
    'Qom',
    'Yongchuan',
    'Peshawar',
    'Linzhou',
    'Benxi',
    'Ulaanbaatar',
    'Zhangqiu',
    'Yongzhou',
    'Sao',
    'Srinagar',
    'Ghaziabad',
    'Xinyi',
    'K\xc3\xb6Ln',
    'Zhangjiagang',
    'Wafangdian',
    'Xianyang',
    'Liaocheng',
    'Ahwaz',
    'Taishan',
    'Linhai',
    'Feicheng',
    'Suwon',
    'Wuwei',
    'Haimen',
    'San',
    'Liling',
    'Xinhui',
    'Gaziantep',
    'Krasnoyarsk',
    'Chiba',
    'Voronezh',
    'Durg-Bhilai',
    'Ruzhou',
    'Macei\xc3\xb3',
    'Yichun',
    'Al-Madinah',
    'Yulin',
    'Seongnam',
    'Yueyang',
    'Yiwu',
    'San',
    'Jixi',
    'Managua',
    'Xinyi',
    'Safi',
    'Guangyuan',
    'Soweto',
    'Zhangjiakou',
    'Baoding',
    'Cartagena',
    'Huludao',
    'Pingdingshan',
    'Torino',
    'Zengcheng',
    'Laiyang',
    'Qingzhou',
    'Aurangabad',
    'Lattakia',
    'M\xc3\xa9Rida',
    'Laizhou',
    'Thiruvananthapuram',
    'Weinan',
    'Wuchang',
    'Guangshui',
    'Gaizhou',
    'G\xc3\xb6Teborg',
    'Xiaogan',
    'Torre\xc3\xb3N',
    'Jiaxing',
    'Kozhikode',
    'Sal\xc3\xa9',
    'Zhuzhou',
    'Tyneside',
    'Hengyang',
    'Dehui',
    'Honghu',
    'Danyang',
    'Daye',
    'Solapur',
    'Xingning',
    'Xiangfan',
    'Shubra-El-Khema',
    'Luoding',
    'Gwalior',
    'Ranchi',
    'Huiyang',
    'Mombasa',
    'Jinzhou',
    'Jiangyan',
    'Chenghai',
    'Jiamusi',
    'Songzi',
    'Tegucigalpa',
    'Wujiang',
    'Jodhpur',
    'Duque',
    "Xi'Ning",
    'Yuyao',
    'Hezhou',
    'Jiangyou',
    'Tiruchchirappalli',
    'Baoshan',
    'Saratov',
    'Nova',
    'Ankang',
    'Gaomi',
    'Yangchun',
    'Santiago',
    'Danzhou',
    'La',
    'Zhuanghe',
    'Zhuhai',
    'Zhaodong',
    'Sakai',
    'Haikou',
    'Jiaonan',
    'El',
    'Xuancheng',
    'Wuchuan',
    'Yuhang',
    'Qinhuangdao',
    'Bogor',
    'Kermanshah',
    'Longhai',
    'Liverpool',
    'Yanshi',
    'Guwahati',
    'Yichun',
    'Konya',
    'Barquisimeto',
    'Yingde',
    'Bengbu',
    'Yibin',
    'Chandigarh',
    'Xiangxiang',
    'Yinchuan',
    'Valencia',
    'Guilin',
    'Hamamatsu',
    'Sao',
    'Deir',
    'Bishkek',
    'Teresina',
    'Suihua',
    'Benghazi',
    'Jiutai',
    'Meishan',
    'Zaporizhya',
    'Gaoyou',
    'Marseille',
    'Kaifeng',
    'Changning',
    'Tongliao',
    'Natal',
    'Bandar',
    'Dongying',
    'Gaoan',
    'Langzhong',
    'Lichuan',
    'Hubli-Dharwad',
    'Mysore',
    'Niigata',
    'Indianapolis',
    'Jiaozhou',
    'Pingxiang',
    'Haiphong',
    'Arequipa',
    'Jacksonville',
    'Tanger',
    'Dandong',
    'Kishinev',
    'Krasnodar',
    'Zagreb',
    'Xinmi',
    'Chaohu',
    'Xinyu',
    'Gongyi',
    'Huixian',
    'Xinxiang',
    'Port',
    'Mendoza',
    'Nantong',
    'Pengzhou',
    'Khulna',
    'Malang',
    'Padang',
    'Anyang',
    'Renqiu',
    'Foshan',
    'Anshun',
    'Chihuahua',
    'Campo',
    'L\xc3\xb3Dz',
    'Goyang',
    'Benin',
    'Bucheon',
    'Gaocheng',
    'Pulandian',
    'Hejian',
    'Dafeng',
    'Krak\xc3\xb3w',
    'Enshi',
    'Dongyang',
    'Lviv',
    'Kunshan',
    'Shuangcheng',
    'Salem',
    'Jiaozuo',
    'Ad-Dammam',
    'Huaibei',
    'Liyang',
    'Samut',
    'Rongcheng',
    'Cenxi',
    'Nampho',
    'Columbus',
    'Bareilly',
    'Leping',
    'Laixi',
    'Liaoyang',
    'Zhaotong',
    'Jerusalem',
    'Tainan',
    'Cuernavaca',
    'Riga',
    'Linfen',
    'Qu\xc3\xa9Bec',
    'Lingbao',
    'Shangyu',
    'Wuan',
    'Hailun',
    'Xingyi',
    'Wuxue',
    'Cebu',
    'Aguascalientes',
    'Tolyatti',
    'Hamilton',
    'Zhoushan',
    'Langfang',
    'Osasco',
    'Nonthaburi',
    'Dashiqiao',
    'Tongxiang',
    'Yichang',
    'Yangzhou',
    'Blantyre',
    'Hamhung',
    'Jalandhar',
    'Al-Rakka',
    'Niamey',
    'Xiangtan',
    'Winnipeg',
    'Oran',
    'Kota',
    'Sevilla',
    'Navi',
    'Port',
    'Saltillo',
    'Khartoum',
    'Shizuoka',
    'Yuanjiang',
    'Raipur',
    'Kryviy',
    'Yingkou',
    'Wuhu',
    'Zhenjiang',
    'Quer\xc3\xa9Taro',
    'Nankang',
    'Wugang',
    'Hegang',
    'Linqing',
    'Pretoria',
    'Zunyi',
    'Panzhihua',
    'Austin',
    'Changle',
    'Lianyungang',
    'Yancheng',
    'Zunhua',
    'Changyi',
    'Mekn\xc3\xa8S',
    'Qiongshan',
    'Bulawayo',
    'Wendeng',
    'Okayama',
    'Santo',
    'Rabat',
    'Pakanbaru',
    'Nehe',
    'Memphis',
    'Joao',
    'Kathmandu',
    'Longkou',
    'Shengzhou',
    'Antalya',
    'Kumamoto',
    'Lilongwe',
    'Mexicali',
    'Kaiping',
    'Palermo',
    'Aligarh',
    'Nottingham',
    'Haining',
    'Mosul',
    'Hermosillo',
    'Tongcheng',
    'Shulan',
    'Miluo',
    'Bhubaneswar',
    'Yangquan',
    'Chenzhou',
    'Haiyang',
    'Morelia',
    'Huangshi',
    'Xinmin',
    'T\xc3\xa9Touan',
    'Barnaul',
    'Qixia',
    'Jaboatao',
    'Chongzhou',
    'Cotonou',
    'Yingcheng',
    'Zaragoza',
    'Changzhi',
    'Qujing',
    'Linghai',
    'Changge',
    'Trujillo',
    'Tampico',
    'Maoming',
    'Mor\xc3\xb3N',
    'La',
    'Ciudad',
    'Moradabad',
    'Jieshou',
    'Sheffield',
    'Donggang',
    'Jingjiang',
    'Acheng',
    'Acapulco',
    'Veracruz',
    'Ulyanovsk',
    'Wroclaw',
    'Jieyang',
    'Shaoxing',
    "Qian'An",
    'Nanchuan',
    'Qionglai',
    'Deyang',
    'Sagamihara',
    'Fuyang',
    'Fuxin',
    'Jiyuan',
    'Puente',
    'Qufu',
    'Gaoyao',
    'Gorakhpur',
    'Fort',
    'Xinji',
    'San',
    'Dujiangyan',
    'The',
    'Bhiwandi',
    'Culiac\xc3\xa1N',
    'Lingyuan',
    'Xingyang',
    'Maiduguri',
    'Genova',
    'Meihekou',
    'Izhevsk',
    'Jeonju',
    'Leling',
    'Xichang',
    'Colombo',
    'Zaria',
    'Anlu',
    'Sao',
    'Charlotte',
    'Yizheng',
    'Malm\xc3\xb6',
    'Weihai',
    'Xinzheng',
    'Dengfeng',
    'Vladivostok',
    'Shaoyang',
    'Taizhou',
    'Jammu',
    'Lanxi',
    'Yuncheng',
    'Kagoshima',
    'Yaroslave',
    'Contagem',
    'Shishou',
    'Panjin',
    'Zamboanga',
    'Orumiyeh',
    'Binzhou',
    'Kisumu',
    'Baoji',
    'Uberl\xc3\xa2Ndia',
    'El',
    'Yunzhou',
    'K\xc3\xa9Nitra',
    'Diyarbakir',
    'Jurong',
    'C\xc3\xbaCuta',
    'Zhaoyuan',
    'Huizhou',
    'Tianchang',
    'Dortmund',
    'Shihezi',
    'Shiyan',
    'Cuttack',
    'Cochabamba',
    'Cheongju',
    'Jingmen',
    'Shangzhi',
    'Anqing',
    'Chongjin',
    'Stuttgart',
    'Rushan',
    'Kingston',
    'Milwaukee',
    'Sorocaba',
    'Glasgow',
    'Khabarovsk',
    'Guanghan',
    'Warangal',
    'Irkutsk',
    'Tyumen',
    'Lomas',
    'Beipiao',
    'Funabashi',
    'Mingguang',
    'D\xc3\xbcSseldorf',
    'Shenzhou',
    'I\xc3\xa7El',
    'Zhangzhou',
    'Xianning',
    'Maanshan',
    'Bandjarmasin',
    'Callao',
    'Poznan',
    'Kayseri',
    'Chon',
    'Quetta',
    'Shuozhou',
    'Samarinda',
    'Helsinki',
    'Akesu',
    'Novokuznetsk',
    'M\xc3\xa1Laga',
    'Fengcheng',
    'Hachioji',
    'Ribeirao',
    'Beihai',
    'Jamnagar',
    'Nouakchott',
    'Bazhou',
    'Yongkang',
    'Louisville',
    'Chizhou',
    'Huaiyin',
    'Fuan',
    'Bhilai',
    'Dezhou',
    'Makhachkala',
    'Xingping',
    'Jiujiang',
    'Bristol',
    'Botou',
    'Fengnan',
    'Astana',
    'Yizhou',
    'Amravati',
    'Nashville-Davidson',
    'Batam',
    'Orenburg',
    'Zhuozhou',
    'Las',
    'Cancun',
    'Longyan',
    'Oslo',
    'Cuiab\xc3\xa1',
    'Tiruppur',
    'Vilnius',
    'Bremen',
    'Gold',
    'Gaobeidian',
    'Mangalore',
    'Songyuan',
    'Yangjiang',
    'Wanyuan',
    'Jiangmen',
    'Xingtai',
    'Shaoguan',
    'Feira',
    'Guixi',
    'Ruijin',
    'Zahedan',
    'Jinzhong',
    'Portland',
    'Jintan',
    'Reynosa',
    'Ilorin',
    'Oklahoma',
    'Nakhon',
    "N'Djamena",
    'Shangzhou',
    'Panshi',
    'Kerman',
    'Kaiyuan',
    'Islamabad',
    'Sarajevo',
    'Bikaner',
    'Dushanbe',
    'Vientiane',
    'Dehradun',
    'Zhangshu',
    'Beining',
    'Abu',
    'Shimkent',
    'Xingcheng',
    'Imbaba',
    'Yicheng',
    'Skoplje',
    'Kadhimain',
    "At-Ta'If",
    'Dali',
    'Fuding',
    'Jinzhou',
    'Renhuai',
    'Mira-Bhayandar',
    'Kemerovo',
    'Duisburg',
    'Rasht'
]

