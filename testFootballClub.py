from unittest import main, TestCase
from Oop import FootballClub, FootballTeam

class TestFootballTeam(TestCase):
    def test_constructor(self):
        arsenal = FootballTeam('Arsenal', 'stanford')
        
        self.assertEquals(arsenal.team_name, 'Arsenal')
        
    def test_add_player_method(self):
        MAN_U = FootballTeam('Manchester United', 'UK')
        MAN_U.add_player('Weyne Rooney')
        MAN_U.add_player('Mata')
        MAN_U.add_player('Van Perse')
        MAN_U.add_player('Welback')
        
        self.assertListEqual(['Weyne Rooney', 'Mata', 'Van Perse', 'Welback'], MAN_U.check_players())
        
    def test_coach(self):
        MAN_C = FootballTeam('Manchester City', 'US')
        
        self.assertEqual(MAN_C.set_team_coach('Morinho'), 'Morinho')
        
    def test_home_gound(self):
        MAN_C = FootballTeam('Manchester City', 'US')
        
        self.assertEqual(MAN_C.home_ground, 'US')
        
    def test_remove_player(self):
        MAN_U = FootballTeam('Manchester United', 'UK')
        MAN_U.add_player('Weyne Rooney')
        
        self.assertEqual('Weyne Rooney successfully removed', MAN_U.remove_player('Weyne Rooney'))
        
class TestFootballClub(TestCase):
    def test_inheritance(self):
        gor = FootballClub('gor mahia', 'Kisumu')
        
        self.assertTrue( isinstance(gor, FootballTeam))
        
    def test_leagues(self):
        bandari = FootballClub('Bandari FC', 'Kisumu')
        bandari.join_new_league('SPORTPESA')
        bandari.join_new_league('GO TV SHIELD')
        
        self.assertListEqual(bandari.current_leagues(), ['SPORTPESA', 'GO TV SHIELD'])
        
    def test_sponsors(self):
        mathare = FootballClub('Mathare FC', 'Ruaraka')
        mathare.add_club_sponsor('SPORTPESA')
        
        self.assertListEqual(mathare.check_club_sponsors(), ['SPORTPESA'])

if __name__ == "__main__":
    main()