# 
#         tokyo
#                   www.fabiocrameri.ch/colourmaps
from matplotlib.colors import LinearSegmentedColormap      
      
cm_data = [[0.10878, 0.055655, 0.20253],      
           [0.11553, 0.057566, 0.20467],      
           [0.12228, 0.059414, 0.20681],      
           [0.12908, 0.060986, 0.20893],      
           [0.1358, 0.062796, 0.2111],      
           [0.14254, 0.064494, 0.21326],      
           [0.14922, 0.066291, 0.21547],      
           [0.15591, 0.068179, 0.21768],      
           [0.16257, 0.07007, 0.21991],      
           [0.16925, 0.072039, 0.22213],      
           [0.17586, 0.074123, 0.22437],      
           [0.18254, 0.076185, 0.22667],      
           [0.18923, 0.078381, 0.22894],      
           [0.1959, 0.080712, 0.23124],      
           [0.20256, 0.083077, 0.23351],      
           [0.20923, 0.08552, 0.23584],      
           [0.2159, 0.088145, 0.23814],      
           [0.22253, 0.090813, 0.24044],      
           [0.22915, 0.093538, 0.24275],      
           [0.23576, 0.096383, 0.24506],      
           [0.24232, 0.099393, 0.24738],      
           [0.24887, 0.10248, 0.24966],      
           [0.25536, 0.10567, 0.25197],      
           [0.26179, 0.10896, 0.25424],      
           [0.26816, 0.11237, 0.25647],      
           [0.27448, 0.11586, 0.25871],      
           [0.28071, 0.11944, 0.26092],      
           [0.28688, 0.12311, 0.26311],      
           [0.29296, 0.12691, 0.26525],      
           [0.29894, 0.13083, 0.26735],      
           [0.30481, 0.1348, 0.26947],      
           [0.31059, 0.13881, 0.27149],      
           [0.31623, 0.14295, 0.27352],      
           [0.32175, 0.14713, 0.27549],      
           [0.32714, 0.15138, 0.2774],      
           [0.33242, 0.15571, 0.27929],      
           [0.33753, 0.16003, 0.28109],      
           [0.34252, 0.16448, 0.28289],      
           [0.34736, 0.16894, 0.2846],      
           [0.35203, 0.17339, 0.28627],      
           [0.35657, 0.17793, 0.2879],      
           [0.36093, 0.1824, 0.28948],      
           [0.36516, 0.18695, 0.291],      
           [0.36923, 0.19148, 0.29245],      
           [0.37313, 0.19603, 0.29386],      
           [0.3769, 0.20053, 0.29521],      
           [0.38049, 0.20506, 0.29652],      
           [0.38393, 0.20955, 0.29776],      
           [0.38721, 0.21403, 0.29897],      
           [0.39035, 0.21847, 0.3001],      
           [0.39334, 0.22287, 0.30119],      
           [0.39618, 0.22723, 0.30223],      
           [0.39888, 0.23156, 0.30323],      
           [0.40145, 0.23582, 0.30418],      
           [0.40388, 0.24002, 0.30509],      
           [0.40618, 0.24418, 0.30596],      
           [0.40835, 0.24832, 0.30676],      
           [0.41042, 0.25236, 0.30752],      
           [0.41236, 0.25633, 0.30826],      
           [0.41418, 0.26026, 0.30897],      
           [0.4159, 0.26413, 0.30963],      
           [0.41753, 0.2679, 0.31025],      
           [0.41905, 0.27164, 0.31085],      
           [0.42049, 0.27532, 0.31139],      
           [0.42183, 0.27892, 0.31191],      
           [0.42311, 0.28246, 0.31242],      
           [0.42431, 0.2859, 0.31291],      
           [0.42544, 0.28932, 0.31337],      
           [0.42649, 0.29265, 0.3138],      
           [0.4275, 0.29592, 0.3142],      
           [0.42843, 0.29915, 0.31459],      
           [0.42931, 0.30228, 0.31496],      
           [0.43015, 0.3054, 0.31532],      
           [0.43094, 0.30842, 0.31566],      
           [0.43169, 0.31139, 0.31599],      
           [0.43239, 0.31431, 0.31629],      
           [0.43305, 0.31719, 0.31658],      
           [0.43368, 0.32001, 0.31686],      
           [0.43428, 0.32277, 0.31713],      
           [0.43487, 0.32547, 0.31739],      
           [0.43542, 0.32815, 0.31764],      
           [0.43594, 0.33076, 0.31788],      
           [0.43644, 0.33336, 0.31811],      
           [0.43692, 0.33588, 0.31834],      
           [0.43739, 0.33837, 0.31855],      
           [0.43783, 0.34084, 0.31877],      
           [0.43826, 0.34327, 0.31897],      
           [0.43867, 0.34564, 0.31917],      
           [0.43908, 0.34801, 0.31937],      
           [0.43947, 0.35034, 0.31957],      
           [0.43986, 0.35263, 0.31976],      
           [0.44024, 0.35491, 0.31994],      
           [0.4406, 0.35715, 0.32013],      
           [0.44096, 0.35936, 0.32031],      
           [0.44132, 0.36157, 0.32049],      
           [0.44168, 0.36375, 0.32066],      
           [0.44203, 0.36592, 0.32083],      
           [0.44237, 0.36807, 0.321],      
           [0.44271, 0.37021, 0.32116],      
           [0.44305, 0.37234, 0.32133],      
           [0.44338, 0.37447, 0.3215],      
           [0.44372, 0.37659, 0.32166],      
           [0.44406, 0.3787, 0.32183],      
           [0.44439, 0.38081, 0.322],      
           [0.44472, 0.38292, 0.32217],      
           [0.44505, 0.38502, 0.32234],      
           [0.44538, 0.38713, 0.32252],      
           [0.44572, 0.38926, 0.32269],      
           [0.44606, 0.39139, 0.32285],      
           [0.44641, 0.39351, 0.32302],      
           [0.44675, 0.39567, 0.32319],      
           [0.4471, 0.39782, 0.32337],      
           [0.44745, 0.39999, 0.32354],      
           [0.4478, 0.40218, 0.32371],      
           [0.44817, 0.40439, 0.32389],      
           [0.44854, 0.40663, 0.32407],      
           [0.44891, 0.40889, 0.32426],      
           [0.44928, 0.41117, 0.32445],      
           [0.44966, 0.41348, 0.32464],      
           [0.45005, 0.41582, 0.32483],      
           [0.45045, 0.41818, 0.32503],      
           [0.45085, 0.42059, 0.32523],      
           [0.45126, 0.42302, 0.32543],      
           [0.45167, 0.42551, 0.32564],      
           [0.4521, 0.42803, 0.32585],      
           [0.45253, 0.43058, 0.32607],      
           [0.45297, 0.43317, 0.32629],      
           [0.45341, 0.43582, 0.32652],      
           [0.45387, 0.43849, 0.32675],      
           [0.45434, 0.44122, 0.32699],      
           [0.45482, 0.444, 0.32723],      
           [0.4553, 0.44682, 0.32748],      
           [0.45579, 0.44968, 0.32773],      
           [0.45629, 0.45261, 0.32799],      
           [0.4568, 0.45557, 0.32826],      
           [0.45733, 0.45858, 0.32854],      
           [0.45786, 0.46165, 0.32882],      
           [0.45841, 0.46477, 0.32911],      
           [0.45897, 0.46794, 0.32941],      
           [0.45953, 0.47117, 0.32971],      
           [0.4601, 0.47444, 0.33002],      
           [0.46069, 0.47776, 0.33034],      
           [0.46129, 0.48114, 0.33066],      
           [0.4619, 0.48457, 0.331],      
           [0.46252, 0.48807, 0.33136],      
           [0.46315, 0.49162, 0.33173],      
           [0.46381, 0.49521, 0.33212],      
           [0.46448, 0.49886, 0.33251],      
           [0.46514, 0.50256, 0.33292],      
           [0.46583, 0.50631, 0.33334],      
           [0.46654, 0.51013, 0.33378],      
           [0.46726, 0.51401, 0.33423],      
           [0.46799, 0.51793, 0.33471],      
           [0.46874, 0.52189, 0.33521],      
           [0.46952, 0.52594, 0.33572],      
           [0.4703, 0.53002, 0.33625],      
           [0.4711, 0.53416, 0.33683],      
           [0.47193, 0.53837, 0.33743],      
           [0.47277, 0.54261, 0.33804],      
           [0.47363, 0.54692, 0.33871],      
           [0.47454, 0.55128, 0.33941],      
           [0.47545, 0.55568, 0.34013],      
           [0.47639, 0.56017, 0.3409],      
           [0.47736, 0.56468, 0.34171],      
           [0.47836, 0.56926, 0.34257],      
           [0.4794, 0.5739, 0.34347],      
           [0.48046, 0.57859, 0.34442],      
           [0.48156, 0.58334, 0.34543],      
           [0.4827, 0.58814, 0.34651],      
           [0.48388, 0.59301, 0.34765],      
           [0.4851, 0.59792, 0.34885],      
           [0.48637, 0.60289, 0.35012],      
           [0.4877, 0.60793, 0.35147],      
           [0.48906, 0.613, 0.35291],      
           [0.4905, 0.61815, 0.35442],      
           [0.49198, 0.62336, 0.35603],      
           [0.49353, 0.62862, 0.35774],      
           [0.49515, 0.63394, 0.35954],      
           [0.49683, 0.63931, 0.36145],      
           [0.4986, 0.64474, 0.36348],      
           [0.50044, 0.65024, 0.36563],      
           [0.50237, 0.65579, 0.3679],      
           [0.5044, 0.6614, 0.3703],      
           [0.5065, 0.66706, 0.37284],      
           [0.50873, 0.67279, 0.37553],      
           [0.51104, 0.67856, 0.37837],      
           [0.51348, 0.6844, 0.38137],      
           [0.51602, 0.69029, 0.38451],      
           [0.5187, 0.69624, 0.38784],      
           [0.5215, 0.70224, 0.39136],      
           [0.52444, 0.7083, 0.39504],      
           [0.52752, 0.7144, 0.3989],      
           [0.53075, 0.72055, 0.40298],      
           [0.53413, 0.72676, 0.40724],      
           [0.53769, 0.73301, 0.41172],      
           [0.54139, 0.7393, 0.41641],      
           [0.54528, 0.74562, 0.4213],      
           [0.54935, 0.75199, 0.42643],      
           [0.55359, 0.7584, 0.43178],      
           [0.55803, 0.76483, 0.43735],      
           [0.56267, 0.77129, 0.44315],      
           [0.5675, 0.77777, 0.44919],      
           [0.57253, 0.78426, 0.45546],      
           [0.57776, 0.79077, 0.46196],      
           [0.58321, 0.79728, 0.4687],      
           [0.58886, 0.80379, 0.47567],      
           [0.59473, 0.8103, 0.48286],      
           [0.6008, 0.81679, 0.49029],      
           [0.60709, 0.82326, 0.49795],      
           [0.61356, 0.82971, 0.5058],      
           [0.62026, 0.83611, 0.51388],      
           [0.62714, 0.84247, 0.52215],      
           [0.63422, 0.84876, 0.53062],      
           [0.64146, 0.855, 0.53926],      
           [0.6489, 0.86115, 0.54808],      
           [0.65649, 0.86722, 0.55705],      
           [0.66423, 0.8732, 0.56615],      
           [0.67211, 0.87908, 0.57537],      
           [0.68011, 0.88484, 0.58471],      
           [0.68823, 0.89047, 0.59412],      
           [0.69644, 0.89597, 0.60362],      
           [0.70472, 0.90132, 0.61314],      
           [0.71306, 0.90653, 0.62271],      
           [0.72144, 0.91157, 0.63229],      
           [0.72986, 0.91645, 0.64185],      
           [0.73827, 0.92115, 0.65139],      
           [0.74667, 0.92569, 0.66086],      
           [0.75505, 0.93004, 0.67029],      
           [0.76337, 0.9342, 0.6796],      
           [0.77164, 0.93818, 0.68883],      
           [0.77983, 0.94197, 0.69792],      
           [0.78792, 0.94557, 0.70689],      
           [0.79591, 0.94898, 0.7157],      
           [0.80378, 0.95221, 0.72434],      
           [0.81153, 0.95526, 0.73282],      
           [0.81912, 0.95813, 0.74111],      
           [0.82658, 0.96082, 0.74921],      
           [0.83388, 0.96335, 0.75712],      
           [0.84101, 0.96571, 0.76482],      
           [0.84797, 0.96792, 0.77231],      
           [0.85476, 0.96997, 0.77959],      
           [0.86137, 0.97189, 0.78667],      
           [0.86782, 0.97366, 0.79353],      
           [0.87407, 0.97531, 0.80018],      
           [0.88016, 0.97684, 0.80663],      
           [0.88607, 0.97825, 0.81287],      
           [0.89181, 0.97957, 0.81892],      
           [0.89739, 0.98078, 0.82478],      
           [0.9028, 0.98191, 0.83047],      
           [0.90807, 0.98295, 0.83598],      
           [0.91319, 0.98393, 0.84133],      
           [0.91818, 0.98484, 0.84654],      
           [0.92305, 0.98569, 0.85161],      
           [0.92781, 0.9865, 0.85657],      
           [0.93248, 0.98726, 0.86143],      
           [0.93707, 0.98799, 0.8662]]      
      
tokyo_map = LinearSegmentedColormap.from_list('tokyo', cm_data)      
# For use of "viscm view"      
test_cm = tokyo_map      
      
if __name__ == "__main__":      
    import matplotlib.pyplot as plt      
    import numpy as np      
      
    try:      
        from viscm import viscm      
        viscm(tokyo_map)      
    except ImportError:      
        print("viscm not found, falling back on simple display")      
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',      
                   cmap=tokyo_map)      
    plt.show()      
