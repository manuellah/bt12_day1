class FootballTeam(object):
    def __init__(self, team_name, home_ground = ''):
        self.team_name = team_name
        self.home_ground = home_ground
        self.players = []
        self.coach = ''
        self.captain = ''
        self.leagues = []
        self.sponsors = []
        
    def add_player(player_name):
        self.players.append(player_name)
        return self.players
    
    def remove_player(player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            return "{} successfully removed".format(player_name)
        
        else:
            return "{} no such player in our team".format(player_name)
        
    def set_team_captain(captain_name): 
        self.captain = captain_name
        return self.captain
    
    def set_team_coach(coach_name):
        self.coach = coach_name
        return self.coach
    
    def change_home_ground(home_ground):
        self.home_ground = home_ground
        return self.home_ground
        
    def check_players():
        return self.players
    
class FootballClub(FootballTeam):
    def join_new_league(league_name):
        self.leagues.append(self.leagues)
    
    def remove_league(league_name):
        if league_name in self.leagues:
            self.leagues.remove(league_name)
            return "{} successfully removed".format(league_name)
        
        else:
            return "{} no such league we have joined".format(league_name)
    
    def current_leagues():
        return self.leagues
    
    def add_club_sponsor(name):
        self.sponsors.append(name)
        return self.sponsors
    
    def remove_club_sponsor(name):
        if name in self.sponsors:
            self.sponsors.remove(name)
            return "{} successfully removed".format(name)
        
        else:
            return "{} no such sponsor in our club".format(name)
    
    def check_club_sponsors():
        return self.sponsors
    
    
    
    
    
    
    
    
    