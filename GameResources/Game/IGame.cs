using GameResources.Game;
using GameResources.Game.Resource;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game
{
    interface IGame
    {
        void InitializeGame(string configFile);
        void PlayARound();
        void PlayAGame();
        void PlayAStep(Player player);
        void GetSnapshotStepData();        
    }
}
