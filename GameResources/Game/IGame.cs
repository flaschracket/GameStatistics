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
        /// <summary>
        /// initilise or set game for the first time
        /// </summary>
        /// <param name="players"></param>
        /// <param name="resources"></param>
        /// <param name="configFile"></param>
        void InitializeGame(List<Player> players,List<Resource> resources, string configFile);
        void PlayARound();
        void PlayAGame();
        void PlayAStep();
        void GetSnapshotStepData();
        
    }
}
