#Braden Leach
#OCT 28th 2024
#List Starter



#Quiz Scores
scores = [50,97,85,78,30,88]
num_elements = len(scores)
average_score = sum(scores) / num_elements
print(f'The average chemistry score is: {average_score:.2f}%')

#Driving Distance 
distances = [47.2,256,182,193,149]#caddalaic,detroit,lansing,flint,muskegon
    #Min
min_cityname = 'Cadillac'
    #Max
max_cityname = 'Detroit'
    #Average 
num_dis = len(distances)


    #Display
print(f'The shorest round trip driving distance is between Traverse City and {min_cityname}.')
print(f'The lomgest round trip driving distance is between Traverse City and {max_cityname}.')
print(f'''The average round trip driving between Traverse city: 
Cadalaic 
Detroit 
Lansing
Flint 
Muskegon 
is: {sum(distances) / num_dis:.2f} miles''')