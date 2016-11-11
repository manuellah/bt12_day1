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
    def join_new_league('league_name'):
        pass
    
    def remove_league('league_name'):
        pass
    
    def current_leagues():
        pass
    
    def add_club_sponsor('name'):
        pass
    
    def remove_club_sponsor('name'):
        pass
    
    
    
    
    
    
    
    
    
    