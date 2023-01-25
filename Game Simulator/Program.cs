using GameResources.Game;
using System;

namespace Game_Simulator
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            string configPath = "D:\\my works\\Brettspiel\\game simulation\\Game Simulator Code\\GameResources\\Game\\GameSettings.config";
            MinibitLand heartsGame = new MinibitLand("Hearts", configPath);
            heartsGame.GetSnapshotStepData();
            heartsGame.PlayAGame();
            Console.WriteLine("the winner was not defined in programm.");
        }
    }
}
