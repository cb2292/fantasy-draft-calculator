'''Created on Aug 14, 2013 by Chris Bruce'''

import os
from operator import attrgetter
import math
import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'])

'''league point settings, to be input by user'''
pass_yd_pp = 25   #pass yards per point
pp_pass_TD = 4    #points per passing touchdown
rush_yd_pp = 10
pp_rush_TD = 6
rec_yd_pp = 10
pp_rec_TD = 6
ppr = 0.5
pp_INT = -2
pp_fum = -2
pp_made_FG = 3
pp_missed_FG = 0
pp_made_XP = 1
pp_missed_XP = 0
DEFpp_INT = 2
DEFpp_ff = 0
DEFpp_fr = 2
DEFpp_sack = 1
DEFpp_TD = 6
DEFpp_safety = 2
DEFpa_0 = 10
DEFpa_lt_7 = 7
DEFpa_lt_14 = 4
DEFpa_lt_21 = 1
DEFpa_lt_28 = 0
DEFpa_lt_35 = -1
DEFpa_gt_35 = -4

'''League roster settings, to be input by user'''
starting_QBs = 1
starting_RBs = 2
starting_WRs = 3
starting_TEs = 1
starting_Ks = 1
starting_DEFSTs = 1
starting_WR_RB = 0
starting_WR_TE = 0
starting_WR_RB_TE = 0
bench_spots = 8
teams = 12
payroll = 300
min_salary = 1

'''initialize values to be used later'''
bench_QBs = 1
bench_RBs = 3
bench_WRs = 3
bench_TEs = 1
bench_Ks = 0
bench_DEFSTs = 0
total_starters = starting_QBs + starting_RBs + starting_WRs + starting_TEs + starting_Ks + starting_DEFSTs
total_players = starting_QBs + starting_RBs + starting_WRs + starting_TEs + starting_Ks + starting_DEFSTs + bench_spots
starter_player_percent = float(total_starters) / float(total_players)
total_dollars = teams * payroll
total_AR_dollars = total_dollars - min_salary * total_players * teams
starter_AR_dollars = (starter_player_percent + (1-starter_player_percent) * 2/3) * total_AR_dollars
bench_AR_dollars = total_AR_dollars - starter_AR_dollars

class Index(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('pages/index.html')
        self.response.write(template.render())

    def post(self):
        global pass_yd_pp,pp_pass_TD,rush_yd_pp,pp_rush_TD,rec_yd_pp,pp_rec_TD,ppr,pp_INT,pp_fum,pp_made_FG,pp_missed_FG,pp_made_XP,pp_missed_XP,DEFpp_INT,DEFpp_ff,DEFpp_fr,DEFpp_sack,DEFpp_TD,DEFpp_safety,DEFpa_0,DEFpa_lt_7,DEFpa_lt_14,DEFpa_lt_21,DEFpa_lt_28,DEFpa_lt_35,DEFpa_gt_35,starting_QBs,starting_RBs,starting_WRs,starting_TEs,starting_Ks,starting_DEFSTs,starting_WR_RB,starting_WR_TE,starting_WR_RB_TE,bench_spots,teams,payroll,min_salary
        reset_values()
        results = []
        '''set values to user input from web page'''
        pass_yd_pp = float(self.request.get('pass_yd_pp'))
        pp_pass_TD = float(self.request.get('pp_pass_TD'))
        rush_yd_pp = float(self.request.get('rush_yd_pp'))
        pp_rush_TD = float(self.request.get('pp_rush_TD'))
        rec_yd_pp = float(self.request.get('rec_yd_pp'))
        pp_rec_TD = float(self.request.get('pp_rec_TD'))
        ppr = float(self.request.get('ppr'))
        pp_INT = float(self.request.get('pp_INT'))
        pp_fum = float(self.request.get('pp_fum'))
        pp_made_FG = float(self.request.get('pp_made_FG'))
        pp_missed_FG = float(self.request.get('pp_missed_FG'))
        pp_made_XP = float(self.request.get('pp_made_XP'))
        pp_missed_XP = float(self.request.get('pp_missed_XP'))
        DEFpp_INT = float(self.request.get('DEFpp_INT'))
        DEFpp_ff = float(self.request.get('DEFpp_ff'))
        DEFpp_fr = float(self.request.get('DEFpp_fr'))
        DEFpp_sack = float(self.request.get('DEFpp_sack'))
        DEFpp_TD = float(self.request.get('DEFpp_TD'))
        DEFpp_safety = float(self.request.get('DEFpp_safety'))
        DEFpa_0 = float(self.request.get('DEFpa_0'))
        DEFpa_lt_7 = float(self.request.get('DEFpa_lt_7'))
        DEFpa_lt_14 = float(self.request.get('DEFpa_lt_14'))
        DEFpa_lt_21 = float(self.request.get('DEFpa_lt_21'))
        DEFpa_lt_28 = float(self.request.get('DEFpa_lt_28'))
        DEFpa_lt_35 = float(self.request.get('DEFpa_lt_35'))
        DEFpa_gt_35 = float(self.request.get('DEFpa_gt_35'))
        starting_QBs = int(self.request.get('starting_QBs'))
        starting_RBs = int(self.request.get('starting_RBs'))
        starting_WRs = int(self.request.get('starting_WRs'))
        starting_TEs = int(self.request.get('starting_TEs'))
        starting_Ks = int(self.request.get('starting_Ks'))
        starting_DEFSTs = int(self.request.get('starting_DEFSTs'))
        starting_WR_RB = int(self.request.get('starting_WR_RB'))
        starting_WR_TE = int(self.request.get('starting_WR_TE'))
        starting_WR_RB_TE = int(self.request.get('starting_WR_RB_TE'))
        bench_spots = int(self.request.get('bench_spots'))
        teams = int(self.request.get('teams'))
        payroll = float(self.request.get('payroll'))
        min_salary = float(self.request.get('min_salary'))
        '''run code to make calculations'''
        adjust_settings()
        import_player_projections("QB-proj-2019.csv","RB-proj-2019.csv","WR-proj-2019.csv","TE-proj-2019.csv","K-proj-2019.csv","DEFST-proj-2019.csv")
        sort_position_lists()
        set_replacement_levels()
        AR_levels()
        calculate_dollar_values()
        sort_final_values()
        results = all_players
        print "all players:" + str(len(all_players))
        print "QB_RL "+str(QB_RL),"RB_RL "+str(RB_RL),"WR_RL "+str(WR_RL),"TE_RL "+str(TE_RL),"K_RL "+str(K_RL),"DEFST "+str(DEFST_RL)
        print total_starter_PAR, total_bench_PAR, starter_AR_dollars, bench_AR_dollars, tda
        print starting_QBs, bench_QBs
        for i in range(0,len(all_players)-1):
            if all_players[i].position == "QB":
                print all_players[i].position,all_players[i].name,all_players[i].fantasy_pts,all_players[i].dollar_value,all_players[i].starter,all_players[i].bench
        template_values = {
            'results': results,
        }
        template = JINJA_ENVIRONMENT.get_template('pages/results.html')
        self.response.write(template.render(template_values))

class FAQ(webapp2.RequestHandler):
    def get(self):
        template = JINJA_ENVIRONMENT.get_template('pages/faq.html')
        self.response.write(template.render())

application = webapp2.WSGIApplication([
    ('/', Index),
    ('/index', Index),
    ('index.html', Index),
    ('/faq', FAQ),
    ('/FAQ', FAQ),
], debug=True)

def adjust_settings():
    global starting_WRs,starting_RBs,starting_TEs,bench_QBs,bench_RBs,bench_WRs,bench_TEs,bench_Ks,bench_DEFSTs
    global total_starters,total_players,starter_player_percent,total_dollars,total_AR_dollars,starter_AR_dollars,bench_AR_dollars
    #adjust for flex positions
    starting_WRs = starting_WRs + starting_WR_RB / 2 + starting_WR_TE * 2/3 + starting_WR_RB_TE * 1/3
    starting_RBs = starting_RBs + starting_WR_RB / 2 + starting_WR_RB_TE * 1/3
    starting_TEs = starting_TEs + starting_WR_TE * 1/3 + starting_WR_RB_TE * 1/3

    #calculate position of bench spots, arbitrary guess on proportions
    bench_QBs = bench_spots * 0.15
    bench_RBs = bench_spots * 0.35
    bench_WRs = bench_spots * 0.45
    bench_TEs = bench_spots * 0.05
    bench_Ks = bench_spots * 0
    bench_DEFSTs = bench_spots * 0

    #calculate available dollars for auction
    total_starters = starting_QBs + starting_RBs + starting_WRs + starting_TEs + starting_Ks + starting_DEFSTs
    total_players = starting_QBs + starting_RBs + starting_WRs + starting_TEs + starting_Ks + starting_DEFSTs + bench_spots
    starter_player_percent = float(total_starters) / float(total_players)
    total_dollars = teams * payroll
    total_AR_dollars = total_dollars - min_salary * total_players * teams
    #allocate majority of dollars to starters, scaled by the proportion of roster they take up
    starter_AR_dollars = (starter_player_percent + (1-starter_player_percent) * 3/4) * total_AR_dollars
    bench_AR_dollars = total_AR_dollars - starter_AR_dollars
    print "adjust settings has been run"

'''create classes to hold stats for each player;
   different positions get different objects since they have different stats'''

class Player(object):
    fantasy_pts = 0
    PAR = 0 #points above replacement, placeholder
    dollar_value = 0
    starter = False
    bench = False
    '''makes a player object - will be inherited by player types'''
    def __init__(self,position,name):
        self.position = position
        self.name = name

    def assign_PAR(self):
        if self.position == "QB":
            self.PAR = ( self.fantasy_pts - QB_RL ) * 1
        elif self.position == "RB":
            self.PAR = ( self.fantasy_pts - RB_RL ) * 1
        elif self.position == "WR":
            self.PAR = ( self.fantasy_pts - WR_RL ) * 0.9
        elif self.position == "TE":
            self.PAR = ( self.fantasy_pts - TE_RL ) * 0.9
        elif self.position == "K":
            self.PAR = ( self.fantasy_pts - K_RL ) * 0.2
        elif self.position == "DEF/ST":
            self.PAR = ( self.fantasy_pts - DEFST_RL ) * 0.4
        else:
            print("Error in assigning PAR")

    def assign_dollar_value(self):
        if self.starter:
            self.dollar_value = int( self.PAR / total_starter_PAR * starter_AR_dollars + min_salary )
        elif self.bench:
            self.dollar_value = int( self.PAR / total_bench_PAR * bench_AR_dollars + min_salary )
        else:
            self.dollar_value = int( self.PAR / total_bench_PAR * bench_AR_dollars + min_salary )

class QB(Player):
    '''makes a QB object to hold stats'''
    def __init__(self,name,pass_yds,pass_TD,INTs,rush_yds,rush_TD,fumbles):
        self.name = name
        self.position = "QB"
        self.pass_yds = pass_yds
        self.pass_TD = pass_TD
        self.INTs = INTs
        self.rush_yds = rush_yds
        self.rush_TD = rush_TD
        self.fumbles = fumbles
        self.fantasy_pts = round(self.pass_yds/pass_yd_pp + self.pass_TD*pp_pass_TD + self.INTs*pp_INT + self.rush_yds/rush_yd_pp + self.rush_TD*pp_rush_TD + self.fumbles*pp_fum,2)

class RB(Player):
    '''makes a RB object to hold stats'''
    def __init__(self,name,rush_yds,rush_TD,rec,rec_yds,rec_TD,fumbles):
        self.name = name
        self.position = "RB"
        self.rec_yds = rec_yds
        self.rec_TD = rec_TD
        self.rec = rec
        self.rush_yds = rush_yds
        self.rush_TD = rush_TD
        self.fumbles = fumbles
        self.fantasy_pts = round(self.rec_yds/rec_yd_pp + self.rec_TD*pp_rec_TD + self.rec*ppr + self.rush_yds/rush_yd_pp + self.rush_TD*pp_rush_TD + self.fumbles*pp_fum,2)

class WR(Player):
    '''makes a WR object to hold stats'''
    def __init__(self,name,rec,rec_yds,rec_TD,fumbles):
        self.name = name
        self.position = "WR"
        self.rec_yds = rec_yds
        self.rec_TD = rec_TD
        self.rec = rec
        self.fumbles = fumbles
        self.fantasy_pts = round(self.rec_yds/rec_yd_pp + self.rec_TD*pp_rec_TD + self.rec*ppr + self.fumbles*pp_fum,2)

class TE(Player):
    '''makes a TE object to hold stats'''
    def __init__(self,name,rec,rec_yds,rec_TD,fumbles):
        self.name = name
        self.position = "TE"
        self.rec_yds = rec_yds
        self.rec_TD = rec_TD
        self.rec = rec
        self.fumbles = fumbles
        self.fantasy_pts = round(self.rec_yds/rec_yd_pp + self.rec_TD*pp_rec_TD + self.rec*ppr + self.fumbles*pp_fum,2)

class K(Player):
    '''makes a K object to hold stats'''
    def __init__(self,name,made_FG,FGA,made_XP,XPA):
        self.name = name
        self.position = "K"
        self.made_FG = made_FG
        self.missed_FG = FGA - made_FG
        self.made_XP = made_XP
        self.missed_XP = XPA - made_XP
        self.fantasy_pts = round(self.made_FG*pp_made_FG + self.missed_FG*pp_missed_FG + self.made_XP*pp_made_XP + self.missed_XP*pp_missed_XP,2)

class DEFST(Player):
    '''makes a DEF/ST object to hold stats'''
    def __init__(self,name,INTs,FR,FF,sacks,TDs,safeties,PA):
        self.name = name
        self.position = "DEF/ST"
        self.FR = FR
        self.FF = FF
        self.INTs = INTs
        self.sacks = sacks
        self.TDs = TDs
        self.safeties = safeties
        if PA / 16 <= 0:
            self.PA = DEFpa_0
        elif PA / 16 <= 7:
            self.PA = DEFpa_lt_7
        elif PA / 16 <= 14:
            self.PA = DEFpa_lt_14
        elif PA / 16 <= 21:
            self.PA = DEFpa_lt_21
        elif PA / 16 <= 28:
            self.PA = DEFpa_lt_28
        elif PA / 16 <= 35:
            self.PA = DEFpa_lt_35
        else:
            self.PA = DEFpa_gt_35
        self.fantasy_pts = round(self.INTs*DEFpp_INT + self.FR*DEFpp_fr + self.FF*DEFpp_ff + self.sacks*DEFpp_sack + self.TDs*DEFpp_TD + self.safeties*DEFpp_safety + self.PA*16,2)

'''import projected stats from .csv files and calculate
   fantasy points for each player/object'''

# initialize variables that use player objects
QBs = []
RBs = []
WRs = []
TEs = []
Ks = []
DEFSTs = []
all_players = []
QB_RL = 0
RB_RL = 0
WR_RL = 0
TE_RL = 0
K_RL = 0
DEFST_RL = 0
total_starter_PAR = 0
total_bench_PAR = 0
tda = 0 #total dollars assigned

def import_player_projections(QB_data,RB_data,WR_data,TE_data,K_data,DEFST_data):
    '''get QB projections into QB objects'''
    with open(QB_data,'r') as f:
        for line in f:
            stats = line.split(",")
            if stats[0] == "Player":
                print("Skipping first line in QB datasheet")
            else: #def __init__(self,name,pass_yds,pass_TD,INTs,rush_yds,rush_TD,fumbles):
                QBs.append(QB(stats[0],float(stats[4]),float(stats[5]),float(stats[6]),float(stats[10]),float(stats[12]),float(stats[13])))

    '''get RB projections into RB objects'''
    with open(RB_data,'r') as f:
        for line in f:
            stats = line.split(",")
            if stats[0] == "Player":
                print("Skipping first line in RB datasheet")
            else: #def __init__(self,name,rush_yds,rush_TD,rec,rec_yds,rec_TD,fumbles):
                RBs.append(RB(stats[0],float(stats[3]),float(stats[5]),float(stats[6]),float(stats[7]),float(stats[9]),float(stats[10])))

    '''get WR projections into WR objects'''
    with open(WR_data,'r') as f:
        for line in f:
            stats = line.split(",")
            if stats[0] == "Player":
                print("Skipping first line in WR datasheet")
            else: #def __init__(self,name,rec,rec_yds,rec_TD,fumbles):
                WRs.append(WR(stats[0],float(stats[2]),float(stats[3]),float(stats[5]),float(stats[6])))

    '''get TE projections into TE objects'''
    with open(TE_data,'r') as f:
        for line in f:
            stats = line.split(",")
            if stats[0] == "Player":
                print("Skipping first line in TE datasheet")
            else: #def __init__(self,name,rec,rec_yds,rec_TD,fumbles):
                TEs.append(TE(stats[0],float(stats[2]),float(stats[3]),float(stats[5]),float(stats[6])))

    '''get K projections into K objects'''
    with open(K_data,'r') as f:
        for line in f:
            stats = line.split(",")
            if stats[0] == "Player":
                print("Skipping first line in K datasheet")
            else: #def __init__(self,name,made_FG,FGA,made_XP,XPA):
                Ks.append(K(stats[0],float(stats[2]),float(stats[3]),float(stats[4]),float(stats[4])*1.02)) # assume 2% of XPA missed

    '''get DEF/ST projections into DEFST objects'''
    with open(DEFST_data,'r') as f:
        for line in f:
            stats = line.split(",")
            if stats[0] == "Player":
                print("Skipping first line in DEF/ST datasheet")
            else: #def __init__(self,name,INTs,FR,FF,sacks,TDs,safeties,PA):
                DEFSTs.append(DEFST(stats[0],float(stats[2]),float(stats[3]),float(stats[4]),float(stats[5]),float(stats[6]),float(stats[7]),float(stats[8])))
    print "players projections have been imported"

def sort_position_lists():
    ''' sort position lists by descending fantasy points (rank)'''
    global QBs,RBs,WRs,TEs,Ks,DEFSTs
    QBs = sorted(QBs, key=attrgetter('fantasy_pts'), reverse=True)
    RBs = sorted(RBs, key=attrgetter('fantasy_pts'), reverse=True)
    WRs = sorted(WRs, key=attrgetter('fantasy_pts'), reverse=True)
    TEs = sorted(TEs, key=attrgetter('fantasy_pts'), reverse=True)
    Ks = sorted(Ks, key=attrgetter('fantasy_pts'), reverse=True)
    DEFSTs = sorted(DEFSTs, key=attrgetter('fantasy_pts'), reverse=True)
    print "sort position lists has been run"

def set_replacement_levels():
    '''get replacement level for each position, in fantasy points'''
    global QB_RL,RB_RL,WR_RL,TE_RL,K_RL,DEFST_RL
    QB_RL = QBs[int(math.ceil((starting_QBs + bench_QBs) * teams))].fantasy_pts
    RB_RL = RBs[int(math.ceil((starting_RBs + bench_RBs) * teams))].fantasy_pts
    WR_RL = WRs[int(math.ceil((starting_WRs + bench_WRs) * teams))].fantasy_pts
    TE_RL = TEs[int(math.ceil((starting_TEs + bench_TEs) * teams))].fantasy_pts
    K_RL = Ks[int(math.ceil((starting_Ks + bench_Ks) * teams))].fantasy_pts
    DEFST_RL = DEFSTs[int(math.ceil((starting_DEFSTs + bench_DEFSTs) * teams))].fantasy_pts
    print "set replacement levels has been run"
def AR_levels():
    '''assign value above replacement for each player, assign starter and bench labels
       and total PAR for starters and bench'''
    global total_starter_PAR,total_bench_PAR
    for x in range(0,len(QBs)-1):
        QBs[x].assign_PAR()
        if x < (starting_QBs * teams):
            total_starter_PAR += QBs[x].PAR
            QBs[x].starter = True
        elif x < ((starting_QBs + bench_QBs) * teams):
            total_bench_PAR += QBs[x].PAR
            QBs[x].bench = True
    for x in range(0,len(RBs)-1):
        RBs[x].assign_PAR()
        if x < (starting_RBs * teams):
            total_starter_PAR += RBs[x].PAR
            RBs[x].starter = True
        elif x < ((starting_RBs + bench_RBs) * teams):
            total_bench_PAR += RBs[x].PAR
            RBs[x].bench = True
    for x in range(0,len(WRs)-1):
        WRs[x].assign_PAR()
        if x < (starting_WRs * teams):
            total_starter_PAR += WRs[x].PAR
            WRs[x].starter = True
        elif x < ((starting_WRs + bench_WRs) * teams):
            total_bench_PAR += WRs[x].PAR
            WRs[x].bench = True
    for x in range(0,len(TEs)-1):
        TEs[x].assign_PAR()
        if x < (starting_TEs * teams):
            total_starter_PAR += TEs[x].PAR
            TEs[x].starter = True
        elif x < ((starting_TEs + bench_TEs) * teams):
            total_bench_PAR += TEs[x].PAR
            TEs[x].bench = True
    for x in range(0,len(Ks)-1):
        Ks[x].assign_PAR()
        if x < (starting_Ks * teams):
            total_starter_PAR += Ks[x].PAR
            Ks[x].starter = True
        elif x < ((starting_Ks + bench_Ks) * teams):
            total_bench_PAR += Ks[x].PAR
            Ks[x].bench = True
    for x in range(0,len(DEFSTs)-1):
        DEFSTs[x].assign_PAR()
        if x < (starting_DEFSTs * teams):
            total_starter_PAR += DEFSTs[x].PAR
            DEFSTs[x].starter = True
        elif x < ((starting_DEFSTs + bench_DEFSTs) * teams):
            total_bench_PAR += DEFSTs[x].PAR
            DEFSTs[x].bench = True
    print "AR levels has been run"

def calculate_dollar_values():
    '''calculate dollar value, total dollar value for check'''
    global tda
    for x in range(0,len(QBs)-1):
        QBs[x].assign_dollar_value()
        if QBs[x].dollar_value > 0:
            tda += QBs[x].dollar_value
    for x in range(0,len(RBs)-1):
        RBs[x].assign_dollar_value()
        if RBs[x].dollar_value > 0:
            tda += RBs[x].dollar_value
    for x in range(0,len(WRs)-1):
        WRs[x].assign_dollar_value()
        if WRs[x].dollar_value > 0:
            tda += WRs[x].dollar_value
    for x in range(0,len(TEs)-1):
        TEs[x].assign_dollar_value()
        if TEs[x].dollar_value > 0:
            tda += TEs[x].dollar_value
    for x in range(0,len(Ks)-1):
        Ks[x].assign_dollar_value()
        if Ks[x].dollar_value > 0:
            tda += Ks[x].dollar_value
    for x in range(0,len(DEFSTs)-1):
        DEFSTs[x].assign_dollar_value()
        if DEFSTs[x].dollar_value > 0:
            tda += DEFSTs[x].dollar_value
    print "calculate dollar values has been run"

def sort_final_values():
    global all_players
    for x in range(0,len(QBs)-1):
        all_players.append(QBs[x])
    for x in range(0,len(RBs)-1):
        all_players.append(RBs[x])
    for x in range(0,len(WRs)-1):
        all_players.append(WRs[x])
    for x in range(0,len(TEs)-1):
        all_players.append(TEs[x])
    for x in range(0,len(Ks)-1):
        all_players.append(Ks[x])
    for x in range(0,len(DEFSTs)-1):
        all_players.append(DEFSTs[x])
    all_players = sorted(all_players, key=attrgetter('dollar_value','fantasy_pts'), reverse=True)
    print "sort final values has been run"

def reset_values():
    global QBs,RBs,WRs,TEs,Ks,DEFSTs,all_players,total_starter_PAR,total_bench_PAR,tda
    '''only needs to be done for lists and counting values'''
    QBs = []
    RBs = []
    WRs = []
    TEs = []
    Ks = []
    DEFSTs = []
    all_players = []
    total_starter_PAR = 0
    total_bench_PAR = 0
    tda = 0 #total dollars assigned
    print "reset values has been run"
