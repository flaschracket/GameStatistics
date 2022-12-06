using GameResources.Game;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources
{
    interface IGame
    {
        void InitializeGame();
        void PlayARound();
        void GetSnapshotStepData();
        
    }
}
