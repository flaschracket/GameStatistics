using System;
using System.Collections.Generic;
using GameResources.Game.Logic;
using GameResources.Game.Resource;

namespace GameResources.Game
{
    public class Player 
    {
        //property-keine logik
        public string PlayerName { get; set; }

        #region resources
        //PCStatus;
        public RAM myRAM;
        public List<SoftwarePatch> mySoftware;
        public List<Card> myCards;
        int CountCPU; 

        public Player(string playerName)
        {
            this.PlayerName = playerName;
            myRAM = new RAM();
            mySoftware = new List<SoftwarePatch>();
            myCards = new List<Card>();
            CountCPU = 1;
        }
        #endregion

    }
}


