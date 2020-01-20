# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 18:02:51 2019

@author: pavoni
"""

import testUtility
import Dominion

# Get player names
player_names = ["Annie", "*Ben", "*Carla"]
numPlayers = len(player_names)

# number of curses and victory cards
nV = testUtility.getNumVC(numPlayers)
nC = testUtility.getNumCurses(numPlayers)

# Define box
box = testUtility.getBox(nV)

supply_order = testUtility.getSupplyOrder()

supply_order[0].append('Province')
supply_order[8] = []

# Pick 10 cards from box to be in the supply.
supply = testUtility.makeSupply(box, numPlayers, nV, nC)

# initialize the trash
trash = []

# Construct the Player objects
players = testUtility.makePlayers(player_names)

# Play the game
testUtility.play(supply, supply_order, players, trash)

# Final score
testUtility.endGame(players)
