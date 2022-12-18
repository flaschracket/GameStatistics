using System;
using System.Collections.Generic;
using System.Configuration;

namespace GameResources.Game
{
    public class Game : IGame
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

        private Field Field;

        public Field field
        {
            get { return Field; }
            set { Field = value; }
        }

        public int currentRound { get; set; }
        public int currentStep { get; set; }
        public Player wonedPlayer { get; set; }
        #endregion

        public Game(string name, string configFilePath)
        {
            Name = name;
            //?? config file?
            InitializeGame(configFilePath);
            int playersQuantity = 4;            
            this.field = new Field();
            this.players = new List<Player>();
            for (int i = 0; i < playersQuantity; i++)
            {
                Player player = new Player("p" + i.ToString());
                this.players.Add(player);
            }
        }

        public void GetSnapshotStepData()
        {
            Console.WriteLine("game Snapshot");
            Console.WriteLine("current round: {0}",currentRound.ToString());
            Console.WriteLine("current step: {0}", currentStep.ToString());
        }

        public void PlayARound()
        {
            currentRound++;
            Console.WriteLine("round {0} is begins...", currentRound.ToString());
            foreach (Player player in players)
            {
                if (currentRound == 10)
                {
                    wonedPlayer = player;
                }
                PlayAStep(player);
            }
        }

        public void PlayAGame()
        {
            Console.WriteLine("a game is begining to play");
            while (wonedPlayer is null)
            {
                PlayARound();
            }
        }

        public void PlayAStep(Player player)
        {
            currentStep++;
            Console.WriteLine("step {0} for player {1} is begining", currentStep.ToString(),player.playerName);
        }

        public void InitializeGame(string configPath)
        {
            // Create configuration reader that reads the files once
            ExeConfigurationFileMap configFileMap = new ExeConfigurationFileMap();
            configFileMap.ExeConfigFilename = configPath;

            // Get the mapped configuration file.
            Configuration gameConfig = ConfigurationManager.OpenMappedExeConfiguration(configFileMap, ConfigurationUserLevel.None);
            
        }
    }
}
