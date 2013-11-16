import sys
from state import State
from button import Button
from player import Player
from direct.gui.OnscreenImage import OnscreenImage
from panda3d.core import TransparencyAttrib
from direct.showbase.ShowBase import ShowBase

class MainMenuState(State):
    def __init__(self,application):
        self.buttonList = []
        self.menuImageList = []
        self.multiplayerImageList = []
        self.windowX = base.win.getXSize()
        self.windowY = base.win.getYSize()
        self.gameLogoImage = self.makeOnscreenVariable("data/images/gamelogo.png", (self.windowX/2), 0, -170, 1024/4, 512/4) # 1024 x 512
        self.application = application
        #default to pass to gameState
        self.numPlayers = 2
        self.gameType = 1
        self.startingFunds = 300
        self.startingFaction = 0
        #making a popup menu background this needs a new image
       
        
		
		#### FRONT PAGE ################################
        #singleplayerButtonImage = self.makeOnscreenVariable("data/images/single_player_highlight.png",,,) # 512 x 32
        #singleplayerButtonHoverImage = self.makeOnscreenVariable("data/images/single_player_highlight.png",,,) # 512 x 32
        
        multiplayerButtonImage = self.makeOnscreenVariable("data/images/multi-player.png", (self.windowX/2), 0, -(self.windowY/1.5), 512/2.5, 32/2.5) # 512 x 32
        multiplayerButtonHoverImage = self.makeOnscreenVariable("data/images/multi-player_highlight.png", (self.windowX/2), 0, -(self.windowY/1.5), 512/2.5, 32/2.5) # 512 x 32
        self.menuImageList.append(multiplayerButtonImage)
        self.menuImageList.append(multiplayerButtonHoverImage)
        #optionsButtonImage = self.makeOnscreenVariable("data/images/options.png",0,0,0,512/2.5,32/2.5) # 512 x 32
        #optionsButtonHoverImage = self.makeOnscreenVariable("data/images/options_highlight.png",0,0,0,512,32) # 512 x 32    
        quitButtonImage = self.makeOnscreenVariable("data/images/quit.png", (self.windowX/2), 0, -(self.windowY/1.5)-36, 512/2.5, 32/2.5) # 512 x 32
        quitButtonHoverImage = self.makeOnscreenVariable("data/images/quit_highlight.png",(self.windowX/2), 0, -(self.windowY/1.5)-36, 512/2.5, 32/2.5) # 512 x 32
        self.menuImageList.append(quitButtonImage)
        self.menuImageList.append(quitButtonHoverImage)
        
        self.multiplayerPopupImage = self.makeOnscreenVariable("data/images/multiplayer_background.png", (self.windowX/2)-18, 0, -(self.windowY/2)-81, 1024/2.3, 512/3)
        self.multiplayerImageList.append(self.multiplayerPopupImage)
		
		#### MULTIPLAYER PAGE ################################
		#### Game Type #######################################
        gametypeButtonImage = self.makeOnscreenVariable("data/images/game_type.png",(self.windowX/2)-192, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32
        #gametypeButtonHoverImage = self.makeOnscreenVariable("data/images/game_type_highlight.png",(self.windowX/2)-192, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32
        lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+420, 32/2.5, 32/2.5) # 32 x 32
        lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+420, 32/2.5, 32/2.5) # 32 x 32
        conquerButtonImage = self.makeOnscreenVariable("data/images/conquer.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32 
        #conquerButtonHoverImage = self.makeOnscreenVariable("data/images/conquer_highlight.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5)# 512 x 32
        self.multiplayerImageList.append(gametypeButtonImage)
        #self.multiplayerImageList.append(gametypeButtonHoverImage)
        self.multiplayerImageList.append(lessthanButtonImage)
        self.multiplayerImageList.append(lessthanButtonHoverImage)
        self.multiplayerImageList.append(conquerButtonImage)
        #self.multiplayerImageList.append(conquerButtonHoverImage)
        #dominationButtonImage = self.makeOnscreenVariable("data/images/domination.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32 
        #dominationButtonHoverImage = self.makeOnscreenVariable("data/images/domination_highlight.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32
        #survivalButtonImage = self.makeOnscreenVariable("data/images/survival.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32 
        #survivalButtonHoverImage = self.makeOnscreenVariable("data/images/survival_highlight.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32
        greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+420, 32/2.5, 32/2.5) # 32 x 32
        greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+420, 32/2.5, 32/2.5)  # 32 x 32
        self.multiplayerImageList.append(greaterthanButtonImage)
        self.multiplayerImageList.append(greaterthanButtonHoverImage)

		#### Players #########################################
        playersButtonImage = self.makeOnscreenVariable("data/images/player.png",(self.windowX/2)-192, 0, -(self.windowY)+384, 512/2.5, 32/2.5) # 512 x 32
        #playersButtonHoverImage = self.makeOnscreenVariable("data/images/player_highlight.png",(self.windowX/2)-192, 0, -(self.windowY)+384, 512/2.5, 32/2.5) # 512 x 32
        lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #number0ButtonImage = self.makeOnscreenVariable("data/images/0.png",0,0,0,32,32) # 32 x 32
        #number1ButtonImage = self.makeOnscreenVariable("data/images/1.png",0,0,0,32,32) # 32 x 32
        number2ButtonImage = self.makeOnscreenVariable("data/images/2.png", (self.windowX/2)+174, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #number3ButtonImage = self.makeOnscreenVariable("data/images/3.png",0,0,0,32,32) # 32 x 32
        #number4ButtonImage = self.makeOnscreenVariable("data/images/4.png",0,0,0,32,32) # 32 x 32
        #number5ButtonImage = self.makeOnscreenVariable("data/images/5.png",0,0,0,32,32) # 32 x 32
        #number6ButtonImage = self.makeOnscreenVariable("data/images/6.png",0,0,0,32,32) # 32 x 32
        #number7ButtonImage = self.makeOnscreenVariable("data/images/7.png",0,0,0,32,32) # 32 x 32
        #number8ButtonImage = self.makeOnscreenVariable("data/images/8.png",0,0,0,32,32) # 32 x 32
        #number9ButtonImage = self.makeOnscreenVariable("data/images/9.png",0,0,0,32,32) # 32 x 32
        greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+384, 32/2.5, 32/2.5)  # 32 x 32
        self.multiplayerImageList.append(playersButtonImage)
        #self.multiplayerImageList.append(playersButtonHoverImage)
        self.multiplayerImageList.append(lessthanButtonImage)
        self.multiplayerImageList.append(lessthanButtonHoverImage)
        #self.multiplayerImageList.append(number0ButtonImage)
        #self.multiplayerImageList.append(number1ButtonImage)
        self.multiplayerImageList.append(number2ButtonImage)
        #self.multiplayerImageList.append(number3ButtonImage)
        #self.multiplayerImageList.append(number4ButtonImage)
        #self.multiplayerImageList.append(number5ButtonImage)
        #self.multiplayerImageList.append(number6ButtonImage)
        #self.multiplayerImageList.append(number7ButtonImage)
        #self.multiplayerImageList.append(number8ButtonImage)
        #self.multiplayerImageList.append(number9ButtonImage)
        self.multiplayerImageList.append(greaterthanButtonImage)
        self.multiplayerImageList.append(greaterthanButtonHoverImage)

		#### Map #############################################
        #mapButtonImage = self.makeOnscreenVariable("data/images/map.png",0,0,0) # 128 x 32
        #mapButtonHoverImage = self.makeOnscreenVariable("data/images/map_highlight.png",0,0,0) # 128 x 32
        #lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #defaultButtonImage = self.makeOnscreenVariable("data/images/default_map.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32 
        #defaultButtonHoverImage = self.makeOnscreenVariable("data/images/default_map_highlight.png", (self.windowX/2)+174, 0, -(self.windowY)+420, 512/2.5, 32/2.5) # 512 x 32
        #greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+384, 32/2.5, 32/2.5)  # 32 x 32

		#### Epic Creatures ##################################
        #epiccreaturesButtonImage = self.makeOnscreenVariable("data/images/epic_creatures.png",0,0,0) # 512 x 32
        #epiccreaturesButtonHoverImage = self.makeOnscreenVariable("data/images/epic_creatures_highlight.png",0,0,0) # 512 x 32
        #lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #number0ButtonImage = self.makeOnscreenVariable("data/images/0.png",0,0,0,32,32) # 32 x 32
        #number1ButtonImage = self.makeOnscreenVariable("data/images/1.png",0,0,0,32,32) # 32 x 32
        #number2ButtonImage = self.makeOnscreenVariable("data/images/2.png", (self.windowX/2)+174, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #number3ButtonImage = self.makeOnscreenVariable("data/images/3.png",0,0,0,32,32) # 32 x 32
        #number4ButtonImage = self.makeOnscreenVariable("data/images/4.png",0,0,0,32,32) # 32 x 32
        #number5ButtonImage = self.makeOnscreenVariable("data/images/5.png",0,0,0,32,32) # 32 x 32
        #number6ButtonImage = self.makeOnscreenVariable("data/images/6.png",0,0,0,32,32) # 32 x 32
        #number7ButtonImage = self.makeOnscreenVariable("data/images/7.png",0,0,0,32,32) # 32 x 32
        #number8ButtonImage = self.makeOnscreenVariable("data/images/8.png",0,0,0,32,32) # 32 x 32
        #number9ButtonImage = self.makeOnscreenVariable("data/images/9.png",0,0,0,32,32) # 32 x 32
        #greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+384, 32/2.5, 32/2.5) # 32 x 32
        #greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+384, 32/2.5, 32/2.5)  # 32 x 32
		
		#### Map #############################################
        startingfundsButtonImage = self.makeOnscreenVariable("data/images/starting_funds.png",(self.windowX/2)-192, 0, -(self.windowY)+348, 512/2.5, 32/2.5)  # 512 x 32
        #startingfundsButtonHoverImage = self.makeOnscreenVariable("data/images/starting_funds_highlight.png", (self.windowX/2)-192, 0, -(self.windowY)+348, 512/2.5, 32/2.5) # 512 x 32
        lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+348, 32/2.5, 32/2.5) # 32 x 32
        lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+348, 32/2.5, 32/2.5) # 32 x 32
        #number100ButtonImage = self.makeOnscreenVariable("data/images/100.png",0,0,0,128,32) # 128 x 32
        #number200ButtonImage = self.makeOnscreenVariable("data/images/200.png",0,0,0,128,32) # 128 x 32
        number300ButtonImage = self.makeOnscreenVariable("data/images/300.png", (self.windowX/2)+174, 0, -(self.windowY)+348, 128/2.5, 32/2.5) # 128 x 32
        greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+348, 32/2.5, 32/2.5) # 32 x 32
        greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+348, 32/2.5, 32/2.5)  # 32 x 32
        self.multiplayerImageList.append(startingfundsButtonImage)
        #self.multiplayerImageList.append(startingfundsButtonHoverImage)
        self.multiplayerImageList.append(lessthanButtonImage)
        self.multiplayerImageList.append(lessthanButtonHoverImage)
        self.multiplayerImageList.append(number300ButtonImage)
        #self.multiplayerImageList.append(number9ButtonImage)
        self.multiplayerImageList.append(greaterthanButtonImage)
        self.multiplayerImageList.append(greaterthanButtonHoverImage)

		#### Connection Type #################################
        connectiontypeButtonImage = self.makeOnscreenVariable("data/images/connection_type.png",(self.windowX/2)-192, 0, -(self.windowY)+312, 512/2.5, 32/2.5) # 512 x 32
        #connectiontypeButtonHoverImage = self.makeOnscreenVariable("data/images/connection_type_highlight.png",(self.windowX/2)-192, 0, -(self.windowY)+312, 512/2.5, 32/2.5) # 512 x 32
        lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+312, 32/2.5, 32/2.5) # 32 x 32
        lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+312, 32/2.5, 32/2.5) # 32 x 32
        hotseatButtonImage = self.makeOnscreenVariable("data/images/hot_seat.png", (self.windowX/2)+174, 0, -(self.windowY)+312, 512/2.5, 32/2.5) # 512 x 32
        #hotseatButtonHoverImage = self.makeOnscreenVariable("data/images/hot_seat_highlight.png", (self.windowX/2)+174, 0, -(self.windowY)+312, 512/2.5, 32/2.5) # 512 x 32
        greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+312, 32/2.5, 32/2.5) # 32 x 32
        greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+312, 32/2.5, 32/2.5)  # 32 x 32
        self.multiplayerImageList.append(connectiontypeButtonImage)
        #self.multiplayerImageList.append(connectiontypeButtonHoverImage)
        self.multiplayerImageList.append(lessthanButtonImage)
        self.multiplayerImageList.append(lessthanButtonHoverImage)
        self.multiplayerImageList.append(hotseatButtonImage)
        #self.multiplayerImageList.append(hotseatButtonHoverImage)
        self.multiplayerImageList.append(greaterthanButtonImage)
        self.multiplayerImageList.append(greaterthanButtonHoverImage)

		#### Player 1 ########################################
        player1factionButtonImage = self.makeOnscreenVariable("data/images/player_1_faction.png",(self.windowX/2)-192, 0, -(self.windowY)+276, 512/2.5, 32/2.5) # 512 x 32
        #player1factionButtonHoverImage = self.makeOnscreenVariable("data/images/player_1_faction_highlights.png",(self.windowX/2)-192, 0, -(self.windowY)+276, 512/2.5, 32/2.5) # 512 x 32
        lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+276, 32/2.5, 32/2.5) # 32 x 32
        lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+276, 32/2.5, 32/2.5) # 32 x 32
        humanButtonImage = self.makeOnscreenVariable("data/images/human.png", (self.windowX/2)+174, 0, -(self.windowY)+276, 512/2.5, 32/2.5) # 512 x 32
        #humanButtonHoverImage = self.makeOnscreenVariable("data/images/human_highlight.png", (self.windowX/2)+174, 0, -(self.windowY)+276, 512/2.5, 32/2.5) # 512 x 32
        #barbariansButtonImage = self.makeOnscreenVariable("data/images/barbarian.png",0,0,0,512,32) # 512 x 32
        #barbariansButtonHoverImage = self.makeOnscreenVariable("data/images/barbarian_highlight.png",0,0,0,512,32) # 512 x 32
        #elfButtonImage = self.makeOnscreenVariable("data/images/elf.png",0,0,0,512,32) # 512 x 32
        #elfButtonHoverImage = self.makeOnscreenVariable("data/images/elf_highlight.png",0,0,0,512,32) # 512 x 32
        greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+276, 32/2.5, 32/2.5) # 32 x 32
        greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+276, 32/2.5, 32/2.5)  # 32 x 32
        self.multiplayerImageList.append(player1factionButtonImage)
        #self.multiplayerImageList.append(player1factionButtonHoverImage)
        self.multiplayerImageList.append(lessthanButtonImage)
        self.multiplayerImageList.append(lessthanButtonHoverImage)
        self.multiplayerImageList.append(humanButtonImage)
        #self.multiplayerImageList.append(humanButtonHoverImage)
        self.multiplayerImageList.append(greaterthanButtonImage)
        self.multiplayerImageList.append(greaterthanButtonHoverImage)

		#### Player 2 ########################################
        player2factionButtonImage = self.makeOnscreenVariable("data/images/player_2_faction.png",(self.windowX/2)-192, 0, -(self.windowY)+240, 512/2.5, 32/2.5) # 512 x 32
        #player2factionButtonHoverImage = self.makeOnscreenVariable("data/images/player_2_faction_hightlight.png",(self.windowX/2)-192, 0, -(self.windowY)+240, 512/2.5, 32/2.5) # 512 x 32
        lessthanButtonImage = self.makeOnscreenVariable("data/images/less_than.png", (self.windowX/2)+48, 0, -(self.windowY)+240, 32/2.5, 32/2.5) # 32 x 32
        lessthanButtonHoverImage = self.makeOnscreenVariable("data/images/less_than_highlight.png", (self.windowX/2)+48, 0, -(self.windowY)+240, 32/2.5, 32/2.5) # 32 x 32
        humanButtonImage = self.makeOnscreenVariable("data/images/human.png", (self.windowX/2)+174, 0, -(self.windowY)+240, 512/2.5, 32/2.5) # 512 x 32
        #humanButtonHoverImage = self.makeOnscreenVariable("data/images/human_highlight.png", (self.windowX/2)+174, 0, -(self.windowY)+240, 512/2.5, 32/2.5) # 512 x 32
        #barbariansButtonImage = self.makeOnscreenVariable("data/images/barbarian.png",0,0,0,512,32) # 512 x 32
        #barbariansButtonHoverImage = self.makeOnscreenVariable("data/images/barbarian_highlight.png",0,0,0,512,32) # 512 x 32
        #elfButtonImage = self.makeOnscreenVariable("data/images/elf.png",0,0,0,512,32) # 512 x 32
        #elfButtonHoverImage = self.makeOnscreenVariable("data/images/elf_highlight.png",0,0,0,512,32) # 512 x 32
        greaterthanButtonImage = self.makeOnscreenVariable("data/images/greater_than.png", (self.windowX/2)+304, 0, -(self.windowY)+240, 32/2.5, 32/2.5) # 32 x 32
        greaterthanButtonHoverImage = self.makeOnscreenVariable("data/images/greater_than_highlight.png", (self.windowX/2)+304, 0, -(self.windowY)+240, 32/2.5, 32/2.5)  # 32 x 32
        print greaterthanButtonHoverImage
        self.multiplayerImageList.append(player2factionButtonImage)
        #self.multiplayerImageList.append(player2factionButtonHoverImage)
        self.multiplayerImageList.append(lessthanButtonImage)
        self.multiplayerImageList.append(lessthanButtonHoverImage)
        self.multiplayerImageList.append(humanButtonImage)
        #self.multiplayerImageList.append(humanButtonHoverImage)
        self.multiplayerImageList.append(greaterthanButtonImage)
        self.multiplayerImageList.append(greaterthanButtonHoverImage)

		#### Start and back buttons###########################
        startButtonImage = self.makeOnscreenVariable("data/images/start.png", (self.windowX/2)-112, 0, -(self.windowY)+176, 512/2.5, 32/2.5) # 512 x 32
        startButtonHoverImage = self.makeOnscreenVariable("data/images/start_highlight.png", (self.windowX/2)-112, 0, -(self.windowY)+176, 512/2.5, 32/2.5) # 512 x 32
        backButtonImage = self.makeOnscreenVariable("data/images/back.png", (self.windowX/2)+92, 0, -(self.windowY)+176, 512/2.5, 32/2.5) # 512 x 32
        backButtonHoverImage = self.makeOnscreenVariable("data/images/back_highlight.png", (self.windowX/2)+92, 0, -(self.windowY)+176, 512/2.5, 32/2.5) # 512 x 32
        self.multiplayerImageList.append(startButtonImage)
        self.multiplayerImageList.append(startButtonHoverImage)
        self.multiplayerImageList.append(backButtonImage)
        self.multiplayerImageList.append(backButtonHoverImage)
        print self.multiplayerImageList
        #Button(xpos,ypos,width,height,image,imageh,handler)
        #gamelogo = Button(self.windowX / 2, self.windowY / 2, 1024, 512, gamelogoButtonImage, gamelogoButtonImage)
        #singleplayer = Button(self.windowX / 2, self.windowY / 2, 512, 32, singleplayerButtonImage, singleplayerButtonHoverImage, self.singleplayerHandler)
        multiplayer = Button((self.windowX/2), -(self.windowY/1.5), 512, 32, multiplayerButtonImage, multiplayerButtonHoverImage, self.multiPlayerHandler)
        self.buttonList.append(multiplayer)
        #options = Button(self.windowX / 2, self.windowY / 2, 512, 32, optionsButtonImage, optionsButtonHoverImage, self.optionsHandler)
        quit = Button((self.windowX/2), -(self.windowY/1.5)-36, 512, 32, quitButtonImage, quitButtonHoverImage, self.quitHandler)
        self.buttonList.append(quit)
        #gametype = Button(self.windowX / 2, self.windowY / 2, 512, 32, gametypeButtonImage, gametypeButtonHoverImage, self.gametypeHandler)
        lessthan = Button((self.windowX/2)+48, -(self.windowY)+384, 32, 32, lessthanButtonImage, lessthanButtonHoverImage, self.lessthanHandler)
        self.buttonList.append(lessthan)
        #conquer = Button(self.windowX / 2, self.windowY / 2, 512, 32, conquerButtonImage, conquerButtonHoverImage, self.conquerHandler)
        greaterthan = Button((self.windowX/2)+304, -(self.windowY)+384, 32, 32, greaterthanButtonImage, greaterthanButtonHoverImage, self.greaterthanHandler)
        self.buttonList.append(greaterthan)
        #players = Button(self.windowX / 2, self.windowY / 2, 512, 32,playersButtonImage, playersButtonHoverImage, self.playersHandler)
        #number0 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number0ButtonImage, number0ButtonImage, self.number0Handler)
        #number1 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number1ButtonImage, number1ButtonImage, self.number1Handler)
        #number2 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number2ButtonImage, number2ButtonImage, self.number2Handler)
        #number3 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number3ButtonImage, number3ButtonImage, self.number3Handler)
        #number4 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number4ButtonImage, number4ButtonImage, self.number4Handler)
        #number5 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number5ButtonImage, number5ButtonImage, self.number5Handler)
        #number6 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number6ButtonImage, number6ButtonImage, self.number6Handler)
        #number7 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number7ButtonImage, number7ButtonImage, self.number7Handler)
        #number8 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number8ButtonImage, number8ButtonImage, self.number8Handler)
        #number9 = Button(self.windowX / 2, self.windowY / 2, 32, 32, number9ButtonImage, number9ButtonImage, self.number9Handler)
        #number100 = Button(self.windowX / 2, self.windowY / 2, 128, 32, number100ButtonImage, number100ButtonImage, self.number100Handler)
        #number200 = Button(self.windowX / 2, self.windowY / 2, 128, 32, number200ButtonImage, number200ButtonImage, self.number200Handler)
        #number300 = Button(self.windowX / 2, self.windowY / 2, 128, 32, number300ButtonImage, number300ButtonImage, self.number300Handler)
        #map = Button(self.windowX / 2, self.windowY / 2, 128, 32, mapButtonImage, mapButtonHoverImage, self.mapHandler)
        #epiccreatures = Button(self.windowX / 2, self.windowY / 2, 512, 32, epiccreaturesButtonImage, epiccreaturesButtonHoverImage, self.epiccreaturesHandler)
        #startingfunds = Button(self.windowX / 2, self.windowY / 2, 512, 32, startingfundsButtonImage, startingfundsButtonHoverImage, self.startingfundsHandler)
        #connectiontype = Button(self.windowX / 2, self.windowY / 2, 512, 32, connectiontypeButtonImage, connectiontypeButtonHoverImage, self.connectiontypeHandler)
        #hotseat = Button(self.windowX / 2, self.windowY / 2, 512, 32, hotseatButtonImage, hotseatButtonHoverImage, self.hotseatHandler)
        #player1faction = Button(self.windowX / 2, self.windowY / 2, 512, 32, player1factionButtonImage, player1factionButtonHoverImage, self.player1factionHandler)
        #player2faction = Button(self.windowX / 2, self.windowY / 2, 512, 32, player2factionButtonImage, player2factionButtonHoverImage, self.player2factionHandler)
        #human = Button(self.windowX / 2, self.windowY / 2, 512, 32, humanButtonImage, humanButtonHoverImage, self.humanHandler)
        #barbarian = Button(self.windowX / 2, self.windowY / 2, 512, 32, barbarianButtonImage, barbarianButtonHoverImage, self.barbarianHandler)
        #elf = Button(self.windowX / 2, self.windowY / 2, 512, 32, elfButtonImage, elfButtonHoverImage, self.elfHandler)
        start = Button((self.windowX/2)-112, -(self.windowY)+176, 512, 32, startButtonImage, startButtonHoverImage, self.startHandler)
        self.buttonList.append(start)
        back = Button((self.windowX/2)+92, -(self.windowY)+176, 512, 32, backButtonImage, backButtonHoverImage, self.backHandler)
        self.buttonList.append(back)
        #create handlers for start, back, gt, lt, multiplayer, quit,options,singleplayer 
        #only show what main menu to start
        #something weird going on here
        self.showMenuImages(False)
        
    def mainLoop(self,task):
        #game logic here
        #loop over things like buttons and the like
        return task.cont
        
    def makeOnscreenVariable(self,fileName,x,y,z,width,height):
        imageVariable = OnscreenImage(image = fileName)
        imageVariable.reparentTo(pixel2d)
        imageVariable.setPos(x,y,z)
        imageVariable.setScale(width,1,height)
        #probably needs an include of some sort
        imageVariable.setTransparency(TransparencyAttrib.MAlpha)
        return imageVariable
        
    def run(self):
        taskMgr.add(self.mainLoop,"menuLoop")
        
    def multiPlayerHandler(self):
        self.showImages(False)
        self.showMenuImages(True)
        
    def quitHandler(self):
        #does quit when the quit button is pushed
        sys.exit()
        
    def startHandler(self):
        #does startup when startof game situation happens
        players = []
        for player in range(self.numPlayers):
            newPlayer = Player(player,self.startingFunds,self.startingFaction,0,0)
            players.append(newPlayer)
        self.showImages(False)
        self.showMenuImages(False)
        self.gameLogoImage.Hide()
        self.application.stateManager.stateList['game'].initializeState(players)  
        self.application.stateManager.setCurrentState('game')
    
    def showImages(self,setting):
        for image in self.menuImageList:
            if setting:
                image.show()
            else:
                image.hide()
    
    def showMenuImages(self,setting):
        for image in self.multiplayerImageList:
            if setting:
                image.show()
            else:
                image.hide()
        
    def greaterthanHandler(self):
        pass
        
    def lessthanHandler(self):
        pass
        
#    def optionsHandler(self):
#        pass
        
#    def singleplayerHandler(self):
#        pass
        
    def backHandler(self):
        self.showImages(True)
        self.showMenuImages(False)
    