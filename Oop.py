class FootballTeam(object):
    def __init__(self, team_name, home_ground = ''):
        self.team_name = team_name
        self.home_ground = home_ground
        self.players = []
        self.coach = ''
        self.captain = ''
        self.leagues = []
        self.sponsors = []
        
    def add_player(self, player_name):
        self.players.append(player_name)
        return self.players
    
    def remove_player(self, player_name):
        if player_name in self.players:
            self.players.remove(player_name)
            return "{} successfully removed".format(player_name)
        
        else:
            return "{} no such player in our team".format(player_name)
        
    def set_team_captain(self, captain_name): 
        self.captain = captain_name
        return self.captain
    
    def set_team_coach(self, coach_name):
        self.coach = coach_name
        return self.coach
    
    def change_home_ground(self, home_ground):
        self.home_ground = home_ground
        return self.home_ground
        
    def check_players(self):
        return self.players
    
class FootballClub(FootballTeam):
    def join_new_league(self, league_name):
        self.leagues.append(league_name)
        return self.leagues
    
    def remove_league(self, league_name):
        if league_name in self.leagues:
            self.leagues.remove(league_name)
            return "{} successfully removed".format(league_name)
        
        else:
            return "{} no such league we have joined".format(league_name)
    
    def current_leagues(self):
        return self.leagues
    
    def add_club_sponsor(self, name):
        self.sponsors.append(name)
        return self.sponsors
    
    def remove_club_sponsor(self, name):
        if name in self.sponsors:
            self.sponsors.remove(name)
            return "{} successfully removed".format(name)
        
        else:
            return "{} no such sponsor in our club".format(name)
    
    def check_club_sponsors(self):
        return self.sponsors
    
    
if __name__ == '__main__':
    
    bandari = FootballClub('Bandari FC', 'Kisumu')
    bandari.join_new_league('sportpesa')
    print bandari.leagues
    
    
    