using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using GameResources.Game.Logic;
using GameResources.Game.Resource;

namespace GameResources.Game
{
    class Player: IPlayer, IDecision, IResource
    {
        string playerName = "player x";
        // player turn number, when is the time for him to play
        private int OrderOfPlayer = -1;
        private PlayerStatus playerStatus;
        
        #region resources
        List<IResource> PlayerResources;
        //or seprate??

        //PCStatus;
        RAM myRAM;
        List<SoftwarePatch> mySoftware;
        List<Card> myCards;
        #endregion

        public Resource.Resource Resource
        {
            get => default;
            set
            {
            }
        }

        internal PlayerStatus PlayerStatus
        {
            get => default;
            set
            {
            }
        }

        public void AllocateResources()
        {
            throw new NotImplementedException();
        }

        public void Decide()
        {
            throw new NotImplementedException();
        }

        public bool IsPublic()
        {
            throw new NotImplementedException();
        }

        public void PlayTheTurn()
        {
            throw new NotImplementedException();
        }

        Enum IResource.GetStatus()
        {
            throw new NotImplementedException();
        }

        ICollection<string> IResource.GetType()
        {
            throw new NotImplementedException();
        }
    }
}


