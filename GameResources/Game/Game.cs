using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GameResources.Game
{
    public class Game : IGame
    {
        string Name = "";
        List<Player> players;

        internal Player Player
        {
            get => default;
            set
            {
            }
        }

        

        //? rules

        //self.currentRound = 0
        //self.currentStep = 0
        //self.samplecounter = samplecounter
        //self.winer = ''
        //# steps
        //self.thisStep = Step(currentStep = self.currentStep, currentgamedeck = self.GD)
        //#self.previousStep = Step(self.currentStep-1)
        //#players -----------------
        //self.listofPlayers = []
        //for x in range(self.GS.NrOfP):
        //   name = 'Player ' + str(x)
        //   self.listofPlayers.append(Player(name))
        //# insert game in DB
        //self.gamesettingsID = gsID
        //self.gameID = mssql.insertGame(self)
        public void GetSnapshotStepData()
        {
            throw new NotImplementedException();
        }

        public void PlayARound()
        {
            throw new NotImplementedException();
            Console.WriteLine("not implemented!");
        }



        public void PlayAGame()
        {
            throw new NotImplementedException();
        }

        public void PlayAStep()
        {
            throw new NotImplementedException();
        }



        public void InitializeGame(List<Player> players, List<Resource> resources, string configFile)
        {
            throw new NotImplementedException();
        }
    }
}
