


places=[['air', '1000', '960', '560', '4%'],
        ['area51', '750', '450', '-3550', '40%'],
        ['attic', '450', '439', '189','2.5%'],
        ['bank', '600','360', '-3640', '40%'],
        ['bed', '175', '172', '-29', '2%'],
        ['bus', '150', '150', '150', '0%'],
        ['bushes', '425', '419', '269', '1.5%'],
        ['car', '0', '0', '0', '100%'],
        ['coat', '375', '375', '375', '0%'],
        ['couch', '325', '322', '222', '1%'],
        ['discord', '250', '245', '45', '2%'],
        ['dog', '500', '480', '80', '4%'],
        ['dresser', '375', '375', '375', '0%'],
        ['dumpster', '250', '238', '-263', '5%'],
        ['glovebox', '400', '396', '296', '1%'],
        ['grass', '200', '200', '200', '0%'],
        ['hospital', '500', '425', '-1075', '15%'],
        ['laundromat', '175', '175', '175', '0%'],
        ['mailbox', '250', '250', '250', '0%'],
        ['pantry', '250', '250', '250', '0%'],
        ['pocket', '125', '125', '125', '0%'],
        ['purse', '750', '450', '-3550', '40%'],
        ['sewer', '600', '510', '-990', '15%'],
        ['shoe', '250', '250', '250', '0%'],
        ['sink', '50', '50', '50', '0%'],
        ['street', '375', '350', '-317', '7%'],
        ['tree', '550', '528', '128', '4%'],
        ['uber', '485', '478', '328', '1.5%']]
# The places variable holds
# places[index][0] is the name
# places[index][1] is the coins per success
# places[index][2] is the average coins
# places[index][3] is the average net gain
# places[index][4] is the death rate
def get_int(string):
    """get_int parses the information in 'places'. """
    death_rate=""
    nums=["-",0,1,2,3,4,5,6,7,8,9]
    for x in range(len(nums)):
        nums[x]=str(nums[x])

    for i in string:
        if i in nums:
            death_rate+=i
    death_rate=int(death_rate)

    return death_rate
def judgement_formula(name1,name2,name3,net_gain_or_death="net gain"):
    """This function takes 3 potential places that can be searched. It considers the statistics for all 3 places.
    Depending on the priority the user_to_rob has specified under variable 'net_gain_or_death', a place to search is
    returned."""
    from random import choice
    global places
    name1.replace(" ","")
    name2.replace(" ", "")
    name3.replace(" ", "")
    nl1 = 0
    nl2 = 0
    nl3 = 0

    for i in places:
        if i[0]==name1:
            nl1=i

        elif i[0]==name2:
            nl2=i

        elif i[0]==name3:
            nl3=i
    net_gain1=0
    net_gain2=0
    net_gain3=0

    if "net gain" in net_gain_or_death:
        if nl1!=0:
            net_gain1=get_int(nl1[3])

        if nl2 != 0 :
            net_gain2 = get_int(nl2[3])

        if nl3 != 0:
            net_gain3 = get_int(nl3[3])
    else:
        if nl1 != 0:
            net_gain1 = get_int(nl1[4])

        if nl2 != 0:
            net_gain2 = get_int(nl2[4])

        if nl3 != 0:
            net_gain3 = get_int(nl3[4])

    main=[]
    if nl1!=0:
        main.append(net_gain1)

    if nl2!=0:
        main.append(net_gain2)

    if nl3!=0:
        main.append(net_gain3)

    if len(main)==0:
        return(choice([name1,name2,name3]))

    main.sort()

    if net_gain_or_death=="net gain":
        index=-1
    elif "death" in net_gain_or_death:
        index=0

    else:
        index=-1


    if "ultra death" in net_gain_or_death and main[index]>0:
        return ""

    if main[index]==net_gain1:
        return(name1)

    if main[index]==net_gain2:
        return(name2)

    if main[index]==net_gain3:
        return(name3)


    # if main[0]==net_gain1:
    #     p1+=1
    # if main[0]==net_gain2:
    #     p1+=1
    # if main[0]==net_gain3:
    #     p1+=1
    else:
        #If none of the logical priorities is specified, just choose a random place to search
        return (choice([name1, name2, name3]))


