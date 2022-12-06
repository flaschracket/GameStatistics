using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game
{
    class PlayerStatus
    {
        int PausingRoundQuantity;
        bool CanPlay;

        public PlayerStatus(int pausingRoundQuantity=0, bool canPlay=true)
        {
            PausingRoundQuantity = pausingRoundQuantity;
            CanPlay = canPlay;
        }
    }
}
