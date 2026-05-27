#100 Birds of the World
#The purpose of my program is to help users find a bird that they would like

#Initialize
import pandas as pd   #Used to read the CSV File
import webbrowser     #Used to open bird images in a browser
import random         #Used to randomly choose a bird image

#Load data from CSV file
data = pd.read_csv('100 birds.csv')
#Convert each column into lists
name = data['Name'].tolist()
pri_color = data['Primary Color'].tolist()
diet = data['Diet'].tolist()
#List of bird image URLs
img_bird =["https://www.allaboutbirds.org/guide/assets/photo/63737371-480px.jpg","https://www.allaboutbirds.org/guide/assets/og/75229331-1200px.jpg","https://upload.wikimedia.org/wikipedia/commons/c/cd/Setophaga_ruticilla_-Chiquimula%2C_Guatemala_-male-8-4c.jpg","https://static.wikia.nocookie.net/animals/images/2/2c/IMG_6372.jpg/revision/latest/scale-to-width-down/340?cb=20140808205058","https://media.nationalgeographic.org/assets/photos/000/277/27700.jpg",
           "https://upload.wikimedia.org/wikipedia/commons/1/1a/About_to_Launch_%2826075320352%29.jpg","https://tilandtrust.org/sites/default/files/images/news/belted_kingfisher_s52-13-028_l.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/191086401/320","https://i.pinimg.com/736x/b3/71/e7/b371e7cec9f6762ae1d81a3e43cc3daf.jpg","https://www.allaboutbirds.org/guide/assets/photo/59859171-480px.jpg","https://upload.wikimedia.org/wikipedia/commons/5/56/Chiroxiphia_caudata-2.jpg",
           "https://farm9.staticflickr.com/8806/17074254082_97daffe794_z.jpg","https://i.pinimg.com/originals/bf/06/c9/bf06c92782159121e579866191c6c08e.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/203317581/1800","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/219318871/1800","https://www.allaboutbirds.org/guide/assets/og/75302131-1200px.jpg","https://www.allaboutbirds.org/guide/assets/photo/68122191-480px.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/143000061/900",
           "https://cdn.mos.cms.futurecdn.net/z3iEY8ryHdNzeyvLxyMppT.jpg","https://www.allaboutbirds.org/guide/assets/og/75368221-1200px.jpg","https://www.allaboutbirds.org/guide/assets/photo/300152741-480px.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/45128851/1800","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/70583361/1800","https://www.allaboutbirds.org/guide/assets/og/75340411-1200px.jpg","https://photofeathers.files.wordpress.com/2011/03/img_5056.jpg",
           "https://www.ontarioparks.com/parksblog/wp-content/uploads/2015/10/canstockphoto2749376.jpg","https://www.birdguides-cdn.com/cdn/gallery/birdguides/e4d0baee-75dc-424e-a76f-ecbfda56c1da.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/275821031/1800","https://www.allaboutbirds.org/guide/assets/og/75351601-1200px.jpg","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Emperor_goose_by_Lisa_Hupp_USFWS.jpg/220px-Emperor_goose_by_Lisa_Hupp_USFWS.jpg","https://www.birdsofcolombia.org/world/Flame_Bowerbird_Male.jpg",
           "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/44495661/1800","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/296730461/1800","https://i2.wp.com/www.beyourownbirder.com/wp-content/uploads/2018/05/golden-white-eye.jpg?fit=670%2C300","https://www.birdsville.net.au/wp-content/uploads/2011/07/Gouldian-finch1.jpg","https://avibirds.com/wp-content/uploads/2020/08/great-blue-heron-400x442.jpg","https://i.pinimg.com/originals/62/8b/a5/628ba5fefe540ae3bc80c4b2a81b3a81.jpg",
           "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/191038011/320","https://upload.wikimedia.org/wikipedia/commons/thumb/e/ee/Great_hornbill_Photograph_by_Shantanu_Kuveskar.jpg/330px-Great_hornbill_Photograph_by_Shantanu_Kuveskar.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/244162041/1200","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/140480041/1800","https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Flamant_rose_Salines_de_Thyna.jpg/1200px-Flamant_rose_Salines_de_Thyna.jpg",
           "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3b/Harpia_harpyja_001_800.jpg/330px-Harpia_harpyja_001_800.jpg","https://upload.wikimedia.org/wikipedia/commons/1/1a/Black-necked_Stilt.jpg","https://wildlatitudes.com/wp-content/uploads/Hoatzin_by_Murray-Foubister.jpg","https://www.pbs.org/wnet/nature/files/2014/08/1200468kpo10-1024x682.jpg","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRIvgz4jXeQSVtLJGvrgs-8lwaTVKUXFO-kbw&usqp=CAU","https://olivemacawparrotsfarm.com/wp-content/uploads/2019/11/Laughing-Falcon-Herpetotheres-cachinnans.jpg",
           "https://animals.sandiegozoo.org/sites/default/files/2016-11/animals_hero_kookaburra.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/188555631/1800","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS1CTaVtQcXuxJV6tI0N9ZTbdML_Xep99yWAg&usqp=CAU","https://www.animalspot.net/wp-content/uploads/2014/07/Macaroni-Penguin-Images.jpg","https://upload.wikimedia.org/wikipedia/commons/b/bf/Anas_platyrhynchos_male_female_quadrat.jpg","https://upload.wikimedia.org/wikipedia/commons/b/b7/Mourning_Dove_2006.jpg",
           "https://cdn.download.ams.birds.cornell.edu/api/v1/asset/158687851/1800","https://abcbirds.org/wp-content/uploads/2016/06/Nene_Jack-Jeffrey_PR.jpg","https://www.biorxiv.org/content/biorxiv/early/2020/05/14/2020.05.12.092080/F1.large.jpg","https://i.ytimg.com/vi/gj_q3rpHF6g/maxresdefault.jpg","https://www.allaboutbirds.org/guide/assets/photo/160654851-480px.jpg","https://images.fineartamerica.com/images-medium-large-5/pied-avocet-recurvirostra-avosetta-panoramic-images.jpg",
           "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Pileated_Woodpecker_%289597212081%29%2C_crop.jpg/220px-Pileated_Woodpecker_%289597212081%29%2C_crop.jpg","https://innerstrength.zone/wp-content/uploads/2020/02/3_result_result2.jpg","https://www.allaboutbirds.org/guide/assets/photo/94974451-480px.jpg","https://alchetron.com/cdn/razorbill-0c5144ab-deca-47c2-b7f1-ec251841176-resize-750.jpg","https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Buphagus_erythrorhynchus00.jpg/330px-Buphagus_erythrorhynchus00.jpg",
           "https://nas-national-prod.s3.amazonaws.com/styles/article_teaser/s3/editorial-card-images/article/ed-card_apa_2013_28356_226452_megumiaita_redbreasted_nuthatch_kk.jpg?itok=0jjmRsgs","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/171755111/1800","https://i.pinimg.com/originals/1e/14/1e/1e141e9b56b19a76b72dab5db07d2716.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/173557351/1800","https://www.allaboutbirds.org/guide/assets/photo/71316071-480px.jpg",
           "https://upload.wikimedia.org/wikipedia/commons/thumb/5/56/Paloma_brav%C3%ADa_%28Columba_livia%29%2C_Palacio_de_Nymphenburg%2C_M%C3%BAnich%2C_Alemania01.JPG/330px-Paloma_brav%C3%ADa_%28Columba_livia%29%2C_Palacio_de_Nymphenburg%2C_M%C3%BAnich%2C_Alemania01.JPG","https://nas-national-prod.s3.amazonaws.com/styles/hero_cover_bird_page/s3/a1_5380_8_roseate-spoonbill_andrew_mccullough_adult.jpg?itok=sulRVtJC","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/193674311/320","https://cdn.birdwatchingdaily.com/2013/06/Kinglet-Ruby-crowned-10-0089-660x440.jpg",
           "https://i.pinimg.com/originals/7d/23/79/7d2379ac656c56ec5e31c67672b2ceb0.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/221182651/1800","https://www.allaboutbirds.org/guide/assets/photo/67449631-480px.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/220892221/1800","https://upload.wikimedia.org/wikipedia/commons/thumb/c/c9/Accipiter_striatus%2C_Canet_Road%2C_San_Luis_Obispo_1.jpg/330px-Accipiter_striatus%2C_Canet_Road%2C_San_Luis_Obispo_1.jpg",
           "https://upload.wikimedia.org/wikipedia/commons/c/c0/Balaeniceps_rex.jpg","https://cdn.download.ams.birds.cornell.edu/api/v1/asset/243730471/1800","https://galapagosconservation.org.uk/wp-content/uploads/2018/12/Smooth-billed-Ani-Crotophaga-ani-Divine-Farm-29-1-2010-2-small-1000x667.jpg","https://upload.wikimedia.org/wikipedia/commons/2/28/Schneckenweih-Snail-Kite.JPG","https://www.treehugger.com/thmb/rYPDZsLevHn5WBs-XuwMdi6BLuk=/4192x3144/smart/filters:no_upscale()/__opt__aboutcom__coeus__resources__content_migration__mnn__images__2020__01__snowy_owl_flying-cdff0730fab6435d8d0e1edffda3ca21.jpg",
           "https://i.ytimg.com/vi/H26Tl7e3KeU/maxresdefault.jpg","https://www.allaboutbirds.org/news/wp-content/uploads/2018/06/14-Vogelkop_sing_Tim_Laman_ML_Feature-1.jpg","https://upload.wikimedia.org/wikipedia/commons/6/68/Tawny_Frogmouth_-_Sydney_Olympic_Park.jpg","https://www.animalspot.net/wp-content/uploads/2016/02/Toco-Toucans.jpg","https://www.allaboutbirds.org/guide/assets/og/81386391-1200px.jpg","https://upload.wikimedia.org/wikipedia/commons/e/e5/Tufted_Puffin_Alaska_%28cropped%29.jpg",
           "https://img.theepochtimes.com/assets/uploads/2020/05/18/Victoria-Crowned-Pigeon-i.jpg","https://i.pinimg.com/736x/dd/42/54/dd425491e9c313330e407d4c7894edb6.jpg","https://www.purelypoultry.com/images/vulturine-guineafowl_04.jpg","https://www.shanghaibirding.com/wp-content/uploads/2020/02/white-wagtail-ocularis.jpg","https://cdn.birdwatchingdaily.com/2019/09/Whooping-Crane-Aransas-NWR_8109-Welty.jpg","https://i.ytimg.com/vi/BvIuUABZkiI/maxresdefault.jpg",
           "https://bloximages.newyork1.vip.townnews.com/yakimaherald.com/content/tncms/assets/v3/editorial/3/03/303e8cea-73fa-11e6-841c-cfeef8ca8b2d/57ce60c1369f6.image.jpg?crop=1662%2C935%2C0%2C155&resize=1662%2C935&order=crop%2Cresize","https://www.allaboutbirds.org/guide/assets/photo/65051941-480px.jpg"]

filter_birds=[]      #Empty list to store filtered bird results

#Functions

#Function to find birds based on diet
def eat(food):
    filter_birds.clear()
    for i in range(len(diet)):
        if food.lower() in diet[i].lower():#Returns a new string with all uppercase characters converted to lowercase  #Check if food matches diet
            filter_birds.append(i)            #Store index of matching bird
    #If matches were found they will be printed out
    if len(filter_birds) > 0:
        print("Here are some birds that eat", food, ":")
        for i in filter_birds:
            print(name[i], "-", diet[i])
    else:
        print("Sorry, No birds found with that diet.")

#Function to show bird images
def look():
    pic = input("Would you like to see an image of a specific bird listed (yes or no): ")
    if pic.lower() == "yes":
        bird =input("What bird would you like to see?: ")
        for i in range(len(name)):
            if bird.lower() in name[i].lower():   #Search for bird name
                webbrowser.open(img_bird[i])      #Open its image
    elif pic.lower() == "no":
        lucky_pic = random.choice(img_bird)       #Opens a random image
        webbrowser.open(lucky_pic)
        print(f"This is the image of the bird selected for you: {lucky_pic}")
    else:
       print("Invalid response!")




#Function to find birds based on color

def colors(the_color):
    found = False          #Keeps track if any match is found
    for i in range(len(pri_color)):
        if the_color.lower() in pri_color[i].lower():     #Check color match
            print(name[i], "-", pri_color[i])
            found = True
    if not found:
        print("Invalid Response. Please try again!")







#Main menu function that runs the program
def together():
   print("""
                                                                                                                                                                                                                                                                            Welcome! You are going to be able to see birds from all around the world!
   But first you are going to answer some questions
   so you are able to see the bird that you would like the most!
          """)
   print("These are the options you could choose from to see different birds: ")
   while True:     #Keeps the program running until user exits
       print("1) Food that birds eat")
       print("2) Find the color of the bird")
       print("3) See an image of a bird")
       print("4) Exit")
       choice=input("Make your choice (1-4): ")
       print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
       if choice == "1":
            ask= input("What food would you like the bird to eat? (e.g., seeds,squid,fish,insects): ")
            eat(ask)             #Call eat function
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Here are the options again so you can pick something else!:")
       elif choice == "2":
            user_color=input("""
    There are so many options when it comes to choosing a bird
    here are the colors of birds that are available for you to pick!
    (pink, blue, black, yellow, white, grey, brown, green, red)
your pick: """)
            colors(user_color)    #Call colors function
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Here are the options again so you can pick something else!:")
       elif choice == "3":
            look()                #Call look function
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Here are the options again so you can pick something else!:")
       elif choice == "4":
           print("""
        I hope you found a bird you liked
        if not, I hope you learned something new!
        Goodbye!
           """)
           break                  #Exit the loop/program
       else:
           print("That is an invalid response. Make sure your choice aligns with the options given:")

#Main
together()

#Data Source Information:
#100 birds dataset
#Website Name: Code.org
#URL: https://code.org/en-US
#Dataset Source: https://www.birds.cornell.edu/home/

#Source Information:
#Website Name:bird.cornell.edu
#URL: https://www.birds.cornell.edu/
#Organization group:Cornell Lab
#Article Name: CornellLab
#Date: January 15, 2015

