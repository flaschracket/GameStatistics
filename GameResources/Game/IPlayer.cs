using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game
{
    interface IPlayer
    {
        void Decide();
        void PlayTheTurn();
        void AllocateResources();


    }
}
