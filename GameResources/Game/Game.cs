using GameResources.Game;
using GameResources.Game.Resource;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
//basis class nicht Interface
//schnittstelle ist when die unterschied sind
namespace GameResources.Game
{
   public abstract class Game
    {
        public abstract void InitializeGame(string configFile);
        public abstract void PlayARound();
        public abstract void PlayAGame ();
        public abstract void PlayAStep(Player player);
        public abstract void GetSnapshotStepData();
    }
}
