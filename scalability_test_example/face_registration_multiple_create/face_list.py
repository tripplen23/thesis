import random 

face_list1 = [
    "../imgs/Pewdiepie_chinhdien_1.jpg",
    "../imgs/ben.jpg",
    "../imgs/000050.jpg",
    "../imgs/000051.jpg",
    "../imgs/000052.jpg",
    "../imgs/000053.jpg",
    "../imgs/000054.jpg",
    "../imgs/000055.jpg",  
    "../imgs/000056.jpg",  
    "../imgs/000057.jpg",  
    "../imgs/000058.jpg",
    "../imgs/000063.jpg",
    "../imgs/000064.jpg",
    "../imgs/000065.jpg",
    "../imgs/000066.jpg",
    "../imgs/000068.jpg",
    "../imgs/000069.jpg",
    "../imgs/000071.jpg",
    "../imgs/000072.jpg",
    "../imgs/000074.jpg",
    "../imgs/000076.jpg",
    "../imgs/000077.jpg",
    "../imgs/000078.jpg",
    "../imgs/000079.jpg",
    "../imgs/000080.jpg",
    "../imgs/000081.jpg",
    "../imgs/000082.jpg",
    "../imgs/000083.jpg",
    "../imgs/000084.jpg",
    "../imgs/000085.jpg",
    "../imgs/000087.jpg",
    "../imgs/000089.jpg",
    "../imgs/000090.jpg",
    "../imgs/000091.jpg",
    "../imgs/000092.jpg",
    "../imgs/000093.jpg",
    "../imgs/000094.jpg",
    "../imgs/000095.jpg",
    "../imgs/000096.jpg",
    "../imgs/000097.jpg",
    "../imgs/000099.jpg",
    "../imgs/000048.jpg",
    "../imgs/000047.jpg",
    "../imgs/000046.jpg",
    "../imgs/000045.jpg",
    "../imgs/000044.jpg",
    "../imgs/000043.jpg",
    "../imgs/000042.jpg",
    "../imgs/000040.jpg",
    "../imgs/000038.jpg",
    "../imgs/000035.jpg",
    "../imgs/000034.jpg",
    "../imgs/000033.jpg",
    "../imgs/000032.jpg",
    "../imgs/000031.jpg",
    "../imgs/000030.jpg",
    "../imgs/000029.jpg",
    "../imgs/000028.jpg",
    "../imgs/000026.jpg",
    "../imgs/000025.jpg",
    "../imgs/000024.jpg",
    "../imgs/000023.jpg",
    "../imgs/000022.jpg",
    "../imgs/000021.jpg",
    "../imgs/000020.jpg",
    "../imgs/000019.jpg",
    "../imgs/000018.jpg",
    "../imgs/000017.jpg",
    "../imgs/000016.jpg",
    "../imgs/000015.jpg",
    "../imgs/000014.jpg",
    "../imgs/000013.jpg",
    "../imgs/000012.jpg",
    "../imgs/000011.jpg",
    "../imgs/000010.jpg",
    "../imgs/000009.jpg",
    "../imgs/000008.jpg",
    "../imgs/000007.jpg",
    "../imgs/000006.jpg",
    "../imgs/000005.jpg",   
]

face_list2 = []

# Shuffle the items in face_list1
face_list1_shuffle = random.shuffle(face_list1)

# Add the shuffled items to face_list2
face_list2.extend(face_list1_shuffle)
