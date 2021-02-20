#======================================================================
# Github: https://github.com/thjsimmons
#======================================================================

'''
User enters string of form 1 2 b3 4 5 6 b7 
outputs modes of that scale 

Must check to make sure form is correct 
 
'''

def genIntervals(): # Get list of all valid intervals names (bb2, b3, 4, #5, ##6, etc.)
    intervals = []
    mods = ['bb', 'b', '', '#', '##']
    for mod in mods:
        for i in range(1, 8): # 1-12
            intervals.append(mod + str(i))
    return intervals

def split_deg(deg): # split degree string 'b3' into '3', 'b'
    prefix = ''
    for mod in ['bb', 'b', '#', '##']:
        if deg.startswith(mod):
            prefix = mod
            break
    if not prefix:
        return int(deg), prefix
    else:
        return int(deg.split(mod)[1]), prefix

def deg2num(deg): # interval name to semitone
    num, mod = split_deg(deg)
    return ([0, 2, 4, 5, 7, 9, 11][num-1] + ['bb', 'b', '', '#', '##'].index(mod)-2) % 12

def degs2nums(degrees): # interval names to semitones
    return [deg2num(deg) for deg in degrees]

def num2deg(N): # return one the 12 interval names
    return ['1','b2','2','b3','3','4','b5','5','b6','6','b7','7'][N]

def nums2degs(nums): # convert degree names to list of semitones
    return [num2deg(n) for n in nums]

def INPUT_ERROR(degrees): # Check user's input for non-existant intervals
    possible = genIntervals()
    error = False
    for d in degrees:
        if d not in possible:
            error = True
            print "ERROR: ", d, " not in possible intervals"
            break
    return error

def degSort(degrees): # re-order user's scale to ascend in semitones:
    return nums2degs(sorted(degs2nums(degrees)))
    
def permute(degrees): # permute a scale by 1 degree:
    dist = deg2num(degrees[1]) - deg2num(degrees[0])
    return nums2degs((num - dist) % 12 for num in degs2nums(degrees))
     
def getModes(degrees): # get list of the 7 modes from user's scale
    modes = [[] for i in range(len(degrees))]
    modes[0] = degSort(degrees)

    for i in range(1, len(modes)): # repeatedly permute scale by 1 degree
        modes[i] = degSort(permute(modes[i-1]))

    return modes

def main(): # Get user's scale and print its modes:
    print "Enter scale degrees: "
    repeat = True

    while repeat:
        inputStr = raw_input()
        degs = inputStr.rstrip().split(' ')
  
        if not INPUT_ERROR(degs):
            
            sdegs = degSort(degs)
            print "\ndegrees = ", sdegs
            modes = getModes(sdegs)
            print "\n", len(degs), " Modes are: \n"

            count = 1
            for mode in modes:
                print count, ") ", ' '.join(mode)
                count += 1

            repeat = False
    return 0

main()