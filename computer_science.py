from req_builder import Req

TRACKS = {}
TRACKNAMES = [
    'chem',
    'biochem',
    'bio',
    'cheme'
]
TRACK_PRIORITIES = {
    'biochem': 2,
    'chem': 1,
    'bio':3,
    'cheme':4
}


# communications has hard logic, gonna be hard to appraoch
# math is tough cuz it's one of those majors where you have to keep track of units

'''
Chem
'''
TRACKS['chem'] = [ 
    Req(['CHEM31A', 'CHEM31B', 'CHEM31M', 'CHEM33'], 1, True), 
    'CHEM121', 'CHEM131', 'CHEM151', 'CHEM171', 'CS106A', 'MATH19', 'MATH20', 'MATH21', 'MATH51', 
    'PHYSICS41', 'PHYSICS42', 'PHYSICS43', 'PHYSICS44', 
    'CHEM123', 'CHEM124', 'CHEM126', 'CHEM153', 'CHEM173', 'CHEM174', 'CHEM175', 'CHEM176']

'''
Biochem
'''
# TRACKS['biochem'] = [ 
#     Req(['CHEM31A', 'CHEM31B', 'CHEM31M', 'CHEM33'], 1), 
#     'CHEM121', 'CHEM131', 'CHEM151', 'CHEM171', 'CHEM181', 
#     Req(['BIO84', 'BIO82', 'BIO86'], 1),
#     'CS106A', 'MATH19', 'MATH20', 'MATH21', 'MATH51', 
#     'PHYSICS41', 'PHYSICS42', 'PHYSICS43', 'PHYSICS44', 
#     'CHEM123', 'CHEM124', 'CHEM126', 'CHEM185', 'CHEM173', 'CHEM183', 'CHEM184', 'CHEM176']

'''
bio
'''

# TRACKS['bio'] = [Req(['BIO60', 'BIO61', 'BIO62'], 1),
#        Req(['BIO81', 'BIOHOPK81', 'BIOHOPK175H'], 1),
#        'BIO82', 'BIO83', 'BIO84', 'BIO85', 'BIO86',
#        'BIO45', 
#        Req(['BIO46', 'BIO47', 'BIOHOPK47', 'BIOHOPK175H'], 1),
#        Req([Req(['CHEM31A', 'CHEM31B'], 2), 'CHEM31M'], 1),
#        'CHEM33', 'CHEM121', 'MATH19', 'MATH20', 'MATH21', 'MATH51',
#        'CME100',
#        Req([Req(['PHYSICS21', 'PHYSICS22', 'PHYSICS23', 'PHYSICS24'], 4), Req(['PHYSICS41', 'PHYSICS42', 'PHYSICS43'], 4)], 1),
#        Req(['BIO141', 'STATS141', 'BIOHOPK174H', 'STATS60'], 1),
#        Req(['BIO46', 'BIO47', 'BIO168', 'BIO196A', 'BIO199W', 'BIOHOPK47', 'BIOHOPK175H'], 1)]


'''
cheme
'''
# TRACKS['cheme'] = [
#     'MATH19', 'MATH20', 'MATH21',
#     Req(['CME100', Req(['MATH51', 'MATH52'], 1), 1]),
#     Req(['CME102', 'MATH53'], 1),
#     Req(['CME104', 'CME106'], 1),
#     'CHEM31M', 'CHEM33', 'CHEM121',
#     Req(['PHYSICS41', 'PHYSICS41E'], 1),
#     'PHYSICS43', 'CHEMENG100', 'CHEMENG110A', 'CHEMENG110B', 'CHEMENG120A', 'CHEMENG120B', 'CHEMENG130B', 
#     'CHEMENG130A', 'CHEMENG150', 'CHEMENG180', 'CHEMENG181', 'CHEMENG185A', 'CHEMENG185B', 'CHEM171', 'CHEMENG20',
#     Req(['CHEMENG140', 'CHEMENG142', 'CHEMENG160', 'CHEMENG174', 'CHEMENG177', 'CHEMENG183', 'CHEMENG190', 'CHEMENG190H', 'CHEMENG196'], 1),
#     Req(['AA252', 'ARCHLGY151', 'BIOE131', 'CEE102A', Req(['CEE17X', 'CEE177S'], 2), 'CLASSICS168', 'COMM120W', 'COMM166', 'CS152',
#          'CS181', 'CS181W', 'CS182', 'CS182W', 'CS278', 'EARTHSYS125','ENGR117', 'ENGR145', 'ENGR148', 'HUMBIO174', 'MS&E193',
#          'ME167', 'POLISCI114S', 'PUBLPOL134', 'STS1'], 1), # This is TIS
#     Req(['ENGR10', 'ENGR14', 'ENGR15', 'ENGR20', 'ENGR21', 'ENGR40A', 'ENGR40B', 'ENGR40M', 'ENGR42', 'ENGR50', 'ENGR50E', 'ENGR50M',
#          'ENGR60', 'ENGR62', 'ENGR62X', 'ENGR76', 'CS106A', 'CS106B', 'CS106M', 'ENGR80', 'ENGR90'], 1)] # This is ENGR Fund.


'''

'''