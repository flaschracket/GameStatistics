using System;
using System.Collections.Generic;
using GameResources.Game.Logic;
using GameResources.Game.Resource;

namespace GameResources.Game
{
    public class Player : IPlayer, IDecision
    {
        public string playerName;

        #region resources
        //polymorphy????

        public List<GameResources.Game.Resource.Resource> playerResource
        {
            get => default;
            set
            {
            }
        }
        //or seprate??

        //PCStatus;
        RAM myRAM;
        List<SoftwarePatch> mySoftware;
        List<Card> myCards;



        public Player(string playerName)
        {
            this.playerName = playerName;
        }

        public void AllocateResources()
        {
            throw new NotImplementedException();
        }

        public void Decide()
        {
            throw new NotImplementedException();
        }

        public void PlayTheTurn()
        {
            throw new NotImplementedException();
        }
        #endregion

    }
}


