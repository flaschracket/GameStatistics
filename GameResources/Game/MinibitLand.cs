using GameResources.Game.Resource;
using System;
using System.Collections.Generic;
using System.Configuration;

namespace GameResources.Game
{
    public class MinibitLand : Game
    {
        #region properties
        public string Name { get; set; }
        private List<Player> Players;
        //??
        public List<Player> players
        {
            get { return Players; }
            set { Players = value; }
        }

        public List<Card> Deck;
        //right click and rename
        public int CurrentRound { get; set; }
        public int CurrentStep { get; set; }

        public Player WinnedPlayer { get; set; }
        #endregion

        public MinibitLand(string name, string configFilePath)
        {
            Name = name;
            //?? config file?
            InitializeGame(configFilePath);
            int playersQuantity = 4;            
            this.players = new List<Player>();
            for (int i = 0; i < playersQuantity; i++)
            {
                Player player = new Player("p" + i.ToString());
                this.players.Add(player);
            }
            //Deck erzeugt werden 
            this.Deck = new List<Card>();
        }

        public override void GetSnapshotStepData()
        {//Entity Framework
            Console.WriteLine("game Snapshot");
            Console.WriteLine("current round: {0}",CurrentRound.ToString());
            Console.WriteLine("current step: {0}", CurrentStep.ToString());
        }

        public override void PlayARound()
        {
            CurrentRound++;
            Console.WriteLine("round {0} is begins...", CurrentRound.ToString());
            foreach (Player player in players)
            {
                if (CurrentRound == 10)
                {
                    
                    WinnedPlayer = player;
                }
                PlayAStep(player);
            }
        }

        public override void PlayAGame()
        {
            Console.WriteLine("a game is begining to play");
            while (WinnedPlayer is null)
            {
                PlayARound();
            }
        }

        public override void PlayAStep(Player player)
        {
            CurrentStep++;
            Console.WriteLine("step {0} for player {1} is begining", CurrentStep.ToString(),player.PlayerName);
        }

        public override void InitializeGame(string configPath)
        {  //xml 
            // Create configuration reader that reads the files once
            ExeConfigurationFileMap configFileMap = new ExeConfigurationFileMap();
            configFileMap.ExeConfigFilename = configPath;

            // Get the mapped configuration file.
            Configuration gameConfig = ConfigurationManager.OpenMappedExeConfiguration(configFileMap, ConfigurationUserLevel.None);
            
        }
    }
}
