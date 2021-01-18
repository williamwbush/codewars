def longest_slide_down(pyramid):
    #assign each number a value equal to its distance from average list position
    dis_pyramid = []
    for level in pyramid:
        index = -1
        for i in level:
            dis_pyramid_loc = [i, (level.index(i) - sum(list(range(len(level)))) / (len(level)))]
            dis_pyramid.append(dis_pyramid_loc)
            index += 1 
            
    dis_pyramid = sorted(dis_pyramid, reverse=True)
    print(dis_pyramid)
    # for level in dis_pyramid:
    #     adjacent = True
    #     path = []
    #     while adjacent == True:
    #         row = 0
    #         if 

    #find distance from number to average list position and add to dictionary
    
    # distances = {}
    # index = 0 
    # for list in pyramid:
    #     for i in list:
    #         distances[i]

    # for list in pyramid:
    #     list = list.sort(reverse=True)
    










longest_slide_down([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]])

