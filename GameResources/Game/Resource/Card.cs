using System;

namespace GameResources.Game.Resource
{
    public class Card 
    {
        public CardType CardType { get; set; }
       
    }

    public enum CardType
    {
        Virus,
        Event,
        Resource
    }
}
