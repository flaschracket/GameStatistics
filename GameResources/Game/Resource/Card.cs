using System;

namespace GameResources.Game.Resource
{
    public class Card : Resource
    {
        
        public Enum GetStatus()
        {
            throw new NotImplementedException();
        }

        public bool IsPublic()
        {
            return true;
        }

        Enum GetVariation()
        {
            Resource resource = new Resource();
            return ResourceVariation.Card;
        }

        private enum CardType
        {
            Worm,
            Event,
            Resource
        }
    }
}
