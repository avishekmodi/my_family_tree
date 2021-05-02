##FT- FAMILY Tree, GF- Grand Father, GM- Grand Mother, F-Father, M-Mother,Sis-Sister
class FT():
    def __init__(self,GF,GM,F,M,Sis,Son):
        self.GrandFather = GF
        self.GrandMother = GM
        self.Father = F
        self.Mother = M
        self.Sisters = Sis
        self.Sons = Son
FT1 = FT('RameshwarModi', 'GangeshwariDevi', 'ManojModi', 'ArtiModi', 2, 2)
FT2 = FT('ManojModi', 'ArtiModi', 'AnilModi', 'SushmaModi', 1, 0)
FT3 = FT('ManojModi', 'ArtiModi', 'VikashModi', 'ShrutiModi', 0, 1)
print(FT3.Father)